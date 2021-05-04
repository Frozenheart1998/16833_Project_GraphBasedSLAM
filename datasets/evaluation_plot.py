import matplotlib.pyplot as plt
import numpy as np

import glob
import os.path as osp
import argparse

from graphslam.load import load_g2o_se2

parser = argparse.ArgumentParser(
    description="A 2D Pose SLAM example that reads input from g2o ")
parser.add_argument('-i_gt', '--input_gt', help='input file g2o format', default="gt_M3500_g2o.g2o")
parser.add_argument('-i_est', '--input_est', help='estimated input file', default="output_M3500_g2o.g2o")
parser.add_argument('-o', '--output_path',
                    help="the path to the output file", default=".")
parser.add_argument("-p", "--plot", action="store_true",
                    help="Flag to plot results")
parser.add_argument("-N", "--number_of_vertex", help="number of vertex", default=3500)
args = parser.parse_args()

inputGtFle = args.input_gt
inputEstFile = args.input_est
outputFilePath = args.output_path
N = args.number_of_vertex

gt = np.loadtxt(inputGtFle, usecols=(2, 3, 4), max_rows=N)
est = np.loadtxt(inputEstFile, usecols=(2, 3, 4), max_rows=N)
g =load_g2o_se2(inputGtFle)
f = load_g2o_se2(inputEstFile)
print("chi2 of gt ",g.calc_chi2())
print("chi2 of est ",f.calc_chi2())

##calculate ATE
## TODO:
gt_centroid = np.sum(gt, axis=0) / N
est_centroid = np.sum(est, axis=0) / N
delta_centroid = est_centroid - gt_centroid

# (gt-gt_centroid)-(est-est_centroid)
error = gt - est + delta_centroid
norm = np.linalg.norm(error, axis=1)
sq = np.square(norm)
ATE = np.sum(sq)/N

error_noS = gt - est
norm_noS = np.linalg.norm(error_noS, axis=1)
sq_noS = np.square(norm_noS)
ATE_noS = np.sum(sq_noS)/N

##calculate RPE relative pose error
step = 10
M = N-step
gt_0 = gt[0:M, :]
gt_1 = gt[step:, :]
est_0 = est[0:M, :]
est_1 = est[step:, :]
err = (gt_1 - gt_0) - (est_1 - est_0)
nrm = np.linalg.norm(err, axis=1)
sqr = np.square(nrm)
RPE = np.sum(sqr)/M

print("RPE ",RPE," ATE ",ATE," ATE_noS ",ATE_noS)



g.plot(vertex_markersize=1)
f.plot(vertex_markersize=1)
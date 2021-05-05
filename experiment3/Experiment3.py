import numpy as np
import random
import pandas as pd
import matplotlib.pyplot as plt

def loadfile(filename,originchi2):
    df =  pd.read_csv(filename,skiprows=(0,1,2,3),usecols=[0,1,2,3],sep=' ',header=None)
    chi2 = df.iloc[:,3].values
    c2 = np.zeros((len(chi2)+1,))
    c2[0] = originchi2
    c2[1:] = chi2
    iter = np.arange(0,len(c2))

    # print(df)
    return iter,c2

def plot(fileLM,fileDL,fileGN,c,title,n,originchi2):
    itrLM, chi2LM = loadfile(fileLM,originchi2)
    itrDL, chi2DL = loadfile(fileDL,originchi2)
    itrGN, chi2GN = loadfile(fileGN,originchi2)
    lw=2
    if len(itrLM) < n:
        plt.plot(itrLM, chi2LM, label="levenberg-marquardt",linewidth=lw,c = "b")
    else:
        plt.plot(itrLM[:n], chi2LM[:n], label="levenberg-marquardt",linewidth=lw,c = "b")

    if len(itrDL) < n:
        plt.plot(itrDL, chi2DL, label="dogleg",linewidth=lw,c = "g")
    else:
        plt.plot(itrDL[:n], chi2DL[:n], label="dogleg",linewidth=lw,c = "g")

    if len(itrGN) < n:
        plt.plot(itrGN, chi2GN, label="Gauss Newton",linewidth=lw-1,c = "r")
    else:
        plt.plot(itrGN[:n], chi2GN[:n], label="Gauss Newton",linewidth=lw-1,c = "r")

    plt.title(title)
    plt.xlabel("iterations")
    plt.ylabel("chi2")
    plt.legend()
    temp = c.replace(".", "_");
    plt.savefig("M3500_plot_" + temp + ".png")
    plt.show()

def plot_part(fileLM,fileDL,fileGN,c,title,n,originchi2):
    itrLM, chi2LM = loadfile(fileLM,originchi2)
    itrDL, chi2DL = loadfile(fileDL,originchi2)
    itrGN, chi2GN = loadfile(fileGN,originchi2)
    lw=2
    if len(itrLM) < n:
        plt.plot(itrLM[1:], chi2LM[1:], label="levenberg-marquardt",linewidth=lw,c = "b")
    else:
        plt.plot(itrLM[1:n], chi2LM[1:n], label="levenberg-marquardt",linewidth=lw,c = "b")

    if len(itrDL) < n:
        plt.plot(itrDL[1:], chi2DL[1:], label="dogleg",linewidth=lw,c = "g")
    else:
        plt.plot(itrDL[1:n], chi2DL[1:n], label="dogleg",linewidth=lw,c = "g")

    if len(itrGN) < n:
        plt.plot(itrGN[1:], chi2GN[1:], label="Gauss Newton",linewidth=lw-1,c = "r")
    else:
        plt.plot(itrGN[1:n], chi2GN[1:n], label="Gauss Newton",linewidth=lw-1,c = "r")

    plt.title(title+" (part)")
    plt.xlabel("iterations")
    plt.ylabel("chi2")
    plt.legend()
    temp = c.replace(".", "_");
    plt.savefig("M3500_plot_" + temp +"_part" ".png")
    plt.show()


cov=(0.5,1.0,1.5,2.0)
origin_chi2_cov = (3.416705,13.482164,29.854827, 51.897265)
for i,c in enumerate(cov):
    originchi2 = origin_chi2_cov[i]
    fileLM = "M3500_Huber_LM_cholmod_"+str(c)+".txt"
    fileDL = "M3500_Huber_DL_cholmod_" + str(c) + ".txt"
    fileGN = "M3500_Huber_GN_cholmod_" + str(c) + ".txt"
    plot(fileLM,fileDL,fileGN,str(c),"covariance="+str(c),8,originchi2)
    plot_part(fileLM, fileDL, fileGN, str(c), "covariance=" + str(c), 6, originchi2)

origin_chi2_og = (2566434.290765,69142.942410 )
for j,g in enumerate(("Olsen","G2O")):
    originchi2 =origin_chi2_og[j]
    fileLM = "M3500"+str(g)+"_Huber_LM_cholmod.txt"
    fileDL = "M3500"+str(g)+"_Huber_DL_cholmod.txt"
    fileGN = "M3500"+str(g)+"_Huber_GN_cholmod.txt"
    plot(fileLM, fileDL, fileGN, g,g, 10,originchi2)
    plot_part(fileLM, fileDL, fileGN, g, g, 5, originchi2)


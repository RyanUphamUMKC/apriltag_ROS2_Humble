import glob
import numpy as np
import argparse
import pandas as pd
import matplotlib.pyplot as plt
import os

experimentFiles = "./isaac_ros-dev/experiments/data/"
tagNum = "0"

def getDataFiles(expFile: str):
    return sorted(glob.glob(experimentFiles + expFile + '/**/data.csv', recursive= True), key= os.path.getctime)

def getRealFile(expFile: str):
    real = pd.read_csv(experimentFiles + expFile + "/real.csv")
    realz = real["Z"]
    realx = real["X"]
    realy = real["Y"]
    print(real)

    return realx, realy, realz

def getStats(dim: str, stats, args):
    distStats = []
    for x in range(args):
        name = "/tag_detections/detections." + tagNum + "/pose/pose/pose/position/" + dim
        distStats.append(stats[x].loc[:,[name]])
        distStats[x] = distStats[x].T
    return distStats

def buildFrame(distStat):
    dsSet = pd.concat(distStat, axis= 0, join= "inner")
    dsSet = dsSet.reset_index(drop= True)
    return dsSet

def combine(real, dsSet):
    pieces = (real, dsSet)
    wholeStat = pd.concat(pieces, axis= 1)
    return wholeStat

def add_tpre(wholeStat, dim: str):
    tpre = wholeStat['mean'].sub(wholeStat[dim]).div(wholeStat[dim]).abs().to_frame('trueRelErr')
    pieces = (wholeStat, tpre)
    wholeStat = pd.concat(pieces, axis= 1)
    return wholeStat



#add parsing arguments for command line 
print("[Experiment Data Hander]\n ")
parser = argparse.ArgumentParser(description="Read and analyse apriltag experimantal data from csv files")
parser.add_argument('--fname', type=str, help='filename', 
       default="defaultFile")
parser.add_argument('--dnum', type=int, help='number of data files', 
       default= 0)

#parse
args = parser.parse_args()

#errors for no inputs
if(args.fname == "defaultFile"):
    print("ERROR: no file given use: \'-fname <experimentFile>\'")
    exit()

if(args.dnum == 0):
    print("ERROR: need number of data files use: \'-dnum <number>\'")
    exit()

print("["+experimentFiles +args.fname + '/**/Data.csv]\n')

#take in all data files in experiment folder
dataFiles = getDataFiles(args.fname)

#read in data files
realx, realy, realz = getRealFile(args.fname)
df = []
for x in range(args.dnum):
    df.append(pd.read_csv(dataFiles[x]))

#take statistics for the files
stats = []
for x in range(args.dnum):
    stats.append(df[x].describe(percentiles= None))

#get the average distance in each file
#dist = []
#for x in range(args.dnum):
#    dist.append(stats[x].iloc[3,8])

#organize the stats array using the distances(low to high)
#dist, stats = zip(*sorted(zip(dist, stats)))

#get statistics data of x, y, z from files
distStatsX = getStats("x", stats, args.dnum)
distStatsY = getStats("y", stats, args.dnum)
distStatsZ = getStats("z", stats, args.dnum)

#combine statistics to single dataframe for each dimension
dsSetX = buildFrame(distStatsX)
dsSetY = buildFrame(distStatsY)
dsSetZ = buildFrame(distStatsZ)

#add real Z data to statistics data
wholeStatX = combine(realx, dsSetX)
wholeStatY = combine(realy, dsSetY)
wholeStatZ = combine(realz, dsSetZ)


#calculate true percent relative error and add to wholeStat
"""
tpre = wholeStatZ['mean'].sub(wholeStatZ['Z']).div(wholeStatZ['Z']).mul(100).to_frame('truePercRelErr')
pieces = (wholeStatZ, tpre)
wholeStat = pd.concat(pieces, axis= 1)
"""

#add tpre to wholeStats
wholeStatX = add_tpre(wholeStatX, "X")
wholeStatY = add_tpre(wholeStatY, "Y")
wholeStatZ = add_tpre(wholeStatZ, "Z")

print(wholeStatX)
print(wholeStatY)
print(wholeStatZ)

#re parse data for graphing purposes 
xTrue = wholeStatX["X"]
zTrue = wholeStatZ["Z"]
xMeas = wholeStatX["mean"]
zMeas = wholeStatZ["mean"]
xStd = wholeStatX["std"]
zStd = wholeStatZ["std"]
xTPRE = wholeStatX["trueRelErr"]
zTPRE = wholeStatZ["trueRelErr"]

#plot xy graph of real vs measured points
plt.figure(0)
plt.scatter(xTrue, zTrue, s= 10, c= "r", marker= "s", label= "real")
plt.scatter(xMeas, zMeas, s= 10, c= "b", marker= "o", label= "meas")
plt.legend(loc='best')
plt.xlabel("x [m]")
plt.ylabel("z [m]")
plt.title(args.fname + " XY")
plt.savefig(experimentFiles + args.fname + "/xyPlot.png")

#plot distance vs std graph for x and z 
plt.figure(1)
plt.scatter(zTrue, zStd, s= 10, c= "b", marker= "s",)
plt.xlabel("z distance [m]")
plt.ylabel("std")
plt.title(args.fname + " Z STD")
plt.savefig(experimentFiles + args.fname + "/stdZPlot.png")
plt.figure(2)
plt.scatter(zTrue, xStd, s= 10, c= "b", marker= "s",)
plt.xlabel("z distance [m]")
plt.ylabel("std")
plt.title(args.fname + " X STD")
plt.savefig(experimentFiles + args.fname + "/stdXPlot.png")

#plot distance vs true percent relative error for x and z with standard deviation error bars
plt.figure(3)
plt.errorbar(zTrue, zTPRE, yerr=zStd, fmt="o", ecolor= "r", barsabove= True, capsize= 5, capthick= 1)
plt.xlabel("z distance [m]")
plt.ylabel("z true relative error")
plt.title(args.fname + " z vs z error")
plt.savefig(experimentFiles + args.fname + "/zVSzError.png")
plt.figure(4)
plt.errorbar(zTrue, xTPRE, yerr=xStd, fmt="o", ecolor= "r", barsabove= True, capsize= 5, capthick= 1)
plt.xlabel("z distance [m]")
plt.ylabel("x true relative error")
plt.title(args.fname + " z vs x error")
plt.savefig(experimentFiles + args.fname + "/zVSxError.png")

#plot x dist vs zTRE
plt.figure(5)
plt.errorbar(xTrue, zTPRE, yerr=xStd, fmt="o", ecolor= "r", barsabove= True, capsize= 5, capthick= 1)
plt.xlabel("x distance [m]")
plt.ylabel("z true relative error")
plt.title(args.fname + " x vs z error")
plt.savefig(experimentFiles + args.fname + "/xVSzError.png")
plt.figure(6)
plt.errorbar(xTrue, xTPRE, yerr=xStd, fmt="o", ecolor= "r", barsabove= True, capsize= 5, capthick= 1)
plt.xlabel("x distance [m]")
plt.ylabel("x true relative error")
plt.title(args.fname + " x vs x error")
plt.savefig(experimentFiles + args.fname + "/xVSxError.png")



xz = combine(wholeStatX, wholeStatY)
wholeStatXYZ = combine(xz, wholeStatZ)

wholeStatXYZ.to_csv(experimentFiles + args.fname + "/STAT_ANAL.csv")







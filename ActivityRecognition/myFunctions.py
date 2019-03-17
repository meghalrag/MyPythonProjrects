import numpy as np
import matplotlib.pyplot as plt
import os

def CalculateSMA(x,y,z):
    modX = np.absolute(x)
    modY = np.absolute(y)
    modZ = np.absolute(z)
    numerator = (np.sum(modX) + np.sum(modY) + np.sum(modZ))
    denominator = x.shape
    sma = numerator/denominator
    return sma

def CalculateSVM(x,y,z):
    svmOut =  np.sqrt(np.square(x)+np.square(y)+np.square(z))
    return svmOut

def CalculateTA(x,y,z):
    denominator = CalculateSVM(x,y,z)
    numerator = y
    taOut = np.arcsin(numerator/denominator)
    return taOut

def featureExtractor(myPath,label,classNum):
    global features
    FeaturesAll = np.zeros((1,15))
    onlyfiles = [f for f in os.listdir(myPath)]  # if isfile(join(myPath, f))]
##    print('onlyfilegws',onlyfiles)
    # print(len(onlyfiles))
    print()
    for currentFileNum in range(len(onlyfiles)):
        label.append(classNum)
        plt.close('all')
        fileName = myPath + onlyfiles[currentFileNum]
        # print(onlyfiles[currentFileNum])
        num_lines = sum(1 for line in open(fileName))
        print('numlines=',num_lines)
        f = open(fileName, 'r')
        message = f.readlines()
        aa = np.array([])
        for lineNum in range(1,num_lines-1):
            x = message[lineNum]
            currentLine = np.fromstring(x, dtype=float, sep=',')
            # print ('current=',currentLine)
            aa = np.concatenate((aa, currentLine), axis=0)
            f.close()
            #print(aa)
        new1 = np.reshape(aa, (num_lines - 2, 3))
        print(str(currentFileNum + 1) + ": " + onlyfiles[currentFileNum] + ' contains ' + str(new1.shape[0]) + ' values')
        # print(type(currentLine))

        xValues = new1[:, 0]
        yValues = new1[:, 1]
        zValues = new1[:, 2]

        plt.plot(xValues, 'r--', yValues, 'b--', zValues, 'g--')
        plt.title('Values')
        plt.grid(True)
        plt.gca().legend(('xValues', 'yValues', 'zValues'))
        # plt.show()
        # plt.draw()
        # print('Calculating Features...')
        xMean = np.mean(xValues)
        yMean = np.mean(yValues)
        zMean = np.mean(zValues)

        xMin = np.min(xValues)
        yMin = np.min(yValues)
        zMin = np.min(zValues)

        xMax = np.max(xValues)
        yMax = np.max(yValues)
        zMax = np.max(zValues)

        xStd = np.std(xValues)
        yStd = np.std(yValues)
        zStd = np.std(zValues)

        SMA = CalculateSMA(xValues, yValues, zValues)

        SVMvalue = CalculateSVM(xMean, yMean, zMean)

        TAvalue = CalculateTA(xMean, yMean, zMean)

        features = [xMean, yMean, zMean, xMin, yMin, zMin, xMax, yMax, zMax,
                xStd, yStd, zStd, SMA, SVMvalue, TAvalue]
        # ff = [features , features]
        FeaturesAll = np.vstack((FeaturesAll, features))

    #print(FeaturesAll.shape)
    # plt.draw()
    # plt.show()
    FeaturesAll = np.delete(FeaturesAll, (0), axis=0)
    return FeaturesAll,label

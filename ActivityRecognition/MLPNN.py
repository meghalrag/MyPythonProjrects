import os
import codecs,json
import numpy as np
import matplotlib.pyplot as plt
import myFunctions

myPath = os.getcwd()
target = []

StandingPath= myPath + "/data/standing/"
print(StandingPath)
featStanding,target = myFunctions.featureExtractor(StandingPath,target,1)
# target.append(1)#np.ones(1,len(featStanding)))
print(featStanding)


WalkingPath= myPath + "/data/walking/"
featWalking,target = myFunctions.featureExtractor(WalkingPath,target,2)
print(WalkingPath)

# print((featWalking.shape))

SittingPath= myPath + "/data/sitting/"
featSitting,target = myFunctions.featureExtractor(SittingPath,target,3)
print(SittingPath)

print()
print( target)
# print(len(featSitting))

AllFeatures = np.vstack((featStanding,featWalking,featSitting))
print('\nTotal of ' + str(AllFeatures.shape[0]) + ' files ' + ' with ' + str(AllFeatures.shape[1]) + ' features each.')


# plt.show()


for currentPlot in range(14):
    plt.subplot(3,5,currentPlot+1)
    plt.plot(featStanding[:, currentPlot], 'r.', featWalking[:, currentPlot], 'b.', featSitting[:, currentPlot], 'g.')
    frame1 = plt.gca()
    plt.title(('Feature'+ str(currentPlot+1)))
    frame1.axes.get_xaxis().set_visible(False)
plt.suptitle('Feature Values')
frame1.legend(('Standing', 'Walking', 'Sitting'))
plt.show()

file1_path = "FeatureData.json"
print('Saving the database as ' + file1_path)
AllFeatures = AllFeatures.tolist()


json.dump(AllFeatures, codecs.open(file1_path, 'w', encoding='utf-8'), separators=(',', ':'),sort_keys=True, indent=4)

file2_path = "Targets.json"
print('Saving the target classes as ' + file2_path)
target = target # nested lists with same data, indices
json.dump(target, codecs.open(file2_path, 'w', encoding='utf-8'), separators=(',', ':'),sort_keys=True, indent=4)
print('Database creation completed.')

import os
from ActivityRecognition.project.project1 import *
os.getcwd()
f=open('newfile.txt','w+',1)
count=1
# for i in range(7):
#     for j in range(4):
#         f.write(str(count)+' ')
#         count+=1
#     f.write('\n')
# print (imggray[0][0])
lis=np.zeros((256,256))
print (len(imggray))
# lis=imggray

f.writelines(str(imggray))
f.seek(0)
lar=f.readlines()
print (len(lar))
print (lar[100][100])
# print (len(lis))
# for i in range(189):
#     for j in range(189):
#         f.write(str(imggray[i][j])+' ')
#     f.write('\n')
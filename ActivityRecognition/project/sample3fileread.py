import numpy as np
f=open('G:\\workspace\\pythonpgm\\ActivityRecognition\\sevDB\\sitting\\input_data10.txt','r',1)
list1=f.readlines()
listx=[]
listy=[]
listz=[]
listpart1=[]
listpart2=[]
listpart3=[]
listpart4=[]
listpart5=[]
listpart6=[]
nr=0
# print (list1)
# print(len(list1))
n=len(list1)
xyz=np.zeros((n,3))
# choi=int(input('enter axis(1,2,3)'))
for i in range(1,n-1,1):
        s=list1[i].split(',')
        # if choi==1:
        listx.append(float(s[0]))
        # elif choi==2:
        listy.append(float(s[1]))
        # elif choi==3:
        listz.append(float(s[2]))
no=(len(listx))
# print(no)
parts5=no/5
# if type(parts5)==float:
#         ra=6
# else:
#         ra=5
parts5=int(parts5)
# print(parts5)
for i in range(5):
        # print('part',i+1,":\n\n")
        initial=nr
        if i==4:
                bb=no-nr
                nr+=bb
                # print(nr)
        else:
                nr=nr+parts5
        for j in range(initial,nr,1):
                # print(listx[j],",",listy[j],",",listz[j])

                str1=str(listx[j])+','+str(listy[j])+","+str(listz[j])
                if i==0:
                        listpart1.append(str1)
                if i==1:
                        listpart2.append(str1)
                if i==2:
                        listpart3.append(str1)
                if i==3:
                        listpart4.append(str1)
                if i==4:
                        listpart5.append(str1)
                # if i==5:
                #         listpart6.append(str1)
# for i in range(len(listpart1)):
#         print(listpart1[i])

def mini():
        listpart1.sort()
        print(listpart1)



def minimum():
        minx = []
        miny = []
        minz = []
        minimumx = 0.0
        minimumy = 0.0
        minimumz = 0.0
        minv = listpart1[0].split(',')
        # print(type(minv[0]))
        minv[0]=float(minv[0])
        minv[1]=float(minv[1])
        minv[2]=float(minv[2])
        for i in listpart1:
                zz=i.split(',')
                zz[0]=float(zz[0])
                zz[1]=float(zz[1])
                zz[2]=float(zz[2])
                if zz[0]<minv[0]:
                        minimumx=zz[0]
                        minv[0]=zz[0]

                if zz[1]<minv[1]:
                        minimumy=zz[1]
                        minv[1]=zz[1]
                if zz[2]<minv[2]:
                        minimumz=zz[2]
                        minv[2]=zz[2]
        minx.append(minimumx)
        miny.append(minimumy)
        minz.append(minimumz)

        minv = listpart2[0].split(',')
        # print(type(minv[0]))
        minv[0] = float(minv[0])
        minv[1] = float(minv[1])
        minv[2] = float(minv[2])

        for i in listpart2:
                zz2=i.split(',')
                zz2[0] = float(zz2[0])
                zz2[1] = float(zz2[1])
                zz2[2] = float(zz2[2])
                if zz2[0]<minv[0]:
                        minimumx=zz2[0]
                        minv[0]=zz2[0]

                if zz2[1]<minv[1]:
                        minimumy=zz2[1]
                        minv[1]=zz2[1]
                if zz2[2]<minv[2]:
                        minimumz=zz2[2]
                        minv[2]=zz2[2]
        minx.append(minimumx)
        miny.append(minimumy)
        minz.append(minimumz)

        minv = listpart3[0].split(',')
        # print(type(minv[0]))
        minv[0] = float(minv[0])
        minv[1] = float(minv[1])
        minv[2] = float(minv[2])

        for i in listpart3:
                zz2 = i.split(',')
                zz2[0] = float(zz2[0])
                zz2[1] = float(zz2[1])
                zz2[2] = float(zz2[2])
                if zz2[0] < minv[0]:
                        minimumx = zz2[0]
                        minv[0] = zz2[0]

                if zz2[1] < minv[1]:
                        minimumy = zz2[1]
                        minv[1] = zz2[1]
                if zz2[2] < minv[2]:
                        minimumz = zz2[2]
                        minv[2] = zz2[2]
        minx.append(minimumx)
        miny.append(minimumy)
        minz.append(minimumz)

        minv = listpart4[0].split(',')
        # print(type(minv[0]))
        minv[0] = float(minv[0])
        minv[1] = float(minv[1])
        minv[2] = float(minv[2])

        for i in listpart4:
                zz2 = i.split(',')
                zz2[0] = float(zz2[0])
                zz2[1] = float(zz2[1])
                zz2[2] = float(zz2[2])
                if zz2[0] < minv[0]:
                        minimumx = zz2[0]
                        minv[0] = zz2[0]

                if zz2[1] < minv[1]:
                        minimumy = zz2[1]
                        minv[1] = zz2[1]
                if zz2[2] < minv[2]:
                        minimumz = zz2[2]
                        minv[2] = zz2[2]
        minx.append(minimumx)
        miny.append(minimumy)
        minz.append(minimumz)

        minv = listpart5[0].split(',')
        # print(type(minv[0]))
        minv[0] = float(minv[0])
        minv[1] = float(minv[1])
        minv[2] = float(minv[2])

        for i in listpart5:
                zz2 = i.split(',')
                zz2[0] = float(zz2[0])
                zz2[1] = float(zz2[1])
                zz2[2] = float(zz2[2])
                if zz2[0] < minv[0]:
                        minimumx = zz2[0]
                        minv[0] = zz2[0]

                if zz2[1] < minv[1]:
                        minimumy = zz2[1]
                        minv[1] = zz2[1]
                if zz2[2] < minv[2]:
                        minimumz = zz2[2]
                        minv[2] = zz2[2]
        minx.append(minimumx)
        miny.append(minimumy)
        minz.append(minimumz)

        print(minx)
        print(miny)
        print(minz)

def maximum():
        maxx = []
        maxy = []
        maxz = []
        maximumx = 0.0
        maximumy = 0.0
        maximumz = 0.0
        minv = listpart1[0].split(',')
        # print(type(minv[0]))
        minv[0] = float(minv[0])
        minv[1] = float(minv[1])
        minv[2] = float(minv[2])
        for i in listpart1:
                zz = i.split(',')
                zz[0] = float(zz[0])
                zz[1] = float(zz[1])
                zz[2] = float(zz[2])
                if zz[0] > minv[0]:
                        maximumx = zz[0]
                        minv[0] = zz[0]

                if zz[1] > minv[1]:
                        maximumy = zz[1]
                        minv[1] = zz[1]
                if zz[2] > minv[2]:
                        maximumz = zz[2]
                        minv[2] = zz[2]
        maxx.append(maximumx)
        maxy.append(maximumy)
        maxz.append(maximumz)

        minv = listpart2[0].split(',')
        # print(type(minv[0]))
        minv[0] = float(minv[0])
        minv[1] = float(minv[1])
        minv[2] = float(minv[2])
        for i in listpart2:
                zz = i.split(',')
                zz[0] = float(zz[0])
                zz[1] = float(zz[1])
                zz[2] = float(zz[2])
                if zz[0] > minv[0]:
                        maximumx = zz[0]
                        minv[0] = zz[0]

                if zz[1] > minv[1]:
                        maximumy = zz[1]
                        minv[1] = zz[1]
                if zz[2] > minv[2]:
                        maximumz = zz[2]
                        minv[2] = zz[2]
        maxx.append(maximumx)
        maxy.append(maximumy)
        maxz.append(maximumz)

        minv = listpart3[0].split(',')
        # print(type(minv[0]))
        minv[0] = float(minv[0])
        minv[1] = float(minv[1])
        minv[2] = float(minv[2])
        for i in listpart3:
                zz = i.split(',')
                zz[0] = float(zz[0])
                zz[1] = float(zz[1])
                zz[2] = float(zz[2])
                if zz[0] > minv[0]:
                        maximumx = zz[0]
                        minv[0] = zz[0]

                if zz[1] > minv[1]:
                        maximumy = zz[1]
                        minv[1] = zz[1]
                if zz[2] > minv[2]:
                        maximumz = zz[2]
                        minv[2] = zz[2]
        maxx.append(maximumx)
        maxy.append(maximumy)
        maxz.append(maximumz)

        minv = listpart4[0].split(',')
        # print(type(minv[0]))
        minv[0] = float(minv[0])
        minv[1] = float(minv[1])
        minv[2] = float(minv[2])
        for i in listpart4:
                zz = i.split(',')
                zz[0] = float(zz[0])
                zz[1] = float(zz[1])
                zz[2] = float(zz[2])
                if zz[0] > minv[0]:
                        maximumx = zz[0]
                        minv[0] = zz[0]

                if zz[1] > minv[1]:
                        maximumy = zz[1]
                        minv[1] = zz[1]
                if zz[2] > minv[2]:
                        maximumz = zz[2]
                        minv[2] = zz[2]
        maxx.append(maximumx)
        maxy.append(maximumy)
        maxz.append(maximumz)

        minv = listpart5[0].split(',')
        # print(type(minv[0]))
        minv[0] = float(minv[0])
        minv[1] = float(minv[1])
        minv[2] = float(minv[2])
        for i in listpart5:
                zz = i.split(',')
                zz[0] = float(zz[0])
                zz[1] = float(zz[1])
                zz[2] = float(zz[2])
                if zz[0] > minv[0]:
                        maximumx = zz[0]
                        minv[0] = zz[0]

                if zz[1] > minv[1]:
                        maximumy = zz[1]
                        minv[1] = zz[1]
                if zz[2] > minv[2]:
                        maximumz = zz[2]
                        minv[2] = zz[2]

        maxx.append(maximumx)
        maxy.append(maximumy)
        maxz.append(maximumz)

        print(maxx)
        print(maxy)
        print(maxz)

def mean():
        meanxsum=0.0
        meanysum=0.0
        meanzsum=0.0
        meanx=[]
        meany=[]
        meanz=[]
        for i in listpart1:
                ss=i.split(',')
                ss[0]=float(ss[0])
                ss[1]=float(ss[1])
                ss[2]=float(ss[2])
                meanxsum+=ss[0]
                meanysum+=ss[1]
                meanzsum+=ss[2]
        meanx.append(meanxsum/len(listpart1))
        meany.append(meanysum/len(listpart1))
        meanz.append(meanzsum/len(listpart1))

        meanxsum = 0.0
        meanysum = 0.0
        meanzsum = 0.0
        for i in listpart2:
                ss = i.split(',')
                ss[0] = float(ss[0])
                ss[1] = float(ss[1])
                ss[2] = float(ss[2])
                meanxsum += ss[0]
                meanysum += ss[1]
                meanzsum += ss[2]
        meanx.append(meanxsum / len(listpart1))
        meany.append(meanysum / len(listpart1))
        meanz.append(meanzsum / len(listpart1))

        meanxsum = 0.0
        meanysum = 0.0
        meanzsum = 0.0
        for i in listpart3:
                ss = i.split(',')
                ss[0] = float(ss[0])
                ss[1] = float(ss[1])
                ss[2] = float(ss[2])
                meanxsum += ss[0]
                meanysum += ss[1]
                meanzsum += ss[2]
        meanx.append(meanxsum / len(listpart1))
        meany.append(meanysum / len(listpart1))
        meanz.append(meanzsum / len(listpart1))

        meanxsum = 0.0
        meanysum = 0.0
        meanzsum = 0.0
        for i in listpart4:
                ss = i.split(',')
                ss[0] = float(ss[0])
                ss[1] = float(ss[1])
                ss[2] = float(ss[2])
                meanxsum += ss[0]
                meanysum += ss[1]
                meanzsum += ss[2]
        meanx.append(meanxsum / len(listpart1))
        meany.append(meanysum / len(listpart1))
        meanz.append(meanzsum / len(listpart1))

        meanxsum = 0.0
        meanysum = 0.0
        meanzsum = 0.0
        for i in listpart5:
                ss = i.split(',')
                ss[0] = float(ss[0])
                ss[1] = float(ss[1])
                ss[2] = float(ss[2])
                meanxsum += ss[0]
                meanysum += ss[1]
                meanzsum += ss[2]
        meanx.append(meanxsum / len(listpart1))
        meany.append(meanysum / len(listpart1))
        meanz.append(meanzsum / len(listpart1))


        print(meanx)
        print(meany)
        print(meanz)

print("minimum is:")
minimum()
print("maximum is:")
maximum()
print('mean:')
mean()
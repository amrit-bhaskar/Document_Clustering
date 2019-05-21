from sklearn.cluster import KMeans
import numpy as np
np.set_printoptions(threshold='nan')
w2v={}
count=0

flag=1
d2v={}
temp=''
with open("res_10.txt", 'r') as f:
    for line in f:
        if flag == 0:
          sen = line.rstrip().split(' ')
          w2v[count] = [float(x) for x in sen[0:]]
          d2v[count] = temp
          count = count + 1
          flag=1
        else:
           temp=line.split("\n")[0]
           flag=0
#for k,v in w2v.iteritems():
#   print v
X=np.array(w2v[0],dtype="float")
#print x
for itr in range(1,len(w2v)):
  X = np.vstack([X,w2v[itr]])

#print(X.shape)
'''
l1=[]
l2=[]
l3=[]
l4=[]
'''
output={}

kmeans = KMeans(n_clusters=4, random_state=0).fit(X)

centroids = kmeans.cluster_centers_

#print (kmeans.labels_.shape)
#print(type(kmeans.labels_))
#print kmeans.labels_

itr=0
for x in np.nditer(kmeans.labels_):
    x = int(x)
    if x in output:
         output[x].append(d2v[itr])
    else:
         output[x]=[d2v[itr]]
    itr+=1
print itr
'''
itr=0
for x in np.nditer(kmeans.labels_):
    if x == 0:
        l1.append(d2v[itr])
    elif x == 1:
        l2.append(d2v[itr])
    elif x == 2:
        l3.append(d2v[itr])
    elif x == 3:
        l4.append(d2v[itr])
    itr+=1

#labels = kmeans.labels_
print len(l1),len(l2),len(l3),len(l4)
#print(centroids)
#print(labels)
#print(len(w2v))
#print(len(d2v))
print l1
print "\n"
print l2
print "\n"
print l3
print "\n"
print l4
'''

#print(len(output[0]),len(output[1]),len(output[2]),len(output[3]))
for k,v in output.iteritems():
    t_d={}
    print(len(output[k]))
    print(v)
    for i in range(len(v)):
        v[i]=v[i].split("/")[1]
        if v[i] in t_d:
            t_d[v[i]]+=1
        else:
            t_d[v[i]]=1
    for ki,vi in t_d.iteritems():
        print ki,vi

    print "\n"
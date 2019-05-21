#f1=open("test.txt","r")
import re
import collections
d={}
from operator import add

def unique(list1):
 
    # intilize a null list
    unique_list = []
     
    # traverse for all elements
    for x in list1:
        # check if exists in unique_list or not
        if x not in unique_list:
            unique_list.append(x)
    return unique_list
w2v={}
with open("glove.840B.300d.txt", 'r') as f3:
        for line in f3:
                sen = line.rstrip().split(' ')
                w2v[sen[0]] = [float(x) for x in sen[1:]]

with open("wikipedia_stanford_sense_cluster",'r') as f2:
      for line in f2:
            vals = line.rstrip().split('\t')
            #vals[2]=vals[2].split(" ,")
            vals[0] = vals[0].split('#')[0]
            if vals[0] in d:
                #d[vals[0]].append([str(x) for x in vals[1:]])
                #d[vals[0]].append((vals[2]))
                vals[2]=vals[2].split(",")
                for i in range(len(vals[2])):
                        #d[vals[0]].append((vals[2][i]))
                        vals[2][i]=vals[2][i].split('#')[0]
                        d[vals[0]]+=' '
                        d[vals[0]]+=vals[2][i].strip()
            else: 
                #d[vals[0]]=[str(x) for x in vals[1:]]
                #d[vals[0]]=[(vals[2])]
                vals[2] = ''.join(str(e) for e in vals[2])
                #print(vals[2])
                vals[2]=re.split(',',vals[2])
                #print("hi",len(vals[2]))
                vals[2][0]=vals[2][0].split('#')[0]
                d[vals[0]]=vals[2][0]
                for i in range(1,len(vals[2])):
                        vals[2][i]=vals[2][i].split('#')[0]
                        d[vals[0]]+=' '
                        d[vals[0]]+=vals[2][i].strip()
#print(d)
'''
for k,v in d.iteritems():
    #print(k,v)
    v=v.split(" ")
    counts = collections.Counter(v)
    v = sorted(v, key=counts.get, reverse=True)
    v=unique(v)
    v=v[:10]
    print(k,v)
    #print(type(v))
'''
l1=[0]*300
flag=0
with open("result_1.txt", 'r') as f:
    for line in f:
      if(len(line.split())==2):
        x=line.split()[0]
        y=line.split()[1]
        #print x,y
        #l2=[0]*300
        if y in d or y.capitalize() in d or y.upper() in d:
            if y.capitalize() in d:
                y=y.capitalize()
            if y.upper() in d:
                y=y.upper()
            temp=d[y].split(" ")
            counts = collections.Counter(temp)
            temp = sorted(temp, key=counts.get, reverse=True)
            temp=unique(temp)
            #print(temp)
            count=0
            #print("Hi")
            #print(len(d[y]))
            for itr in range(len(temp)):
                if(count==10):
                    break
                #print d[y][itr]
                if temp[itr] in w2v:
                    count+=1
                    #print temp[itr],type(w2v[temp[itr]])
                    l1=map(add,w2v[temp[itr]],l1)

                    
      else:
          if flag==1:
             #print(l1)
             s1=" ".join(str(x) for x in l1)
             print s1
          flag=1
          l1=[0]*300
          print line,
          #l2=map(add,w2v[temp[itr]],l2)
#print l1
s1=" ".join(str(x) for x in l1)
print s1



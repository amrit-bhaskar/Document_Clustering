import nltk
import string
import os

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
f1=open("result_1.txt","w")

from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.stem.porter import PorterStemmer

from nltk.stem.wordnet import WordNetLemmatizer

def kthmax(k, list):
        if (k == 1):
            return max(list)
        else:
            m = max(list)
            return(kthmax(k-1, [x for x in list if x != m]))

nltk.download('wordnet')


#path = '/opt/datacourse/data/parts'
token_dict = {}
stemmer = PorterStemmer()

lemma= WordNetLemmatizer()

def stem_tokens(tokens, stemmer):
    stemmed = []
    for item in tokens:
        #stemmed.append(stemmer.stem(item))
        stemmed.append(lemma.lemmatize(item))
    return stemmed

def tokenize(text):
    w=''
    tokens = nltk.word_tokenize(text)
    stems = stem_tokens(tokens, stemmer)
    result=nltk.pos_tag(stems)
    #print(type(result))
    #print(result)
    #for i in result:
    #    if i[1]=='NN' or i[1]=='NNP' or i[1]=='NNPS' or i[1]=='NNS':
    #        w += i[0]
    #        w += ' '
    #stems = stem_tokens(w, stemmer)
    return stems

for subdir, dirs, files in os.walk("bbc/"):
  for r,d,f in os.walk(subdir):  
    for file in f:
        file_path = r + os.path.sep + file
        #print(file_path)
        shakes = open(file_path, 'r')
        text = shakes.read()
        lowers = text
        no_punctuation = lowers.translate(None, string.punctuation)
        token_dict[file_path] = no_punctuation

from collections import OrderedDict
dicti=OrderedDict(token_dict)
index={}
count=0
#print("              **************************************                                                  ")
for k,v in dicti.iteritems():
        index[count]=k
        count=count+1


#this can take some time
tfidf = TfidfVectorizer(tokenizer=tokenize, stop_words='english')

print(tfidf)
tfs = tfidf.fit_transform(dicti.values())


#print(tfidf)
#print type(tfs)
#y=tfs[0,:].toarray()
'''
print(type(y))
print float(y[0][0])
print("%f" %(y[0][23]))
x=tfidf.get_feature_names()
print(type(x))
print(len(x))
'''
x=tfidf.get_feature_names()
#print("length",len(x))
#print(x)
#print(tfs)


#print(tfs.shape[1])
#print("Hi")
#print(tfs[0].shape)
#print(tfs[0,3])



x=tfidf.get_feature_names()
#print(type(x))
#print(len(x))


#print(x)
#print(x[3])
#for i in range(tfs.shape[1]):
#    print(tfs[0,i])
#    print(i)
#print(tfs.shape)


#print(tfs[4])
#for itr in range(tfs.shape[1]):
#    print tfs[4,itr],

def is_ascii(s):
            return all(ord(c) < 128 for c in s)



for j in range(tfs.shape[0]):
  lil=[]
  f1.write(index[j])
  f1.write("\n")
  for i in range(tfs.shape[1]):
     lil.append(tfs[j,i])
  #print(len(lil))
  #print(type(lil))
  #print(lil)
  rank=kthmax(30,lil)
  #print(rank)
  #print(type(tfs[0]))
  for i in range(tfs[j].shape[1]):
     if tfs[j,i]>=rank:
         if (is_ascii(x[i]))==True:
           f1.write("%s" %tfs[j,i])
           f1.write("  ")
           f1.write("%s" %x[i].encode('utf-8'))
           f1.write("\n")


f1.close()





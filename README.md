A sense cluster file("wikipedia_stanford_sense_cluster") is required for prog.py.Refer this:
http://ltmaggie.informatik.uni-hamburg.de/jobimtext/documentation/sense-clustering/



# Document_Clustering
Clustering files with respect to similarity between them

## 1st code - tfidf1.py : 
Collect top 30 words from each document based on tf-idf score.

            input: All text documents.(bbc documents)
            output: result_1.txt

## 2nd Code - prog.py :  
Search for the words collected from result_1.txt in the sense_cluster file from wikipedia to get the cluster terms.
After getting the cluster terms, search for the cluster terms in the glove file to get the vector of each term.
Add all the vectors of each term and add all the vectors of top 30 words together for a document.
Now you have got a vector for each document.

                      input : result_1.txt
                      output : res_10.txt

## 3rd Code - prog_clus.py :
Apply K-Means clustering algorithm.
Output is the clusters.

                      input : res_10.txt
                      output : res_12.txt




![graph_dc](https://user-images.githubusercontent.com/31445774/58119016-af656900-7c1f-11e9-85ae-382d5dd7c8af.png)

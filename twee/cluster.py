import json
import random
import math
import json
import re


#Euclidian Distance between two d-dimensional points
def eucldist(p0,p1):
    dist = 0.0
    for i in range(0,len(p0)):
        dist += (p0[i] - p1[i])**2
    return math.sqrt(dist)


    
#K-Means Algorithm
def kmeans(k,datapoints):

    # d - Dimensionality of Datapoints
    d = len(datapoints[0]) 
    
    #Limit our iterations
    Max_Iterations = 1000
    i = 0
    
    cluster = [0] * len(datapoints)
    prev_cluster = [-1] * len(datapoints)
    
    #Randomly Choose Centers for the Clusters
    cluster_centers = []
    for i in range(0,k):
        new_cluster = []
        #for i in range(0,d):
        #    new_cluster += [random.randint(0,10)]
        cluster_centers += [random.choice(datapoints)]
        
        
        #Sometimes The Random points are chosen poorly and so there ends up being empty clusters
        #In this particular implementation we want to force K exact clusters.
        #To take this feature off, simply take away "force_recalculation" from the while conditional.
        force_recalculation = False
    
    while (cluster != prev_cluster) or (i > Max_Iterations) or (force_recalculation) :
        
        prev_cluster = list(cluster)
        force_recalculation = False
        i += 1
    
        #Update Point's Cluster Alligiance
        for p in range(0,len(datapoints)):
            min_dist = float("inf")
            
            #Check min_distance against all centers
            for c in range(0,len(cluster_centers)):
                
                dist = eucldist(datapoints[p],cluster_centers[c])
                
                if (dist < min_dist):
                    min_dist = dist  
                    cluster[p] = c   # Reassign Point to new Cluster
        
        
        #Update Cluster's Position
        for k in range(0,len(cluster_centers)):
            new_center = [0] * d
            members = 0
            for p in range(0,len(datapoints)):
                if (cluster[p] == k): #If this point belongs to the cluster
                    for j in range(0,d):
                        new_center[j] += datapoints[p][j]
                    members += 1
            
            for j in range(0,d):
                if members != 0:
                    new_center[j] = new_center[j] / float(members) 
                
                #This means that our initial random assignment was poorly chosen
                #Change it to a new datapoint to actually force k clusters
                else: 
                    new_center = random.choice(datapoints)
                    force_recalculation = True
                    print ("Forced Recalculation...")
                    
            
            cluster_centers[k] = new_center
    
        
    #print ("======== Results ========")
    #print ("Clusters", cluster_centers)
    #print ("Iterations",i)
    #print ("Assignments", cluster)

    
    segments=[]
    for i in cluster_centers:
    	segments.append(dum.get(int(i[0])))
    return segments
    
    
#TESTING THE PROGRAM#
if __name__ == "__main__":
    #2D - Datapoints List of n d-dimensional vectors. (For this example I already set up 2D Tuples)
    #Feel free to change to whatever size tuples you want...
    dir='data/weight_'
    f=open(dir,'r')
    x=[]
    y=[]
    datapoints=[]
    for i in f:
    	dic=eval(i)
    dummies={}
    dum={}
    j=0
    for i in dic:
    	if dummies.get(i)==None:
    		dummies[i]=j
    		y.append(dic[i])
    		dum[j]=i
    		j+=1
    for i in dummies:
    	x.append(dummies[i])
    for i in range(len(x)):
    	datapoints.append((x[i],y[i]))
    	





    k = 4 # K - Number of Clusters
    
    segment=[]
    segment.extend(kmeans(k,datapoints))
    print(segment)
    f=open('data/10_hour.json','r')

    events=[]

    for line in f:
        line = line.replace('\n','')
        if line=='':
            break
        json_tweet=json.loads(line)

        for i in segment:
            if i in json_tweet['text'] or i in  json_tweet['entities']['user_mentions']:
                events.append( [ [json_tweet['created_at']],[ json_tweet['text']] ] )

    f1=open('result/events.txt','w')

    f1.write('The Events happening now are')
    f1.write('\n')
    print(events)
    for i in events:
        f1.write(str(i[0]))
        f1.write(' - ')
        f1.write(str(i[1]))
        f1.write('\n')
        f1.write('---------------------------------------------------------------------------------------------------------------------------------------')
        f1.write('\n')









    

    




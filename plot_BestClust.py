import pandas as pd
import os
import re
import sys
import matplotlib.pyplot as plt
#import seaborn as sns
#get the current directory

max_hyp = 100 # the maximum hyperparameter
curr_clust = 2 #the current cluster
box = []

#store the stats of the cluster
cluster_stats = dict(
            Cluster_number=[],DBI=[],pSF=[],R2=[] )

#main loop
while curr_clust <= max_hyp: 
    cwd = os.getcwd()
    #change direcetory to cluster file
    os.chdir(os.path.join(cwd,'cluster_%i' % curr_clust))
    
    #extract cluster's info stats info and input it into dict
    with open('cluster_%i.txt' % curr_clust, 'r' ) as fh:
        re_DBI = re.compile(r'#DBI:\s*(-?\d*\.\d*)')
        re_psF = re.compile(r'#pSF:\s*(-?\d*\.\d*)')
        re_R2 = re.compile(r'#SSR/SST:\s*(-?\d*\.\d*)')
        re_inf = re.compile(r'#DBI:\s*(inf)')

        for line in fh:
            if 'inf' in line:
                #replace the inf of DBI with 5
                cluster_stats['DBI'].extend(list('5'))
                cluster_stats['pSF'].extend(list(re_psF.findall(line)))
                cluster_stats['R2'].extend(list(re_R2.findall(line)))
                #otherwise, add the current number 
            else:
            	#cluster_stats['Cluster_number'].append(curr_clust)
            	cluster_stats['DBI'].extend(list(re_DBI.findall(line)))
            	cluster_stats['pSF'].extend(list(re_psF.findall(line)))
            	cluster_stats['R2'].extend(list(re_R2.findall(line)))
            
    cluster_stats['Cluster_number'].append(curr_clust)
    curr_clust+=1
    os.chdir(cwd)
    #print(cluster_stats)
    print(cluster_stats)
    df=pd.DataFrame(cluster_stats)
#df 
#convert to numeric
df['DBI'] = pd.to_numeric(df['DBI'], downcast="float")
df['pSF'] = pd.to_numeric(df['pSF'], downcast="float")
df['R2'] = pd.to_numeric(df['R2'], downcast="float")

#take into account, that clustering starts at 2, and indexing starts at 0
for i in range(0, max_hyp-2):
    curr = df['R2'].iloc[i+1]
    previ = df['R2'].iloc[i]
    #the minimum difference between 
    cutoff = 0.02
        
    if curr - previ <= cutoff and len(box)==2:
        box.append(i)
        #print(box)
        #find the lowest DBI score within a plateauing SSR/SST value
        minimum = df['DBI'].iloc[box[0]:].min() 
        #print(box[0])
        break
        #print (minimum)
        #print(box)
            
    elif curr - previ <= cutoff and len(box)<2:
        box.append(i)
        print(box)
    
    elif df['DBI'].iloc[i] == 'inf':
        minimum = df['DBI'].iloc[box[0]:i].min() 
        print(box[0])
        break
    else:
         #makes sure all numbers are consecutive
         box.clear()
         continue
            
choosen_cluster = float(df[df['DBI']==minimum].Cluster_number.values)
final_R2 = float(df[df['DBI']==minimum].R2.values)
final_psF = float(df[df['DBI']==minimum].pSF.values)
    
with open('BestClusterStats.txt','w+') as bc:
    bc.write('Cluster number:%f, SSR/SST:%f, DBI:%f, psF:%f'  % (choosen_cluster, final_R2, minimum,final_psF))

#plt.savefig('Kmeans.png', bbox_inches='tight',dpi=300)
#returns the chosen cluster number and its associated DBI and R**2 values
#return choosen_cluster,final_R2, minimum,final_psF

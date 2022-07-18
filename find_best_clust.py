import pandas as pd
import os
import re
import matplotlib.pyplot as plt
#import seaborn as sns


#go through each directory and collect the DBI and SSR/SST values
#take the lowest one and state that as the best algorithm

#def FindBestClust():
R2_list = []

KMeans_dict = dict(Cluster_number=[],DBI=[],pSF=[],R2=[])
HierAvgLink_dict = dict(Cluster_number=[],DBI=[],pSF=[],R2=[])
HierComplLink_dict = dict(Cluster_number=[],DBI=[],pSF=[],R2=[])
HierlLink_dict = dict(Cluster_number=[],DBI=[],pSF=[],R2=[])
DBSCAN_dict = dict(Cluster_number=[],DBI=[],pSF=[],R2=[])

cwd = os.getcwd()
#change direcetory to each algorithm's file
algorithms = ['KMeans','HierAvgLink','HierComplLink','HierLink','DBSCAN']
#algorithms = (KMeans,'HierAvgLink','HierComplLink','HierLink','DBSCAN')
for s in algorithms:
    os.chdir(os.path.join(cwd,'%s' % s))
    with open('BestClusterStats.txt','r') as f:
        re_ClustNum = re.compile(r'Cluster number:(-?\d*\.\d*)')
        re_DBI = re.compile(r'DBI:(-?\d*\.\d*)')
        re_psF = re.compile(r'psF:(-?\d*\.\d*)')
        re_R2 = re.compile(r'SSR/SST:(-?\d*\.\d*)')
        
        
        for line in f:
           # print(line)
           # s['Cluster_number'].extend(int(re.finditer(re_ClustNum, line)))
           # #s['Cluster_number'].extend(list(re_ClustNum.findall(line)))
           # s['DBI'].extend(list(re_DBI.findall(line)))
           # s['pSF'].extend(list(re_psF.findall(line)))
           # s['R2'].extend(list(re_R2.findall(line)))
           # 
           # #add all the SSR/SST to the R2 list
           # R2_list.extend(list(re_R2.findall(line)))
            
            #convert to numeric
            if s == 'KMeans':
                KMeans_dict['Cluster_number'].extend(list(re_ClustNum.findall(line)))
                KMeans_dict['DBI'].extend(list(re_DBI.findall(line)))
                KMeans_dict['pSF'].extend(list(re_psF.findall(line)))
                KMeans_dict['R2'].extend(list(re_R2.findall(line)))
               # print(KMeans_dict['Cluster_number'],KMeans_dict['DBI'],KMeans_dict['pSF'],KMeans_dict['R2'])
            
                #add all the SSR/SST to the R2 list
                R2_list.extend(list(re_R2.findall(line)))
                
                #convert to numeric 
                KMeans_df=pd.DataFrame(KMeans_dict)
                KMeans_df['Cluster_number'] = pd.to_numeric(KMeans_df['Cluster_number'], downcast="float")
                KMeans_df['DBI'] = pd.to_numeric(KMeans_df['DBI'], downcast="float")
                KMeans_df['pSF'] = pd.to_numeric(KMeans_df['pSF'], downcast="float")
                KMeans_df['R2'] = pd.to_numeric(KMeans_df['R2'], downcast="float")
                
            elif s == 'HierAvgLink':
                HierAvgLink_dict['Cluster_number'].extend(list(re_ClustNum.findall(line)))
                HierAvgLink_dict['DBI'].extend(list(re_DBI.findall(line)))
                HierAvgLink_dict['pSF'].extend(list(re_psF.findall(line)))
                HierAvgLink_dict['R2'].extend(list(re_R2.findall(line)))
             
                #add all the SSR/SST to the R2 list
                R2_list.extend(list(re_R2.findall(line)))
            
                HierAvgLink_df=pd.DataFrame(HierAvgLink_dict)
                HierAvgLink_df['Cluster_number'] = pd.to_numeric(HierAvgLink_dict['Cluster_number'], downcast="float")
                HierAvgLink_df['DBI'] = pd.to_numeric(HierAvgLink_dict['DBI'], downcast="float")
                HierAvgLink_df['pSF'] = pd.to_numeric(HierAvgLink_dict['pSF'], downcast="float")
                HierAvgLink_df['R2'] = pd.to_numeric(HierAvgLink_dict['R2'], downcast="float")
                
            elif s == 'HierComplLink':
                
                HierComplLink_dict['Cluster_number'].extend(list(re_ClustNum.findall(line)))
                HierComplLink_dict['DBI'].extend(list(re_DBI.findall(line)))
                HierComplLink_dict['pSF'].extend(list(re_psF.findall(line)))
                HierComplLink_dict['R2'].extend(list(re_R2.findall(line)))
             
                #add all the SSR/SST to the R2 list
                R2_list.extend(list(re_R2.findall(line)))
                
                HierComplLink_df=pd.DataFrame(HierComplLink_dict)
                HierComplLink_df['Cluster_number'] = pd.to_numeric(HierComplLink_dict['Cluster_number'], downcast="float")
                HierComplLink_df['DBI'] = pd.to_numeric(HierComplLink_dict['DBI'], downcast="float")
                HierComplLink_df['pSF'] = pd.to_numeric(HierComplLink_dict['pSF'], downcast="float")
                HierComplLink_df['R2'] = pd.to_numeric(HierComplLink_dict['R2'], downcast="float")
                
            elif s == 'HierLink':
                
                HierlLink_dict['Cluster_number'].extend(list(re_ClustNum.findall(line)))
                HierlLink_dict['DBI'].extend(list(re_DBI.findall(line)))
                HierlLink_dict['pSF'].extend(list(re_psF.findall(line)))
                HierlLink_dict['R2'].extend(list(re_R2.findall(line)))
             
                #add all the SSR/SST to the R2 list
                R2_list.extend(list(re_R2.findall(line)))
                
                HierLink_df=pd.DataFrame(HierlLink_dict)
                HierLink_df['Cluster_number'] = pd.to_numeric(HierlLink_dict['Cluster_number'], downcast="float")
                HierLink_df['DBI'] = pd.to_numeric(HierlLink_dict['DBI'], downcast="float")
                HierLink_df['pSF'] = pd.to_numeric(HierlLink_dict['pSF'], downcast="float")
                HierLink_df['R2'] = pd.to_numeric(HierlLink_dict['R2'], downcast="float")
            elif s == 'DBSCAN':
                
                DBSCAN_dict['Cluster_number'].extend(list(re_ClustNum.findall(line)))
                DBSCAN_dict['DBI'].extend(list(re_DBI.findall(line)))
                DBSCAN_dict['pSF'].extend(list(re_psF.findall(line)))
                DBSCAN_dict['R2'].extend(list(re_R2.findall(line)))
             
                #add all the SSR/SST to the R2 list
                R2_list.extend(list(re_R2.findall(line)))
                
                DBSCAN_df=pd.DataFrame(DBSCAN_dict)
                DBSCAN_df['Cluster_number'] = pd.to_numeric(DBSCAN_dict['Cluster_number'], downcast="float")
                DBSCAN_df['DBI'] = pd.to_numeric(DBSCAN_dict['DBI'], downcast="float")
                DBSCAN_df['pSF'] = pd.to_numeric(DBSCAN_dict['pSF'], downcast="float")
                DBSCAN_df['R2'] = pd.to_numeric(DBSCAN_dict['R2'], downcast="float")
                
#comparing the stats from each algorithm; choose the one with the lowest R**2 value 
#get the max R2 value and append the best cluster to the file

print(R2_list)
max_R2 = max(R2_list)
for num, i in enumerate(R2_list):
    if max_R2 == i:
        indexofBestAlgo = num
        best_algo = algorithms[num]
        print(best_algo)
        os.chdir(os.path.join(cwd))
        with open('BestCluster.txt','w') as fh:
            fh.write('BestClust is: %s' % best_algo)
        break
    else:
        continue
    #print(df[df['R2']==max_R2].pSF.values)

import pandas as pd
import os
import re
import sys
import matplotlib.pyplot as plt
#import seaborn as sns
#get the current directory

curr_clust = 2 #the current cluster

#store the stats of the cluster
cluster_stats = dict(
            Cluster_number=[],DBI=[],pSF=[],R2=[] )

#main loop

cwd = os.getcwd()
#change direcetory to cluster file
os.chdir(os.path.join(cwd,'cluster_2'))
    
#extract cluster's info stats info and input it into dict
with open('cluster_2.txt', 'r' ) as fh:
    re_DBI = re.compile(r'#DBI:\s*(-?\d*\.\d*)')
    re_psF = re.compile(r'#pSF:\s*(-?\d*\.\d*)')
    re_R2 = re.compile(r'#SSR/SST:\s*(-?\d*\.\d*)')
        
    for line in fh:
        #cluster_stats['Cluster_number'].append(curr_clust)
            cluster_stats['DBI'].extend(list(re_DBI.findall(line)))
            cluster_stats['pSF'].extend(list(re_psF.findall(line)))
            cluster_stats['R2'].extend(list(re_R2.findall(line)))
            
    cluster_stats['Cluster_number'].append(curr_clust)
    os.chdir(cwd)
    #print(cluster_stats)
    df=pd.DataFrame(cluster_stats)
#df 
#convert to numeric
df['DBI'] = pd.to_numeric(df['DBI'], downcast="float")
df['pSF'] = pd.to_numeric(df['pSF'], downcast="float")
df['R2'] = pd.to_numeric(df['R2'], downcast="float")


#Plotting parameters

#sns.set_theme(style="whitegrid")
#sns.set_theme(style="darkgrid")

ax = plt.gca() 
df.plot(kind='line',linestyle='dashed',marker='o',x= 'Cluster_number',y= 'DBI' ,color = 'blue', ax = ax)
df.plot(kind='line',marker='o',x= 'Cluster_number',y='R2' ,color = 'green', ax = ax)
plt.xlabel('Cluster size')
plt.ylabel('DBI & pSF values')
plt.legend(title='Legend', title_fontsize = 10, labels=['DBI', 'R2'])
tight_layout=True
ax.grid(False)

#saving the figure
plt.savefig('DBSCAN.png', bbox_inches='tight',dpi=300)


choosen_cluster = 2.000000
final_R2 = float(df['R2']) 
minimum = float(df['DBI'])
final_psF = float(df['pSF'])


with open('BestClusterStats.txt','w+') as bc:
    bc.write('Cluster number:%f, SSR/SST:%f, DBI:%f, psF:%f'  % (choosen_cluster, final_R2, minimum,final_psF))


# Amber-ML-Tool
Unsupervised Machine Learning Tool Using AMBER 

What the program/tool does:
Run available unsupervised machine learning(ML) algorithms in AMBER on your molecular dynamics (MD) trajectories.
The program is designed to indicate the best algorithm which is most suited for, and preformed the best clustering on your data. The tool, will output associated statistical information and their associated graphs and data files for each ML algorithm into separate folders. 
The tool also comes with an additional features to run the individual ML algorithms (instead of running all algorithms) on your data.
The tool uses linear regression as well as distance calculations to determine the epsilon and mini-points, respectively, within your data for the DBSCAN algorithm. 

How to use the program/tool:
Please set up a virtual environment with (or make sure your system has) sciKit-learn downloaded. Please also make sure that AMBER's modules are activated. 
Run the program using the bash script './Clustering.sh', to which you'll be prompted to give the full path of your trajectory and topology files, as well as the residues or molecules that you wish to focus your clustering on (please use the amber format for the residues/molecular delimitations i.e. 'commas' or dashes'-'). You will also be asked for the sieved frames(the frames you wish to skip) for the DBSCAN algorithm. You will have the option to run any of the clustering algorithms individually (in which, please indicate your choice through writing out the number i.e. 
'1' for 'K Means', 
'2' for 'Hierarchial Average Linkage', 
'3' for 'Hierarchial Linkage', 
'4' for 'Hierarchial Complete', 
'5' for 'DBSCAN', or 
'6' for running all the algorithms and comparing their perfomance on your data. 

Unsupervised ML algorithms available:
K Means, Hierarchial Average Linkage, Hierarchial Linkage, Hierarchial Complete, DBSCAN. 

Example:
Toplogy/paramater file path:
/home/petgravm/temp/tools/AMBER_ML_TOOL/mod_parm.parm7

Trajectory file path:
/home/petgravm/temp/tools/AMBER_ML_TOOL/prod10.dcd

Residue clustering mask?:
125,126,202,170,130,56,120,254

sieved frames? (for DBSCAN):
1

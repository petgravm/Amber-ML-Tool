#!/bin/bash

main (){
    #Ask the user for the location of their paramater file
    echo path of paramater file?
    read varparm

    #Ask the user for the location of their trajectory file
    echo path of trajectory file?
    read vartraj

    #Ask for which residues to be considered for clustering
    echo "Residue clustering mask? ex)1-472"
    read mask

    # Ask for which clustering program to use
    echo Which Clustering algorithm do you want to use? \n 1.K means \n 2.Hierarchial_AverageLinkage \n 3. Hierarchial_Linkage \n 4.Hierarchial_Complete \n 5.DBSCAN \n 6.All
    read algorithm 

    # will go to the appopriate algorithm depending on the users choice
    if [ $algorithm == "1" ]
    then K_Means

    elif [ $algorithm == "2" ] 
    then Hierarchial_AverageLinkage

    elif [ $algorithm == "3" ]
    then Hierarchial_Linkage

    elif [ $algorithm == "4" ]
    then Hierarchial_Complete

    elif [ $algorithm == "5" ]
    then DBSCAN

	elif [ $algorithm == "6" ]
	then Run_All

    else
	    echo Please type corresponding digit for algorithm 

    fi
}

# Function for Kmeans algorithm
K_Means() {

	mkdir KMeans
    	cd KMeans
	counts=2;max=100; while [ $counts -le $max ]; do mkdir "cluster_$counts";
	cd "cluster_$counts";
	echo "parm $varparm">>cluster.in; 
	echo "trajin $vartraj">>cluster.in; 
	echo "cluster c0 \ ">>cluster.in; 
	echo "kmeans clusters $counts randompoint maxit 500 \ ">>cluster.in; 
	echo "rms :$mask@C,N,O,CA \ ">>cluster.in; 
	echo "sieve 10 random \ ">>cluster.in; 
	echo "out cnumvtime.dat \ ">>cluster.in; 
	echo "summary summary.dat \ ">>cluster.in; 
	echo "info info.dat \ ">>cluster.in; 
	echo "cpopvtime cpopvtime.agr normframe \ ">>cluster.in; 
	echo "repout rep repfmt pdb \ ">>cluster.in; 
	echo "singlerepout singlerep.dcd singlerepfmt dcd \ ">>cluster.in; 
	echo "avgout avg avgfmt pdb">>cluster.in; 
	echo "run">>cluster.in; $((counts++));cpptraj -i cluster.in; cd ..; done 

    	Generate_Stats
}

#Function for Hierarchical clustering average algorithm: use the average distance between members of two clusters
Hierarchial_AverageLinkage() {
	
	mkdir HierAvgLink
    	cd HierAvgLink
	counts=2;max=100; while [ $counts -le $max ]; do mkdir "cluster_$counts";
	cd "cluster_$counts";
	echo "parm $varparm">>cluster.in; 
	echo "trajin $vartraj">>cluster.in; 
	echo "cluster c1 \ ">>cluster.in; 
	echo "hieragglo epsilon 3.0 clusters $counts averagelinkage \ ">>cluster.in; 
	echo "rms :$mask@C,N,O,CA \ ">>cluster.in; 
	echo "sieve 10 random \ ">>cluster.in; 
	echo "out cnumvtime.dat \ ">>cluster.in; 
	echo "summary summary.dat \ ">>cluster.in; 
	echo "info info.dat \ ">>cluster.in; 
	echo "cpopvtime cpopvtime.agr normframe \ ">>cluster.in; 
	echo "repout rep repfmt pdb \ ">>cluster.in; 
	echo "singlerepout singlerep.dcd singlerepfmt dcd \ ">>cluster.in; 
	echo "avgout avg avgfmt pdb ">>cluster.in; 
	echo "run">>cluster.in; $((counts++));cpptraj -i cluster.in; cd ..; done 

    	Generate_Stats
}

#Function for Hierarchical clustering single linkage algorithm: use the shortest distance between members of two clusters
Hierarchial_Linkage() {
	
	mkdir HierLink
    	cd HierLink
	counts=2;max=100; while [ $counts -le $max ]; do mkdir "cluster_$counts";
	cd "cluster_$counts";
	echo "parm $varparm">>cluster.in; 
	echo "trajin $vartraj">>cluster.in; 
	echo "cluster c1 \ ">>cluster.in; 
	echo "hieragglo epsilon 3.0 clusters $counts linkage \ ">>cluster.in; 
	echo "rms :$mask@C,N,O,CA \ ">>cluster.in; 
	echo "sieve 10 random \ ">>cluster.in; 
	echo "out cnumvtime.dat \ ">>cluster.in; 
	echo "summary summary.dat \ ">>cluster.in; 
	echo "info info.dat \ ">>cluster.in; 
	echo "cpopvtime cpopvtime.agr normframe \ ">>cluster.in; 
	echo "repout rep repfmt pdb \ ">>cluster.in; 
	echo "singlerepout singlerep.dcd singlerepfmt dcd \ ">>cluster.in; 
	echo "avgout avg avgfmt pdb ">>cluster.in; 
	echo "run">>cluster.in; $((counts++));cpptraj -i cluster.in; cd ..; done 

    	Generate_Stats
}

#Function for Hierarchical clustering complete linkage algorithm: use the maximum distance between members of two clusters
Hierarchial_Complete() {
	
	mkdir HierComplLink
    cd HierComplLink
	counts=2;max=100; while [ $counts -le $max ]; do mkdir "cluster_$counts";
	cd "cluster_$counts";
	echo "parm $varparm">>cluster.in; 
	echo "trajin $vartraj">>cluster.in; 
	echo "cluster c1 \ ">>cluster.in; 
	echo "hieragglo epsilon 3.0 clusters $counts complete \ ">>cluster.in; 
	echo "rms :$mask@C,N,O,CA \ ">>cluster.in; 
	echo "sieve 10 random \ ">>cluster.in; 
	echo "out cnumvtime.dat \ ">>cluster.in; 
	echo "summary summary.dat \ ">>cluster.in; 
	echo "info info.dat \ ">>cluster.in; 
	echo "cpopvtime cpopvtime.agr normframe \ ">>cluster.in; 
	echo "repout rep repfmt pdb \ ">>cluster.in; 
	echo "singlerepout singlerep.dcd singlerepfmt dcd \ ">>cluster.in; 
	echo "avgout avg avgfmt pdb ">>cluster.in; 
	echo "run">>cluster.in; $((counts++));cpptraj -i cluster.in; cd ..; done 

    	Generate_Stats
}

#Function for DBSCAN clustering algorithm
DBSCAN(){
	
	Find_Eps_Mini
	#utilizing the python script to get the minipoints and epslison value 
	#whole_output="$(python ../find_eps.py)"
	#mini_points="$(echo "$whole_output" | cut -d' ' -f1)"
	#epsilon_num="$(echo "$whole_output" | cut -d' ' -f2)"
    #mini_points="$(grep -oP 'MiniPoints:\s+\K\"[0-9]+" 'Eps.txt)" 
	#epsilon_num="$(grep -oP 'Epsilon:\s+\K\"[0-9]+\.[0-9]*" 'Eps.txt)" 
    #python ../find_eps.py
   # python ../find_eps.py     
    mini_points="$(grep -m 1 -oP "[0-9]+" Eps.txt)"
    epsilon_num="$(grep -oP "[0-9]+\.[0-9]*" Eps.txt)"



	mkdir DBSCAN
    cd DBSCAN
	counts=2;max=2; while [ $counts -le $max ]; do mkdir "cluster_$counts";
	cd "cluster_$counts";
	echo "parm $varparm">>cluster.in; 
	echo "trajin $vartraj">>cluster.in; 
	echo "cluster c1 \ ">>cluster.in; 
	echo "dbscan minpoints $mini_points epsilon $epsilon_num sievetoframe \ ">>cluster.in; 
	echo "rms :$mask@C,N,O,CA \ ">>cluster.in; 
	echo "sieve 10 random \ ">>cluster.in; 
	echo "out cnumvtime.dat \ ">>cluster.in; 
	echo "summary summary.dat \ ">>cluster.in; 
	echo "summarysplit split_summary.dat \ ">>cluster.in; 
	echo "info info.dat \ ">>cluster.in;
	echo "cpopvtime cpopvtime.agr normframe \ ">>cluster.in; 
	echo "repout rep repfmt pdb \ ">>cluster.in; 
	echo "singlerepout singlerep.dcd singlerepfmt dcd \ ">>cluster.in; 
	echo "avgout avg avgfmt pdb ">>cluster.in; 
	echo "run">>cluster.in; $((counts++));cpptraj -i cluster.in; cd ..; done 

    Generate_Stats_DBSCAN
}

#Function will extract the files 
Generate_Stats() {

    counts=2;max=100; while [ $counts -le $max ]; do cd "cluster_$counts";
    #check if cluster.txt is not empty
    file="info.dat";
    #if it's not empty then:
    if grep -q "#DBI: 0.000000" $file; then
        result=${PWD##*/};
        printf "#DBI:0.00,#pSF:0.00,#SSR/SST:0.00" >>$result.txt;
        cd ..;

    elif [ -s info.dat ]; then
        count="$(ls -dq *rep.c* | wc -l)"
	    result=${PWD##*/};
        starts=$((count+2));
	    middle=$((count+4))p; 
	    quit=$((count+5))q;
	    sed -n "$starts,$middle;$quit" info.dat > $result.txt; 
    	let counts="counts +1"; 
    	cd ..;
#else:
    else
        result=${PWD##*/};
	    printf "#DBI:0.00,#pSF:0.00,#SSR/SST:0.00" >>$result.txt;

    fi
    done;
    
    python ../plot_Stats.py
    python ../plot_BestClust.py
    cd ..;
}

Generate_Stats_DBSCAN() {

#the function for DBSCAN only needs to iterate once
    counts=2;
    cd "cluster_$counts";
    file="info.dat";

    if grep -q "#DBI: 0.000000" $file; then
        result=${PWD##*/};
        printf "#DBI:0.00,#pSF:0.00,#SSR/SST:0.00" >>$result.txt;  
	    cd ..;

    elif [ -s info.dat ]; then
        result=${PWD##*/};
    	starts=$((counts+2));
		middle=$((counts+4))p; 
		quit=$((counts+5))q;
		sed -n "$starts,$middle;$quit" info.dat > $result.txt; 
    	cd ..;

#else:
	else
		result=${PWD##*/};
		printf "#DBI:0.00,#pSF:0.00,#SSR/SST:0.00" >>$result.txt;
        cd ..;

	fi

	python ../plot_DBSCAN.py
    cd ..;

}

#Find the eplison value and mini-points used for Hierarchial and DBSCAN clustering
Find_Eps_Mini(){

	echo number of sieved frames?
	read sieved 

	echo "parm $varparm">>dist.in; 
	echo "trajin $vartraj">>dist.in; 
	echo "cluster c10 dbscan kdist 1 rms :$mask@C,N,O,CA sieve $sieved loadpairdist pairdist CpptrajPairDist ">>dist.in; 
	echo "cluster c11 dbscan kdist 2 rms :$mask@C,N,O,CA sieve $sieved loadpairdist pairdist CpptrajPairDist ">>dist.in; 
	echo "cluster c12 dbscan kdist 3 rms :$mask@C,N,O,CA sieve $sieved loadpairdist pairdist CpptrajPairDist ">>dist.in; 
	echo "cluster c13 dbscan kdist 4 rms :$mask@C,N,O,CA sieve $sieved loadpairdist pairdist CpptrajPairDist ">>dist.in; 
	echo "cluster c14 dbscan kdist 5 rms :$mask@C,N,O,CA sieve $sieved loadpairdist pairdist CpptrajPairDist ">>dist.in; 
	echo "cluster c15 dbscan kdist 6 rms :$mask@C,N,O,CA sieve $sieved loadpairdist pairdist CpptrajPairDist ">>dist.in; 
	echo "cluster c16 dbscan kdist 7 rms :$mask@C,N,O,CA sieve $sieved loadpairdist pairdist CpptrajPairDist ">>dist.in; 
	echo "cluster c17 dbscan kdist 8 rms :$mask@C,N,O,CA sieve $sieved loadpairdist pairdist CpptrajPairDist ">>dist.in; 
	echo "cluster c18 dbscan kdist 9 rms :$mask@C,N,O,CA sieve $sieved loadpairdist pairdist CpptrajPairDist ">>dist.in;
	echo "cluster c19 dbscan kdist 10 rms :$mask@C,N,O,CA sieve $sieved loadpairdist pairdist CpptrajPairDist ">>dist.in; 
	echo "run">>dist.in;
	cpptraj -i dist.in;

	python find_eps.py

}

#Run all the algorithms and find the best Algorithm

Run_All(){

	DBSCAN;
	K_Means;
	Hierarchial_AverageLinkage;
	Hierarchial_Linkage;
	Hierarchial_Complete;

	python find_best_clust.py

}


main "$@"


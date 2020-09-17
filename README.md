
                SPDH                

SPDH
├─conf	                    #configuration file
├─datasets					#All data 
│	├─train_sequence		#The sequence files used for the training set
│	└─test_sequence			#The sequence files used for the test set
├─feature					#AAindex feature
├─model						#model data file
├─outwhd					#output file
└─src						#code folder

[Publication Title]
Predicting hot spot residues at protein-DNA binding interfaces based on sequence information
******************************************************
[Environment]
This software needs to run on Linux
A python2.7 environment is required
******************************************************
[Data]
	The data used before preprocessing is rawData.txt.
	Data comes from PrPDH. (http://bioinfo.ahu.edu.cn:8080/PrPDH/downloads/PrPDH_v1_benchmark.zip)
	
	train_pos_label.csv	is the preprocessed training set data and labels  
	test_pos_label.csv	is the preprocessed test set data and labels 
	train_feature.csv	is the feature of the training set data
	test_feature.csv	is the feature of the test set data
	train_sequence/ 	is the sequence file used in the training set
	test_sequence/		is the sequence file used in the test set
	
******************************************************
[REQUIREMENTS]
Need to download and install the following software

SPIDER2
	https://servers.sparks-lab.org/downloads/SPIDER2_local.tgz

Blast-2.2.18
	https://ftp.ncbi.nlm.nih.gov/blast/executables/legacy.NOTSUPPORTED/2.2.18/blast-2.2.18-x64-linux.tar.gz

ncbi-blast-2.7.1+
	ftp://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/2.7.1/ncbi-blast-2.7.1+-x64-linux.tar.gz

Netsurfp-1.0
	http://www.cbs.dtu.dk/cgi-bin/nph-sw_request?netsurfp
	And download the library files it needs http://www.cbs.dtu.dk/services/NetSurfP-1.0/data.tar.gz
	And the blast library files it uses http://www.cbs.dtu.dk/services/NetSurfP-1.0/nr70_db.tar.gz
	
DISOPRED 3.1
	http://bioinfadmin.cs.ucl.ac.uk/downloads/DISOPRED/DISOPRED3.16.tar.gz

******************************************************
Characteristics of the tool:
Spider2_path
	run_local_blast
	HSE_run1
Netsurfp_path
DISOPRED_path

******************************************************
conf/  is a configuration file
	you need change your path, like spider2...
feature/ is part of feature, don't move.

model/ is model data file. And Don't move it.

src/ is the code folder,  you can change it if you want.


******************************************************
[example]
run----->

python main.py -i 1AAY_A.seq -s3 1aay.i1 -o outScore

_________________________________________________
The '-i' is that input you seq.
The '-s3' is spider3 output for the input to your sequence file.
The '-o' is the output file.

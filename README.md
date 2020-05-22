This software needs to run on Linux
A python2.7 environment is required
******************************************************
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
example:
run----->

python main.py -i 1AAY_A.seq -s3 1aay.i1 -o outScore

_________________________________________________
The '-i' is that input you seq.
The '-s3' is spider3 output for the input to your sequence file.
The '-o' is the output file.

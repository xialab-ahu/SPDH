This software needs to run on Linux
A python2.7 environment is required
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
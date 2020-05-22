import os
import subprocess
import configparser


cf = configparser.ConfigParser()
cf.read('./conf/conf.data')
Spider2_path = cf.get("tools","Spider2_path")
Netsurfp_path = cf.get("tools","Netsurfp_path")
DISOPRED_path = cf.get("tools","DISOPRED_path")
run_local_blast = cf.get("tools","run_local_blast")
run1 = cf.get("tools","HSE_run1")



def excuteCommand(com):
    ex = subprocess.Popen(com, stdout=subprocess.PIPE, shell=True)
    out, err  = ex.communicate()
    ex.wait()
#    print("cmd in:", com)
#    print("cmd out: ", out.decode())
    return err

def isHaveFile(lis):
    out = []
    for file in lis:
        out.append(os.path.exists(file))
    flag = (len(out) <= sum(out))
    return flag

def run(commds, lis):
    excuteCommand(commds)
    if isHaveFile(lis):
        print('okAndFileexist.....')
    else:
        print('error.....')




class Feature():
    def __init__(self,path,seqPath):
        self.Path = path
        self.name = seqPath.split('/')[-1].replace('.seq','')
        self.Sqe = seqPath
        
        self.SPIDER2()
        self.NETSURFP()
        self.DISOPRED()
        self.AAINDEX()
        
        
    
    def SPIDER2(self):
        print('SPIDER2------------>>')
        commds = '{0} {1}'.format(Spider2_path + run_local_blast, self.Sqe)
        lis = [self.name+'.spd3', self.name+'.pssm']
        run(commds,lis)
        
        commds = '{0} {1} {2}'.format(Spider2_path + run1, './', './'+self.name+'.spd3')
        lis = [self.name+'.hsa2', self.name+'.hsb2']
        run(commds,lis)
        
    
    
    
    def NETSURFP(self):
        print('NetSurfP------------>>')
        commds = '{0} -i {1} -a > {2}'.format(
                Netsurfp_path+'netsurfp' ,
                self.Sqe,
                self.Path+self.name+'.myrsa',
                 )
        lis = [self.name+'.myrsa']
        run(commds,lis)
    
    
    
    def DISOPRED(self):
        print('DISOPRED------------>>')
        commds = '{0} {1}'.format(
                DISOPRED_path+'run_disopred.pl' ,
                self.Sqe,
                 )
        lis = [self.name+'.seq.diso']
        run(commds,lis)
    
    
    
    
    def AAINDEX(self):
        if os.path.exists('./feature/aaindex.txt'):
            print('aaindexOK------------>>')
        else:
            print('not have aaindex')
        return 0


















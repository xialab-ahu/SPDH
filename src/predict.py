import os
import numpy as np
import pandas as pd
from sklearn.externals import joblib
import warnings
warnings.filterwarnings('ignore')

'''
5-3:whd
'''


def SPIDER2(SPIDER2_path,fileList):
    cN = np.loadtxt(SPIDER2_path+fileList[0], delimiter='\t', dtype=str)[:,2:3]
    psi = np.loadtxt(SPIDER2_path+fileList[1], delimiter='\t', dtype=str)[:,5:6]
    hsa_HSEu = np.loadtxt(SPIDER2_path+fileList[0], delimiter='\t', dtype=str)[:,3:4]
    hsb_HSEu = np.loadtxt(SPIDER2_path+fileList[2], delimiter='\t', dtype=str)[:,3:4]
    return cN, psi, hsa_HSEu, hsb_HSEu


#SPIDER3(P(8I),P(8G))
def SPIDER3(SPIDER3_path,file):
    data = []
    with open(SPIDER3_path+file, 'r') as f:
        for line in f:
    #        line = line.replace('\n','')
            col = []
            i = 0
            while i <= len(line):
                word = ''
                for j in range(i,len(line)):
                    if line[j] == ' ' or line[j] == '\n':
                        i = j
                        break
                    else:
                        word+=line[j]
                if word != '':
                    col.append(word)
                i+=1
            data.append(col)
    data = np.array(data)[3:-3]
    return data[:,15:16], data[:,17:18]



#blast 
def Blast(Blast_path,file):
    import re
    rule = re.compile('^\s*[0-9]{1}.*$')
    data = []
    
    with open(Blast_path+file, 'r') as f:
        for line in f:
            if rule.match(line) is None: continue
            col = []
            i = 0
            while i <= len(line):
                word = ''
                for j in range(i,len(line)):
                    if line[j] == ' ' or line[j] == '\n':
                        i = j
                        break
                    else:
                        word+=line[j]
                if word != '':
                    col.append(word)
                i+=1
            data.append(col)
    
    data = np.array(data)[:,-20:]
    return data[:,:1], data[:,5:6], data[:,16:17], data[:,19:20], data[:,4:5], data[:,14:15]


#netsurfp-1.0(NetSurfP_ASA)
def Netsurfp(Netsurfp_path,file):
    data = []
    with open(Netsurfp_path+file, 'r') as f:
        for line in f:
            if line.startswith('#'): continue
            col = []
            i = 0
            while i <= len(line):
                word = ''
                for j in range(i,len(line)):
                    if line[j] == ' ' or line[j] == '\n':
                        i = j
                        break
                    else:
                        word+=line[j]
                if word != '':
                    col.append(word)
                i+=1
            data.append(col)
    return np.array(data)[:,5:6]


#DISOPRED 3.1(DISOPRED_Score)
def DISOPRED(DISOPRED_path,file):
    data = []
    with open(DISOPRED_path+file, 'r') as f:
        for line in f:
            if line.startswith('#'): continue
            line = line.replace('\n','').split(' ')[-1]
            data.append(line)
    return np.array(data).reshape(-1,1)


#AAINDEX(CZMAXF760103, CZVELV850101, CZWILM950102)	
def AAINDEX(AAINDEX_path, seq_path):
    seq = np.loadtxt(seq_path,dtype=str)[1]
    match = np.loadtxt('./feature/aaindex.txt',delimiter='\t',dtype=str,skiprows=1)
    data = []
    for sq in seq:
        for ma in match:
            if sq == ma[0]:
                data.append(ma[1:])
                break
    return np.array(data)



def getfeature(path, name,Spider3File):
    
    cN, psi, hsa_HSEu, hsb_HSEu = SPIDER2(path,[name+'.hsa2',name+'.spd3',name+'.hsb2'])
    P_8G, P_8I = SPIDER3(path,Spider3File)
    PSSM_A, PSSM_T, PSSM_Q, PSSM_V, PSSM_C, PSSM_P = Blast(path,name+'.pssm')
    NetSurfP_ASA = Netsurfp(path,name+'.myrsa')
    DISOPRED_Score = DISOPRED(path,name+'.seq.diso')
    AAindex = AAINDEX(path, './'+name+'.seq')
    
    return np.column_stack((P_8I,PSSM_A,PSSM_T,PSSM_Q,PSSM_V,DISOPRED_Score,PSSM_C,PSSM_P,AAindex[:,0:1],cN,hsb_HSEu,psi,P_8G,hsa_HSEu,NetSurfP_ASA,AAindex[:,1:]))



def models(model_path, path, name, Spider3File, outpath):
# =============================================================================
#     model_path:model data
#    path: feature path
#    name: seq name
#    Spider3File: e.g.1aay.i1
#    outpath: output path
# =============================================================================
    data = getfeature(path, name,Spider3File)
    np.savetxt(outpath+'/'+name+'_feature.txt', data, delimiter='\t', fmt='%s')
    
    
    print('dataProcessing_read')
    clf = joblib.load(model_path+os.sep+"S.dataProcessing")
    data = clf.transform(data)
    
    print ('model_read')
    model = joblib.load(model_path+os.sep+"model.my")
    y_proba = model.predict_proba(data)[:,1]
    
    
    out_score = np.column_stack((np.arange(1, len(y_proba)+1, 1),y_proba))
    
    np.savetxt(outpath+'/'+name+'_Score.txt',out_score,delimiter='\t',fmt='%s')
    print(name + ' get Score!')
    



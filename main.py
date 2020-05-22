import os
from src.feature import Feature
import src.predict as predict
import argparse

modelPath = './model/'


parser = argparse.ArgumentParser(usage="it's usage tip.", description="Whd 2020-5-13")
parser.add_argument("-i", "--inSeqFile",  help="input Seq file")
parser.add_argument("-s3", "--inSpider3File",  help="input Spider3 file")
parser.add_argument("-o", "--outScoreFile",  help="out Score file")

args = parser.parse_args()
seqFile=args.inSeqFile
outScoreFile = args.outScoreFile
Spider3File = args.inSpider3File
if not os.path.exists(outScoreFile):
    os.makedirs(outScoreFile)


seqPath = seqFile
seqFile = seqFile.split('/')[-1]
Spider3File = Spider3File.split('/')[-1]

print('your input seq:', seqFile)
print('your input spider3 data:', Spider3File)

runPath = os.path.dirname(os.path.abspath(__file__))+'/'



#feature
Feature(runPath, seqPath)


#predict
predict.models(modelPath,runPath, seqFile.replace('.seq',''),Spider3File , outScoreFile)




















import os
import sys
if (len(sys.argv)<2):

        print "usage: python3 train.py \"sampleimagename.jpg\""
	sys.exit()

else:
        print (sys.argv[1])
	sampleimg = sys.argv[1]

print("Creating Samples")
os.system("opencv_createsamples -img " + sampleimg + " -bg bg.txt -info info/info.lst -pngoutput info -maxxangle 0.5 -maxyangle 0.5 -maxzangle 0.5 -num 1950")

os.system("opencv_createsamples -info info/info.lst -num 1950 -w 20 -h 20 -vec positives.vec")
print("Training the samples")

os.system("opencv_traincascade -data data -vec positives.vec -bg bg.txt -numPos 1800 -numNeg 900 -numStages 12 -w 20 -h 20")

print("The Samples are tained successfully")

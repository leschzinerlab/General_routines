#!/usr/bin/env python

import optparse
from sys import *
import os,sys,re
from optparse import OptionParser
import glob
import subprocess
from os import system


#=========================
def setupParserOptions():
        parser = optparse.OptionParser()
        parser.set_usage("%prog -i [stack]")
	parser.add_option("-i", dest="stack",type="string",metavar="FILE",
                help="Input .mrc stack")
	parser.add_option("-d", action="store_true",dest="debug",default=False,
                help="debug")	
	options,args = parser.parse_args()
        if len(args) > 0:
                parser.error("Unknown commandline options: " +str(args))
	if len(sys.argv)<=1:
		parser.print_help()
                sys.exit()
        params={}
        for i in parser.option_list:
                if isinstance(i.dest,str):
                        params[i.dest] = getattr(options,i.dest)
	return params

#=============================
def checkConflicts(params):

	emanpath = subprocess.Popen("env | grep EMANDIR", shell=True, stdout=subprocess.PIPE).stdout.read().strip()
        if not emanpath:
                print "EMAN was not found, make sure EMAN is loaded"
                sys.exit()
	eman2path = subprocess.Popen("env | grep EMAN2DIR", shell=True, stdout=subprocess.PIPE).stdout.read().strip()
        if not eman2path:
                print "EMAN2 was not found, make sure EMAN2 is loaded"
                sys.exit()

 	#Check if outputs already exist
	i=1
	while i <= int(getNumImages(params['stack'])):
		if os.path.exists('%s_%05d.mrc' %(params['stack'].split('.')[0],i)):
			print 'Output file %s_%05d.mrc already exists. Exiting.' %(params['stack'].split('.')[0],i)
			sys.exit()
		i=i+1
	
#==============================
def getNumImages(stack):

	numimages=subprocess.Popen("iminfo %s"%(stack), shell=True, stdout=subprocess.PIPE).stdout.read().strip().split('\n')[3].split('\t')[0].split('x')[-1]

	return numimages
	
#==============================
if __name__ == "__main__":

	params=setupParserOptions()
	checkConflicts(params)
	
	if params['debug'] is True:
		print 'number of images in stack %s is %s'%(params['stack'],getNumImages(params['stack']))

	#Split up stack
	i=1
        while i <= int(getNumImages(params['stack'])):

		cmd='e2proc2d.py %s %s_%05d.mrc --first=%i --last=%i'%(params['stack'],params['stack'].split('.')[0],i,(i-1),(i-1))
		if params['debug'] is True:
			print cmd
		subprocess.Popen(cmd,shell=True).wait()	
		i=i+1	

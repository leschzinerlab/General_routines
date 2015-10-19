# General Routines
This repository will contain scripts for general data processing of single particle cryo-electron microscopy (cryo-EM) data sets.

## Extracting particles into a single stack using makeStack.py

###Inputs

*makeStack.py* assumes that the particles you have picked are stored in a *.box* file with the **same** micrograph name as the micrograph, which is in **.mrc** format. Particle coordinates stored as a *.box* file are within a text file that has four columns: X, Y, BoxSize X, BoxSize Y.

For instance, the output from [*runSignature.py*] (https://github.com/leschzinerlab/Signature) will provide particle coordinates in *.box* format that are compatible with *makeStack.py*.

####Picking particles

Typically users can pick particles using *boxer* from EMAN1.9 or *e2boxer.py* from EMAN2. Both can save particle coordinates in .box format.

####Estimating the CTF


###Outputs

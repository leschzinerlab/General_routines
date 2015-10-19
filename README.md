# General Routines
This repository will contain scripts for general data processing of single particle cryo-electron microscopy (cryo-EM) data sets.

## Extracting particles into a single stack using makeStack.py

###Inputs

*makeStack.py* assumes that the particles you have picked are stored in a *.box* file with the **same** micrograph name as the micrograph, which is in **.mrc** format. Particle coordinates stored as a *.box* file are within a text file that has four columns: X, Y, BoxSize X, BoxSize Y.

For instance, the output from [*runSignature.py*] (https://github.com/leschzinerlab/Signature) will provide particle coordinates in *.box* format that are compatible with *makeStack.py*.

####Picking particles

Typically users can pick particles using *boxer* from EMAN1.9 or *e2boxer.py* from EMAN2. Both can save particle coordinates in .box format.

####Estimating the CTF

Below, users have the option to extract 1) phase flipped particles or 2) RCT/OTR particle pairs. For either of these processing outputs, you will need to run:

1) phase flipping: CTFFIND3 --> [estimateCTF_CTFFIND3.py] (https://github.com/leschzinerlab/FREALIGN/tree/master/ctffind_ctftilt)

2) RCT/OTR: CTFTILT --> [estimateCTF_CTFTILT.py] (https://github.com/leschzinerlab/FREALIGN/tree/master/ctffind_ctftilt)

These programs will output text files with CTF and tilt information.

###Running the program: extracting raw particles (no phase flipping)

```
/data/Scripts/makeStack.py --micros='*en.mrc' -o outputstack.img
```

###Running the program: exacting particles WITH phase flipping


###Running the program: exacting RCT/OTR tilt mates

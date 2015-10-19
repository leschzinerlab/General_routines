# General Routines
This repository will contain scripts for general data processing of single particle cryo-electron microscopy (cryo-EM) data sets.

*Table of contents*
- [Extracting particles using makeStack.py](https://github.com/leschzinerlab/General_routines#extracting-particles-using-makestackpy)
- Estimating CTF using CTFFIN3 and CTFTILT

## Extracting particles using makeStack.py

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

###Dependencies

This software requires [SPIDER] (http://spider.wadsworth.org/spider_doc/spider/docs/spider.html) and [EMAN2] (http://blake.bcm.edu/emanwiki/EMAN2) to be installed & libraries correctly setup.

###Running the program

Input options for the program are displayed by running the program without any options on the command line:

```
$ /General_routines/makeStack.py
Usage: makeStack.py --micros=<micrographs> --box=<boxfiles> -o <output stack name.img>

Options:
  -h, --help       show this help message and exit
  --micros=FILE    Path to micrographs with wildcard in quotes ('*en.mrc')
                   (Not needed for tilt mates)
  -o FILE          Output stack name (.img). If tilt mates, do not provide
                   .img extension, output stack name will be the base name for
                   tilted and untilted particles.
  --bin=INT        Optional: Binning factor used during boxer picking
                   (Default=1)
  --invert         Invert contrast of micrographs
  --boxsize=INT    Optional: box size for final stack. (Default is size used
                   in boxer picking)
  --phaseflip      Flag to phase flip particles
  --ctf=STRING     If phase-flipping - ctf_param.txt output file from
                   estimateCTF_CTFFIND.py if not using tilt mates
  --untilt=STRING  If extracting tilt mates - provide CTFTILT output file for
                   UNtilted micrographs created by estimateCTF_CTFTILT.py.
                   Assumes extension is '01'.
  --tilt=STRING    If extracting tilt mates - provide CTFTILT output file for
                   TILTED micrographs created by estimateCTF_CTFTILT.py.
                   Assumes extension is '00'.
  --noinsideonly   Flag to NOT exclude particles on edges of images (needed
                   for tilt pairs)
  -d               debug
  ```

####Extracting raw particles (no phase flipping)

To extract particles from your micrographs without phase flipping or extracting tilt mates for OTR/RCT, you just need to specify the path to the micrographs and provide an output stack name. **NOTE** The box files are assumed to be the same name as the micrograph names.

```
$ /General_routines/makeStack.py --micros='*en.mrc' -o outputstack.img
```

####Extracting particles WITH phase flipping

To extract particles from phase flipped micrographs, you can execute this command, specifying *--phaseflip* and providing the *ctf_param.txt* file, which is the output from *estimateCTF_CTFFIND.py*:

```
$ /General_routines/makeStack.py --micros='*en.mrc' -o outputstack.img --phaseflip --ctf=ctf_param.txt
```

####Extracting RCT/OTR tilt mates

*work in progress*

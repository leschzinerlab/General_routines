#!/usr/bin/bash

#Will convert all .dm3 micros to .mrc
for i in $(ls *.dm3); do proc2d ${i%%.*}.dm3 ${i%%.*}.mrc; done

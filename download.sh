#!/bin/bash
URL=https://zenodo.org/record/6245867/files/CDFdataCodeWmass.tgz
rm -rf data
mkdir data
cd data
wget $URL
tar -xzf CDFdataCodeWmass.tgz
rm CDFdataCodeWmass.tgz
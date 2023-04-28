# RNAframework Scripts

RNA-Framework is a tool for processing data from various structure probing experiments. This repository holds scripts for running RNAframework for different tasks and analyzing output files. 

- ```xml2tab.py```: Convert and XML or a directory of XML files outputted by RNAframewok to a single tab-delineated file. 
```
usage: xml2tab.py [-h] [-i REACT_FILE] [-o OUT_FILE]

Convert an XML file or directory of XML files output from the RNA framework to a tab-delimited file

options:
  -h, --help     show this help message and exit
  -i REACT_FILE  XML file or directory of XML files
  -o OUT_FILE    fasta file

```
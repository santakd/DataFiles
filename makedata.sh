#!/bin/bash
echo -------------------------------------
echo creating data files from ObjectId.csv
echo -------------------------------------
  
python3 split01_obj.py 1

python3 split05_obj.py 5

python3 split20_obj.py 20

python3 split40_obj.py 40

python3 split60_obj.py 60

python3 split80_obj.py 80

python3 split100_obj.py 100

echo -------------------------------------
echo creating data files from ObjectId2.csv
echo -------------------------------------

python3 merge05_obj2.py 5

python3 split01_obj2.py 1

echo -------------------------------------
echo finished creating the csv data files
echo -------------------------------------

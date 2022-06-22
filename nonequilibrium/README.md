# nonequilibrium: nonequilibrium sub-module

Date:               22-Apr-22
Version:            0.1.0

### Description of files in this directory
README.md           this file
main.py             solver to generate nonequilibrium drop
run.sh              run solver
data/*              storage of numerical data
fig/*               save visualizations

### Usage
0. data/ and fig/ will be automatically generated.
1. Run the run.sh with following arguments:
   alpha beta_2 beta_3 R_b h1_init h2_init h3_init
   For example:
   ./run.sh 0.2 1.2 0.8 0.45 0.1 0.5 0.1
   generates figure 2a of Assovskii2002.

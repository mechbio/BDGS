# growth: growth sub-module

Date:               22-Apr-22
Version:            0.1.0

### Description of files in this directory
README.md           this file
main.py             solver to simulate growing drop
run.sh              run simulation
data/*              storage of numerical data
fig/*               save visualizations

### Usage
0. data/ and fig/ will be automatically generated.
1. Run the run.sh with following arguments:
   n_frames gif_fps g1 g2 dt
   For example:
   ./run.sh 60 30 1.0 3.0 0.1

#!/bin/bash
# -*- coding: utf-8 -*-

# BDGS: Binary Drop Growth Simulator
#
# See the README file in the top-level directory.

# -----------------------------------------------------------------------------
# This file (run.sh) is used to run main.py.
# -----------------------------------------------------------------------------

# date         :22-Jun-22
# version      :0.1.0
# usage        :./run.sh 60 30 1.0 3.0 0.1
# sh_version   :5.0.17(1)-release

# Ensure fig/ and data/ exist
mkdir -p fig/
mkdir -p data/

# run simulation
# n_frames gif_fps g1 g2 dt
python3 main.py $1 $2 $3 $4 $5

# view GIF
animate fig/drop.gif

exit 0

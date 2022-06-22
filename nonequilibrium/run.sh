#!/bin/bash
# -*- coding: utf-8 -*-

# BDGS: Binary Drop Growth Simulator
#
# See the README file in the top-level directory.

# -----------------------------------------------------------------------------
# This file (run.sh) is used to run main.py.
# -----------------------------------------------------------------------------

# date         :20-Jun-22
# version      :0.1.0
# usage        :./run.sh 0.2 1.2 0.8 0.45 0.1 0.5 0.1
# sh_version   :5.0.17(1)-release

# Ensure fig/ and data/ exist
mkdir -p fig/
mkdir -p data/

# run solver
# alpha beta_2 beta_3 R_b h1_init h2_init h3_init
python3 main.py $1 $2 $3 $4 $5 $6 $7

exit 0

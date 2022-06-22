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
# usage        :./run.sh
# sh_version   :5.0.17(1)-release

# Ensure fig/ and data/ exist
mkdir -p fig/
mkdir -p data/

# run solver
python3 main.py

exit 0

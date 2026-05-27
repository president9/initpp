#!/usr/bin/env python3
import os
import sys
from pathlib import Path
import subprocess
from generator import generator
import argparse


if len(sys.argv) < 2:
    print("Basic usage: initpp -n project_name")
    sys.exit(1)

parser = argparse.ArgumentParser()
parser.add_argument("-n", help="Create a new project. Usage: initpp -n project_name to create a project")
parser.add_argument("-opt", help="Set optimisation value. Usage: -opt n Enables march native and [O0|O1|O2|O3]")
parser.add_argument("-inc", help="Include the libraries you want. Usage: -include boost;gtest")
args = parser.parse_args()

generator(args)


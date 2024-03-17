import argparse
import os

parser = argparse.ArgumentParser(description='parse flags')
parser.add_argument('-d', '--dir', default=os.getcwd(), type=str, help='starting directory')
parser.add_argument('-n', '--nest', default=1000, type=int, help='nesting')
args = parser.parse_args()

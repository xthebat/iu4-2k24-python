import argparse

parser = argparse.ArgumentParser(description='parse flags')
parser.add_argument('dir', type=str, help='starting directory')
parser.add_argument('nest', type=int, help='nesting')
args = parser.parse_args()

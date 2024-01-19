import argparse

parser = argparse.ArgumentParser(description='A simple script with argparse')
parser.add_argument('-a', help='Input file path')
args = parser.parse_args()

print(f"Input file: {args}")

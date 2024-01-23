import argparse
import subprocess


parser = argparse.ArgumentParser(description='A simple script with argparse')
parser.add_argument('-a', help='Input file path')
parser.add_argument('-m', help='Git commit message')
args = parser.parse_args()

print(f"Input file: {args}")

# PIPE = subprocess.PIPE


# process = subprocess.Popen(['git', 'show', "-s", '--format=%s'], stdout=PIPE, stderr=PIPE)

# stdoutput, stderror =  process.communicate()

# print('stdoutput', stdoutput)
# print('stderror', stderror)

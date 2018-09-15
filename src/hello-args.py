#!/usr/bin/env python
import argparse

parser = argparse.ArgumentParser(description="Say hello")
parser.add_argument('--name')

args = parser.parse_args()

print("hello,", args.name)

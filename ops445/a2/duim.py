#!/usr/bin/env python3

import subprocess, sys
import os
import argparse

'''
OPS445 Assignment 2 - Winter 2022
Program: duim.py 
Author: Azebaze Ngueya Aime Parfait
The python code in this file (duim.py) is original work written by
Azebaze Ngueya Aime Parfait. No code in this file is copied from any other source 
except those provided by the course instructor, including any person, 
textbook, or online resource. I have not shared this python script 
with anyone or anything except for submission for grading.  
I understand that the Academic Honesty Policy will be enforced and 
violators will be reported and appropriate action will be taken.

Description: This script displays disk usage for a specified directory
in the form of a text-based bar chart.

Date: 4/10/2025
'''

def parse_command_args():
    "Set up argparse here. Call this function inside main."
    parser = argparse.ArgumentParser(description="DU Improved -- See Disk Usage Report with bar charts", epilog="Copyright 2022")
    parser.add_argument("-l", "--length", type=int, default=20, help="Specify the length of the graph. Default is 20.")
    parser.add_argument("-H", "--human-readable", action="store_true", help="Show disk usage in human-readable format (e.g., 1K, 234M, 2G).")
    parser.add_argument("target", type=str, help="Target directory for disk usage analysis.")
    args = parser.parse_args()
    return args

def percent_to_graph(percent, total_chars):
    "Returns a string: eg. '##  ' for 50 if total_chars == 4"
    num_hashes = int(percent / 100 * total_chars)  # Calculate number of hashes based on the percent
    return "#" * num_hashes + " " * (total_chars - num_hashes)

def call_du_sub(location):
    "takes the target directory as an argument and returns a list of strings"
    "returned by the command `du -d 1 location`"
    try:
        result = subprocess.check_output(["du", "-d", "1", location], stderr=subprocess.STDOUT)
        return result.decode().splitlines()
    except subprocess.CalledProcessError as e:
        print(f"Error: {e.output.decode().strip()}")
        return []  # Returning an empty list if the command fails


def create_dir_dict(alist):
    "Takes a list from call_du_sub, returns a dictionary with full directory name as key, and the number of bytes as value."
    dir_dict = {}
    for line in alist:
        size, directory = line.split("\t")
        dir_dict[directory] = int(size)
    return dir_dict

def main():
    args = parse_command_args()
    
    # Call the `du` command to get disk usage for the target directory
    du_output = call_du_sub(args.target)
    
    # Create a dictionary of directories and their sizes
    dir_dict = create_dir_dict(du_output)

    # Display the results
    for directory, size in dir_dict.items():
        if args.human_readable:
            # If human-readable is requested, use human-readable format (e.g., 1K, 234M, 2G)
            size_human = subprocess.run(["du", "-sh", directory], stdout=subprocess.PIPE).stdout.decode().split()[0]
            print(f"{directory}: {size_human}")
        else:
            # Otherwise, show the size in bytes
            print(f"{directory}: {size} bytes")

        # Create a bar chart (percentage of total size)
        total_size = sum(dir_dict.values())
        percent = (size / total_size) * 100
        graph = percent_to_graph(percent, args.length)
        print(f"  | {graph} | {percent:.2f}%")

if __name__ == "__main__":
    main()

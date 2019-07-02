#!/usr/bin/python3

import subprocess

import sys

import time
from functools import wraps

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

def usage():
    eprint("Usage:	paraevaluar [OPTIONS]... program")
    eprint("\tOPTIONS:")
    eprint("\t\t-N|--iterations ITERATIONS\tspecify the number of iterations each binary will be executeds.")
    eprint("\t\t-i|--ignore-golden\t\tdon't abort when output doesn't match golden output")
    eprint("\t\t-prefix PREFIX\t\t\tspecify the path of th program (default \$PWD)")
    eprint("\t\t-d|--directory EVALDIR\t\tsets the paraevaluar working directory to EVALDIR")
    eprint("\t\t-name NAME\t\t\tsets to the execution the alias NAME")
    eprint("\t\t-original\t\t\tforces the program to be treated as the original")
    eprint("\t\t-t|--time-path PATH\t\tto specify the path of time (default /usr/bin/time)")
    eprint("\t\t-v|--verbose\t\t\tverbose")
    eprint("\t\t-report [REPORT OPTIONS]\tdisplays the report of the evaluations (default REPORT OPTIONS: TABLE)")
    eprint("\t\t-o|--output FILE\t\tappends the result of the evaluation to the FILE")
    eprint("\t\t--clean\t\t\t\tdeletes all evaldir in the current directory")
    eprint("\t\t-h|--help\t\t\tprint this usage")
    eprint("\tREPORT OPTIONS:")
    eprint("\t\tTABLE\tdisplays a table")
    eprint("\t\tPLOT\tdisplays a speedup plot")

def show_error(msg):
    print("=> ERROR: " + msg)

def show_warning(msg):
    print("=> WARNING: " + msg)

def show_note(msg):
    print("=> NOTE: " + msg)

def errorNexit(msg):
	show_erro(msg)

def run(prog):
	start_time = time.time()
	subprocess.run(prog)
	elapsed_time = time.time() - start_time
	return elapsed_time
#	show_note("Time: " + str(elapsed_time));

def main(args):
	avg=0
	for i in range(3):
		avg += run(args)
	avg /= 3;
	show_note("Time -> " + str(avg) + "s")

if __name__ == "__main__":
   main(sys.argv[1:])

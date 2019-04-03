
# paraevaluar

## What is paraevaluar?

Paraevaluar is a performance analysis script that allows developers to compare an original version of an application to optimized ones, checking that the output is the same.

## Usage
```
Usage:	paraevaluar [OPTIONS]... program
	OPTIONS:
		-N|--iterations ITERATIONS	specify the number of iterations each binary will be executeds.
		-i|--ignore-golden		don't abort when output doesn't match golden output
		-prefix PREFIX			specify the path of th program (default $PWD)
		-d|--directory EVALDIR		sets the paraevaluar working directory to EVALDIR
		-name NAME			sets to the execution the alias NAME
		-original			forces the program to be treated as the original
		-t|--time-path PATH		to specify the path of time (default /usr/bin/time)
		-v|--verbose			verbose
		-report [REPORT OPTIONS]	displays the report of the evaluations (default REPORT OPTIONS: TABLE)
		-o|--output FILE		appends the result of the evaluation to the FILE
		--clean				deletes all evaldir in the current directory
		-h|--help			print this usage
	REPORT OPTIONS:
		TABLE	displays a table
		PLOT	displays a speedup plot

```
## Dependencies
The dependencies needed are coreutils, gawk, time, groff-base, bc, gnuplot

Other dependencies for extended features:
In order to plot data gnuplot is required to be installed.


## Example

In the examples folder, first compile the code using different gcc optimitzation levels.
```
make all
```
Then run the command to evaluate the code, execute 4 times each binary, pass the argument 3333 to the programs.
```
../paraevaluar -N 4 pi.O0 3333
../paraevaluar -N 4 pi.O1 3333
../paraevaluar -N 4 pi.O2 3333
../paraevaluar -N 4 pi.O3 3333
../paraevaluar -N 4 pi.Ofast 3333
```
Get the results of the execution.
```
../paraevaluar --report TABLE PLOT
```
We get the following output and a beautifull plot:
```
Results for pi.O0:
+---------+------+------+--------+----------+--------+--------+--------+------------+
|Program  | MaxE | MinE | AvgE   | SpeedUpE | MaxCPU | MinCPU | AvgCPU | SpeedUpCPU |
+---------+------+------+--------+----------+--------+--------+--------+------------+
|pi.O0    | 0.18 | 0.17 | 0.1733 | -        | 0.18   | 0.17   | 0.1722 | -          |
+---------+------+------+--------+----------+--------+--------+--------+------------+
|pi.O1    | 0.09 | 0.09 | 0.0900 | 1.9256   | 0.09   | 0.09   | 0.0894 | 1.9262     |
+---------+------+------+--------+----------+--------+--------+--------+------------+
|pi.O2    | 0.06 | 0.06 | 0.0600 | 2.8883   | 0.06   | 0.06   | 0.0588 | 2.9286     |
+---------+------+------+--------+----------+--------+--------+--------+------------+
|pi.O3    | 0.06 | 0.06 | 0.0600 | 2.8883   | 0.06   | 0.06   | 0.0596 | 2.8893     |
+---------+------+------+--------+----------+--------+--------+--------+------------+
|pi.Ofast | 0.06 | 0.06 | 0.0600 | 2.8883   | 0.06   | 0.06   | 0.0592 | 2.9088     |
+---------+------+------+--------+----------+--------+--------+--------+------------+
```

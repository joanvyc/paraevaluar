
# paraevaluar

## What is paraevaluar?

Paraevaluar is a performance analysis script that allows developers to compare an original version of an application to optimized ones, checking that the output is the same.

## Usage

```
Usage:	paraevaluar [OPTIONS]... original [updated]...
	OPTIONS:
		-h|--help		print this usage.
		-N ITERATIONS		specify the number of iterations each binary will be executed.
		-o|--output FILE	appends the result of the evaluation to the FILE
		-i|--ignore-golden	don't abort when output doesn't match golden output.
		-a|--arguments=ARGUMENT	append ARGUMENT to the argument list.
		-p|--plots		plot average time of different versions.
		-t|--time-path		specify where is the path of GNU/Time(Default:/usr/bin/time)
		--no-cleanup		keeps the intermediate files used by the program.
		--clean			deletes all evaldir in the current directory.

```
## Dependencies
The dependencies needed are coreutils, gawk, time, groff-base, bc

Other dependencies for extended features:
In order to plot data gnuplot is required to be installed.


## Example

In the examples folder, first compile the code using different gcc optimitzation levels.
```
make all
```
Then run the command to evaluate the code, execute 4 times each binary, pass the argument 3333 to the programs.
```
../paraevaluar -N 4 -a 3333 -p pi.O0 pi.O1 pi.O2 pi.O3 pi.Ofast  #paraevaluar is not installed
```
We get the following output:
```
Results for pi.O0:
+---------+------+------+--------+----------+--------+--------+--------+------------+
|Program  | MaxE | MinE | AvgE   | SpeedUpE | MaxCPU | MinCPU | AvgCPU | SpeedUpCPU |
+---------+------+------+--------+----------+--------+--------+--------+------------+
|Original | 0.18 | 0.17 | 0.1733 | -        | 0.18   | 0.17   | 0.1722 | -          |
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


# evaluate

## What is evaluate?

Evaluate is a performance analysis script that allows developers to compare an original version of an application to optimized ones, checking that the output is the same.

## Usage

```
Usage:	evaluate [OPTIONS]... original updated...
	OPTIONS:
		-h|--help		print this usage.
		-N ITERATIONS		specify the number of iterations each binary will be executed.
		-o|--output FILE	appends the result of the evaluation to the FILE
		-i|--ignore-golden	don't abort when output doesn't match golden output.
		-a|--arguments=ARGUMENT	append ARGUMENT to the argument list.
		-p|--plots		plot average time of different versions.
		--no-cleanup		keeps the intermediate files used by the program.

```
## Dependencies
In order to plot data gnuplot is required to be installed.

## Example

In the examples folder, first compile the code using different gcc optimitzation levels.
```
make all
```
Then run the command to evaluate the code, execute 4 times each binary, pass the argument 3333 to the programs.
```
../evaluate -N 4 -a 3333 -p ./pi.O0 ./pi.O1 ./pi.O2 ./pi.O3 ./pi.Ofast  #suposing evaluate is not installed
```
We get the following output:
```
Results:
Program     MaxE  MinE  AvgE    SpeedUp  MaxP  MinP  AvgP
Original    0.98  0.96  0.9650  -        98    96    96.5000
./pi.O1     0.56  0.52  0.5350  1.8037   56    52    53.5000
./pi.O2     0.36  0.34  0.3500  2.7571   36    34    35.0000
./pi.O3     0.35  0.34  0.3450  2.7971   35    34    34.5000
./pi.Ofast  0.35  0.33  0.3425  2.8175   35    33    34.2500
```



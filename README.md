
# paraevaluar

## What is paraevaluar?

Paraevaluar is a performance analysis script that allows developers to compare an original version of an application to optimized ones, checking that the output is the same.

## Usage
```
Usage:	paraevaluar [GLOBAL_OPTIONS] <command> [OPTIONS]
	GLOBAL_OPTIONS:
		-f | --file  <file> specify <file> as the config file. (default ./paraevaluar.xml) [unimplemented]
	commands:
		init
		script
		add
		eval
		report
```
### Init command
The init command initialises an empty project inside the current folder based on the `paraevaluar.xml` file.	
```
Usage:	paraevaluar init [OPTIONS]
	OPTIONS:
		--help	prints this message and exits	
```
### Script command
The script generates the template script for the eval stage based on the `paraevaluar.xml` file.
```
Usage:	paraevaluar script [OPTIONS]
	OPTIONS:
		--help	prints this message and exit
		-e | --editor when the script is generated, open up an editor to edit the script
```
### Add command
The add command copies the given files to the execution directory.
```
Usage:	paraevaluar add <file>...
```
### Eval command
The eval command executes the script for each possible configuration given the `paraevaluar.xml` file.
```
Usage:	paraevaluar eval
```

### Report command
The report command is unimplemented.

## Dependencies
The dependencies needed are coreutils, gawk, time, bc, xmlstarlet

## Example
TODO when report option is implemented
```

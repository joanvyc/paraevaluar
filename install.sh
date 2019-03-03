#!/bin/bash

if [[ ! -f /usr/bin/evaluate ]]; then
	cp evaluate /usr/bin/evaluate;
else
	echo -e "\033[1;31m Error: file /usr/bin/evaluate already exists.\033[0m"
fi



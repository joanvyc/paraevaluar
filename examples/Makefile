
all: pi.O0 pi.O1 pi.O2 pi.O3 pi.Ofast

pi.O0: pi.c
	gcc -O0 $< -o $@
pi.O1: pi.c
	gcc -O1 $< -o $@
pi.O2: pi.c
	gcc -O2 $< -o $@
pi.O3: pi.c
	gcc -O3 $< -o $@
pi.Ofast: pi.c
	gcc -Ofast $< -o $@
clean:
	rm -rf pi.O0 piO1 pi.O2 pi.O3 pi.Ofast




libparaevaluar.so: libparaevaluar.c
	gcc -shared -fPIC $< -o $@ -ldl

paraevaluar.x: paraevaluar paraevaluar.addfile paraevaluar.eval paraevaluar.init paraevaluar.report paraevaluar.script paraevaluar.utils
	shc -v -r -f $^

paraevaluar_2.1-0:
	DEBIAN


clean:
	rm libparaevaluar.so

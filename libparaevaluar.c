#define _GNU_SOURCE
#include <dlfcn.h>

#include <stdio.h> 
#include <stdlib.h>

#include <time.h>
#include <sys/time.h>

typedef  void (*orig_exit_f)(int error);
typedef void (*orig_fini_f)(void);
typedef int (*orig_main_f)(int (*main) (int, char **, char **
					 MAIN_AUXVEC_DECL),
			    int argc,
			    char **argv,
#ifdef LIBC_START_MAIN_AUXVEC_ARG
			    ElfW(auxv_t) *auxvec,
#endif
			    __typeof (main) init,
			    void (*fini) (void),
			    void (*rtld_fini) (void),
			    void *stack_end);

extern void exit(int exit_code)  __attribute__ ((noreturn));

struct timeval tv0, tv1;

int eval_init(int argv, char **argc, char ** a) {
	printf("Starting...\n");
	gettimeofday(&tv0, NULL);
}

void eval_fini(void) {
	printf("Exiting...\n");
}

extern void __libc_start_main (int (*main) (int, char **, char ** MAIN_AUXVEC_DECL),
		int argc, char **argv,
			    __typeof (main) init,
			    void (*fini) (void),
			    void (*rtld_fini) (void),
			    void *stack_end)
{
	orig_main_f orig_main;
	orig_main = (orig_main_f) dlsym(RTLD_NEXT, "__libc_start_main");
	orig_main(main, argc, argv, eval_init, eval_fini, rtld_fini, stack_end);
}

void exit(int exit_code) 
{
	printf("Exiting...\n");
	gettimeofday(&tv1, NULL);

	tv1.tv_sec  -= tv0.tv_sec;
	tv1.tv_usec -= tv0.tv_usec;

	tv0.tv_sec  -= tv0.tv_sec;
	tv0.tv_usec -= tv0.tv_usec;

	printf("Time: %f s\n", tv1.tv_sec + (tv1.tv_usec/1000000.f));

	orig_exit_f orig_exit;
	orig_exit = (orig_exit_f) dlsym(RTLD_NEXT, "exit");
	orig_exit(exit_code);
	while (1) {}
} 


#include "trace.h"
#include "logger.h"
#include <stdio.h>

void trace_enter(const char* name){
    char b[32];
    snprintf(b,32,"%s_ENTER",name);
    log_event(b);
}
void trace_exit(const char* name){
    char b[32];
    snprintf(b,32,"%s_EXIT",name);
    log_event(b);
}

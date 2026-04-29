
#include "logger.h"
#include "FreeRTOS.h"
#include "task.h"
#include <stdio.h>
#include <string.h>

#define LOG_BUFFER_SIZE 1024

typedef struct {
    uint32_t ts;
    char event[32];
} Log;

static Log buf[LOG_BUFFER_SIZE];
static int idx = 0;

void log_event(const char* e){
    if(idx>=LOG_BUFFER_SIZE) return;
    buf[idx].ts = xTaskGetTickCount();
    strncpy(buf[idx].event, e, 31);
    idx++;
}

void dump_logs(void){
    for(int i=0;i<idx;i++){
        printf("LOG,%lu,%s\n", buf[i].ts, buf[i].event);
    }
}

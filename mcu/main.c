
#include "FreeRTOS.h"
#include "task.h"
#include "trace.h"

void imu_task(void* p){
    while(1){
        trace_enter("IMU");
        for(volatile int i=0;i<60000;i++);
        trace_exit("IMU");
        vTaskDelay(1);
    }
}

void motor_task(void* p){
    while(1){
        trace_enter("MOTOR");
        for(volatile int i=0;i<30000;i++);
        trace_exit("MOTOR");
        vTaskDelay(1);
    }
}

int main(){
    xTaskCreate(imu_task,"imu",256,NULL,3,NULL);
    xTaskCreate(motor_task,"motor",256,NULL,2,NULL);
    vTaskStartScheduler();
    while(1);
}

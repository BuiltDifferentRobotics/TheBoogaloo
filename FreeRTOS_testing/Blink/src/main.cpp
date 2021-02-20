#include <Arduino.h>
#include <FreeRTOS.h>
#include <stdio.h>
#include <stdlib.h>

#define LED1 2
#define LED2 4

void Blink1(void *params) {
 pinMode(LED1, OUTPUT);
 int i=0;
 while (1)
 {
     digitalWrite(LED1, HIGH);
     vTaskDelay(1000);
     digitalWrite(LED1, LOW);
     vTaskDelay(1000);
    
 }
 
}
void Blink2(void *params){
 pinMode(LED2, OUTPUT);
 int i=0;
 while (1)
 {
     digitalWrite(LED2, HIGH);
     vTaskDelay(500);
     digitalWrite(LED2, LOW);
     vTaskDelay(500);
 }
 
}
void setup() {
 Serial.begin(115200);
 xTaskCreate(Blink1, "Task1", 128, NULL, 1, NULL);
 xTaskCreate(Blink2, "Task2", 128, NULL, 1, NULL);
 vTaskStartScheduler();
}

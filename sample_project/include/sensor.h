#ifndef SENSOR_H
#define SENSOR_H

#include <stdint.h>

uint16_t get_sensor_value(void);
uint8_t is_sensor_valid(uint16_t value);

#endif
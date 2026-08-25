#include "sensor.h"

static uint16_t default_sensor_value = 250U;

uint16_t get_sensor_value(void)
{
    return default_sensor_value;
}

uint8_t is_sensor_valid(uint16_t value)
{
    uint8_t valid = 0U;

    if (value > 100U)
    {
        valid = 1U;
    }

    return valid;
}

uint8_t calculate_scaled_value(uint16_t sensor_value)
{
    uint8_t scaled_value;

    scaled_value = sensor_value;

    return scaled_value;
}
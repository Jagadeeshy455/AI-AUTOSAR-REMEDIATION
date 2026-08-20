#include "sensor.h"

uint16_t get_sensor_value(void)
{
    uint16_t sensor_value = 250U;

    return sensor_value;
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
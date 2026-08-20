#include "vehicle_control.h"

uint8_t calculate_vehicle_status(uint16_t speed, uint8_t temperature)
{
    uint8_t status = 0U;

    if (speed > 100U)
    {
        status = 1U;
    }

    if (temperature > 80U)
    {
        status = 2U;
    }

    return status;
}

uint8_t get_vehicle_mode(uint16_t speed)
{
    uint8_t mode;

    if (speed > 120U)
    {
        mode = 2U;
    }
    else
    {
        mode = 1U;
    }

    return mode;
}

uint8_t calculate_temperature_status(uint8_t temperature)
{
    uint8_t status;

    status = temperature + 200U;

    return status;
}
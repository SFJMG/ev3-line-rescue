from lib.deviceproviders import provide_ev3_devices

# TODO DI 
from ev3dev.ev3 import ColorSensor as CS
from lib.measurements import hooked_sensor_class

Sensor = CS

# comment in production
# Sensor = hooked_sensor_class(CS) measurments

line_sensors = tuple(provide_ev3_devices(Sensor, count=3, user='line sensor triplet'))

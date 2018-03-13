from ev3dev.ev3 import Sensor

SENSOR_COUNT = 8

class LineSensorArray(Sensor):
	def __init__(self, port, inverted=False):
		super(LineSensorArray, self).__init__(port)
		self.inverted = inverted

	def values(self):
		vals = [100 - self.value(i) for i in range(SENSOR_COUNT)]

		if self.inverted:
			return vals[::-1]

		return vals

	@property
	def line_pos(self):
		values = self.values()
		return (-3, -2, -1, 0, 0, 1, 2, 3)[values.index(max(values))]

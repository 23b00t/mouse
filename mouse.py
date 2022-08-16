#!/usr/bin/env python3
from pyudev import Context
import os
context = Context()
for device in context.list_devices(subsystem='input', ID_INPUT_MOUSE=True):
	if device.sys_name.startswith('event'):
		name = device.parent['NAME']
		#print(name)
		test = name.find('SHARKFORCE')
		if test != -1:
			os.system('synclient TouchpadOff=1')


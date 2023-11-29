### 06/16/2023 Notes (from Fisher)

-  For flight make sure you tape the SD card in place OR do something to secure it so that it does not "wiggle" out
- Glue the LED cover on OR take it off if you need to conserve weight
- On POWER UP
	- It takes 41 seconds to get good date and time data
	- It takes 258 seconds to get good GPS data
-  Temperature - when directly in the SUN the sensor reads really HOT (e.g., 100 deg F) when the ambient temp is around 70 deg F
- Version 12 of the flight code, I modified the serial comm baud rate between GPS and Teensy from 39400 to 38400
- It is recommended we remove GPS from board and switch to I2C communication between GPS and Teensy. This is to get the GPS antenna away from the Teensy I/O pins. 
	- This also requires upgrading to version 15 of the flight code

### 10/14/23  NEBP TX launch

- Data files exported. data stops mid launch.
- [ ] investigate the data stop #todo 
- Sensor data plots available [here](https://docs.google.com/presentation/d/1fL3OsHpcmTIaDc9tEFIUz38oztJMXeCRJYTw4ZYHEwU/edit#slide=id.p)

### Sep-Nov 2023

- Ran tests to see why the data was not correctly saved
- design report: [here](https://drive.google.com/file/d/1HJm21-mG5jri2jbTdC5BQTLqtb0IvBZx/view)
	- Source code is available as an appendix
- There is a blocking routine and if the SD card is not available during boot. (No RF data or SD data)
	- when correct operation there is a single blinking light on the board (identify led)
- after initial boot even if the card is yanked RF data is sent correctly
- RFD900: when link is connected there is a red led blinking (on both RF modules) They can be powered on at any order loose connection/re connection is fine 
- During the tests an omni-directional "ducky" was used on both ends

### 28/11/2023 

- Ran a test with RF and GPS.
	- GPS was locked
	- python and RF data was collected
- Temperature data may not be calibrated properly 
-  analog vs Digital sensors show huge deviations 
- Data available: `./Data/RFD900/`
-  Data is appending to the same file `PAYLOAD.CSV`
	- May be change the code so that it will make new files by the date of the launch.  (not critical)
	- For now old data is moved to `./old/` in the SD card after adding an index to the end of the file name
	- [ ] make a script to rename data files and move automatically #todo 
	- [ ] data export to video feed #todo #python
- GPS lock time: ~36 s (based off of past runs)
	
	![Pasted image 20231128205331](../Data/images/Pasted%20image%2020231128205331.png)
	
- Temperature data
	![Pasted image 20231128210817](../Data/images/Pasted%20image%2020231128210817.png)

### next update date

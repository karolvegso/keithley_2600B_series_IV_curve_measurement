# keithley_2600B_series_IV_curve_measurement
This program is measuring IV curve using Keithley 2600B source meter. 

This simple program uses the Keithley2600 module. It opens TCP/IP communication at a specific IP address. The program sweeps voltage, for example, from -1.0 Volt to +1.0 Volt with step +0.01 Volt and measures the corresponding electric current. After the IV curve measurement, the result is saved to a text file. 

from keithley2600 import Keithley2600
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import time

path_to_IV_curve_folder = 'd:/GIWAXS_measurements/2024/V4_Japan_project_PSK_QDs/IV_curve_Keithley_2612B/test_transile_diode/'
path_to_IV_curve = path_to_IV_curve_folder + 'IV_curve.txt'

# starting / initial volatge
voltage_start = -1.0 # [V]
# stop / final voltage
voltage_stop = 1.0 # [V]
# volatge step
voltage_step = 0.01 # [V]
# number of voltage steps
no_vol_steps = int((voltage_stop - voltage_start) / voltage_step) + 1
# wait time
wait_time = 1 # [s]
# initialize buffer numpyarray
buffer = np.zeros((2,no_vol_steps), dtype = float)

# initialize Keithley and connect to 20612B (two channels)
k = Keithley2600('TCPIP0::147.213.112.153::INSTR')
# switch on channel A
k.smua.source.output = k.smua.OUTPUT_ON
for index_0 in range(no_vol_steps):
    # calculate actual voltage
    voltage_actual = voltage_start + index_0 * voltage_step
    # set actual voltage
    k.smua.source.levelv = voltage_actual
    time.sleep(wait_time)
    # measure voltage
    v = k.smua.measure.v()
    time.sleep(wait_time)
    # measure electric current
    i = k.smua.measure.i()
    time.sleep(wait_time)
    print('Actual voltatge is: ', v)
    print('Eletric current is: ', i)
    # buffer - insert actual voltage value
    buffer[0, index_0] = v
    # buffer - insert actual electric curent value
    buffer[1, index_0] = i
    
# set actual voltage to 0 Volts
k.smua.source.levelv = 0
# switch OFF channel A
k.smua.source.output = k.smua.OUTPUT_OFF
# print final buffer with IV curve
print(buffer)
### plot result IV curve
##plt.plot(buffer[0,:], buffer[1,:], linestyle='dotted')
### add Title and axes labels
##plt.title("IV curve")
##plt.xlabel("Voltage in [V]")
##plt.ylabel("Electric current in [A]")
### display the plot
##plt.show()
# save result numpt array
np.savetxt(path_to_IV_curve, buffer.transpose(), delimiter='\t')

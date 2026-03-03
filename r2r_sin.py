import r2r_dac as r2r_mod
import signal_generator as sg
import time

amplitude = 3.2
signal_frequency = 10
sampling_frequency = 1000

dac = None

try:
    dac = r2r_mod.R2R_DAC()
    start = time.time()
    while True:
        current = time.time() - start
        norm_ampl = sg.get_sin_wave_amplitude(signal_frequency, current)
        voltage = norm_ampl * amplitude
        dac.set_voltage(voltage)
        sg.wait_for_sampling_period(sampling_frequency)
finally:
    if dac is not None:
        dac.deinit()        

            
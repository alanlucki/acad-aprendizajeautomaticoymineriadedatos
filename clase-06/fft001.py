import numpy as np
import matplotlib.pyplot as plotter

samplingFrequency   = 100.0;
samplingInterval    = 1 / samplingFrequency; # At what intervals time points are sampled
beginTime           = 0;        # Begin time period of the signals
endTime             = 10.0;      # End time period of the signals

signal1Frequency     = 4.0;   # Frequency of the signals
signal2Frequency     = 7.0;

time        = np.arange(beginTime, endTime, samplingInterval); # Time points

amplitude1 = np.sin(2*np.pi*signal1Frequency*time) # Create two sine waves
amplitude2 = np.sin(2*np.pi*signal2Frequency*time)

figure, axis = plotter.subplots(4, 1)  # Create subplot
plotter.subplots_adjust(hspace=1)

# Time domain representation for sine wave 1
axis[0].set_title('Sine wave with a frequency of 4 Hz')
axis[0].plot(time, amplitude1)
axis[0].set_xlabel('Time')
axis[0].set_ylabel('Amplitude')

# Time domain representation for sine wave 2
axis[1].set_title('Sine wave with a frequency of 7 Hz')
axis[1].plot(time, amplitude2)
axis[1].set_xlabel('Time')
axis[1].set_ylabel('Amplitude')

amplitude = amplitude1 + amplitude2  # Add the sine waves

# Time domain representation of the resultant sine wave
axis[2].set_title('Sine wave with multiple frequencies')
axis[2].plot(time, amplitude)
axis[2].set_xlabel('Time')
axis[2].set_ylabel('Amplitude')

# Frequency domain representation
fourierTransform = np.fft.fft(amplitude)/len(amplitude)           # Normalize amplitude

fourierTransform = fourierTransform[range(int(len(amplitude)/2))] # Exclude sampling frequency

tpCount     = len(amplitude)
values      = np.arange(int(tpCount/2))
timePeriod  = tpCount/samplingFrequency
frequencies = values/timePeriod

# Frequency domain representation
axis[3].set_title('Fourier transform depicting the frequency components')
axis[3].plot(frequencies, abs(fourierTransform))
axis[3].set_xlabel('Frequency')
axis[3].set_ylabel('Amplitude')

plotter.show()
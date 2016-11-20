# -*- coding: utf-8 -*-
"""
Created on Fri Nov 18 13:09:53 2016

@author: Shivam B. Waghela, Akshdeep Rungta, Anuj Singh, Siddharth Vyas
"""
############################################################################
#																		   #
#			         Musical Note Identification				           #
#																		   #
############################################################################

import numpy as np
import wave
import struct

############################## Initialize ##################################
# Some Useful Variables
window_size = 1000#2205  # Size of window to be used for detecting silence
sampling_freq = 44100  # Sampling frequency of audio signal

############################# Implementation ###############################
def play(sound_file):
    '''
    sound_file-- a single test audio_file as input argument

    '''
    # Reading Audio

    print('\n\nReading Audio File...')
    file_length = sound_file.getnframes()
    sound = np.zeros(file_length)  # Return a new array of given shape and type, filled with zeros
    for i in range(file_length):
        data = sound_file.readframes(1)  # Reads and returns at most n frames of audio, as a bytes object
        data = struct.unpack("<h", data)
        sound[i] = int(data[0])
    sound = np.divide(sound, float(2 ** 15))  # Normalize data in range -1 to 1

    # squaring(window_size) -> mean
    mean_squared_list = []
    counter = 0
    result = 0
    for i in range(file_length):
        counter += 1
        result += sound[i] ** 2
        if (counter > window_size):
            result /= window_size
            mean_squared_list.append(result)
            counter = 0
            result = 0

    temp = mean_squared_list[0]
    times = 0
    silence = []
    for i in range(1, len(mean_squared_list)):
        if mean_squared_list[i] < 0.1:  # detect silence
            silence.append(i)  # store the index of window of silence

    start = 0
    i = 0
    notes_freq = []
    exi = 0
    # loop
    for iterator in range(len(silence)):
        end = silence[i] * window_size
        fourier = np.fft.fft(sound[start:end])
        freqs = np.fft.fftfreq(len(fourier))
        idx = np.argmax(np.abs(fourier))
        freq = freqs[idx]
        frate = sound_file.getframerate()
        freq_in_hertz = abs(freq * frate)

        notes_freq.append(freq_in_hertz)

        while True:
            if (len(silence) - 1 != i and i < len(silence)):
                if silence[i + 1] != silence[i] + 1:  # adjacent window not silent
                    start = (silence[i] + 1) * window_size
                    i += 1
                    break
                else:  # if adjacent is also silence
                    i += 1
            else:
                exi = 1
                break
        if (exi == 1):
            break

    # Identify notes from frequency
    L = [("A0", 27.50), ("A1", 55.00), ("A2", 110.00), ("A3", 220.00), ("A4", 440.00), ("A5", 880.00), ("A6", 1760.00),
         ("A7", 3520.00), ("A8", 7040.00), ("B0", 30.87), ("B1", 61.74), ("B2", 123.47), ("B3", 246.94), ("B4", 493.88),
         ("B5", 987.77), ("B6", 1975.53), ("B7", 3951.07), ("B8", 7902.13), ("C0", 16.35), ("C1", 32.70), ("C2", 65.41),
         ("C3", 130.81), ("C4", 261.63), ("C5", 523.25), ("C6", 1046.50), ("C7", 2093.00), ("C8", 4186.01),
         ("D0", 18.35), ("D1", 36.71), ("D2", 73.42), ("D3", 146.83), ("D4", 293.66), ("D5", 587.33), ("D6", 1174.66),
         ("D7", 2349.32),("D8", 4698.63), ("E0", 20.60), ("E1", 41.20), ("E2", 82.41), ("E3", 164.81), ("E4", 329.63),
         ("E5", 659.25), ("E6", 1318.51), ("E7", 2637.02), ("E8", 5274.04), ("F0", 21.83), ("F1", 43.65), ("F2", 87.31),
         ("F3", 174.61), ("F4", 349.23), ("F5", 698.46), ("F6", 1396.91), ("F7", 2793.83),("F8", 5587.65), ("G0", 24.50),
         ("G1", 49.00), ("G2", 98.00), ("G3", 196.00), ("G4", 392.00), ("G5", 783.99), ("G6", 1567.98), ("G7", 3135.96),
         ("G8", 6271.93)]

    Identified_Notes = []
    freq = [x[1] for x in L]
    note_name = [x[0] for x in L]
    for i in range(len(notes_freq)):
        for j in range(len(freq)):
            if abs(freq[j] - notes_freq[i]) < 5:
                Identified_Notes.append(note_name[j])

    return Identified_Notes


############################## Testing Audio File #############################
if __name__ == "__main__":
    #code for checking output for all audio
    for file_number in range(1,6):
        Identified_Notes = []
        file_name = "Test_Audio_files/New_Audio_files/Audio_"+str(file_number)+".wav"
        sound_file = wave.open(file_name)
        Identified_Notes = play(sound_file)
        #Identified_Notes_list.append(Identified_Notes)
        print("Notes = ", Identified_Notes)
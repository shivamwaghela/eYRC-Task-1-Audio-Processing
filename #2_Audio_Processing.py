# -*- coding: utf-8 -*-
"""
Created on Fri Nov 18 13:09:53 2016

@author: Shivam B. Waghela, Akshdeep Rungta, Anuj Singh, Siddharth Vyas
"""
############################################################################
#																		   #
#			Musical Note Identification							           #
#																		   #
#######  #####################################################################

import numpy as np
import wave
import struct

# Teams can add other helper functions
# which can be added here


############################## Initialize ##################################

# Some Useful Variables
window_size = 2205  # Size of window to be used for detecting silence
beta = 1  # Silence detection parameter
max_notes = 100  # Maximum number of notes in file, for efficiency
sampling_freq = 44100  # Sampling frequency of audio signal


############################## Implementation ##############################

def play(sound_file):
    '''
    sound_file-- a single test audio_file as input argument

    '''

    return Identified_Notes


############################## Testing Audio File #############################

if __name__ == "__main__":
    # code for checking output for single audio file
    sound_file = wave.open('Test_Audio_files/Audio_1.wav', 'r')
    Identified_Notes = play(sound_file)
    print("Notes = ", Identified_Notes)

    # code for checking output for all images
    Identified_Notes_list = []
    for file_number in range(1, 6):
        file_name = "Test_Audio_files/Audio_" + str(file_number) + ".wav"
        sound_file = wave.open(file_name)
        Identified_Notes = play(sound_file)
        Identified_Notes_list.append(Identified_Notes)
    print(Identified_Notes)


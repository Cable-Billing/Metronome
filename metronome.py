#!/bin/python

import argparse
import time

parser = argparse.ArgumentParser(description='Metronome Application')
parser.add_argument('--beats', type=int, default=4, help='The number of beats per bar')
parser.add_argument('--tempo', type=int, default=60, help='The number of beats per minute')

args = parser.parse_args()
beats = args.beats
tempo = args.tempo

colourList = ['blue', 'red', 'yellow']

beatInterval = float(60) / float(tempo)
i = 1
while True:
    time.sleep(beatInterval)
    print(i)
    i += 1
    if i > beats:
        i = 1

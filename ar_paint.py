#!/usr/bin/env python3
# --------------------------------------------------
# André Cabaço
# PSR, 2022.
# --------------------------------------------------
from copy import deepcopy
from email.policy import default

import numpy as np
import cv2
import sys
import argparse
from colorama import Fore, Style
import json





def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-j','--json',help='Full path to json file.', type=argparse.FileType('r'))
    args = parser.parse_args()

    with args.json as file:
        limits=json.load(file)
        # print(limits)
    limits_dict=limits['limits_dict']

    lvlmax = np.array([limits_dict['B']['max'], limits_dict['G']['max'], limits_dict['R']['max']])
    lvlmin = np.array([limits_dict['B']['min'], limits_dict['G']['min'], limits_dict['R']['min']])
    vid = cv2.VideoCapture(0)
    window_name = 'Original'
    window_name2 = 'Segmented'
    cv2.namedWindow(window_name,cv2.WINDOW_NORMAL)
    cv2.resizeWindow(window_name, 800, 400)
    cv2.namedWindow(window_name2,cv2.WINDOW_NORMAL)
    cv2.resizeWindow(window_name2, 800, 400)

    # display the image using opencv
    while True:
        
        retval, frame = vid.read()
        flip_video = cv2.flip(frame, 1)
        cv2.imshow(window_name, flip_video)

        mask_frame = cv2.inRange(frame, lvlmin, lvlmax)
        flip_video2 = cv2.flip(mask_frame, 1)
        cv2.imshow(window_name2, flip_video2)
        # Capture the video frame
        # by frame
        ret, frame = vid.read()

        # Display the resulting frame
        new_frame = cv2.flip(frame,1)
        cv2.imshow(window_name, new_frame)
        #dimensions = new_frame.shape
        img = np.ones((400, 800, 3), dtype = np.uint8)
        img = 255* img

        #   display the image using opencv
        cv2.imshow('white image', img)

        

        pressed_key = cv2.waitKey(30)

        if pressed_key == -1:
            pass
        elif chr(pressed_key) == 'q':  # Quite the program
            exit(0)







if __name__ == '__main__':
    main()
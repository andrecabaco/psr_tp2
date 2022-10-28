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






def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-j','--json',help='Full path to json file.', type=argparse.FileType('r'))
    args = parser.parse_args()

    with args.json as file:
        limits=file.read()
        print(limits)

    vid = cv2.VideoCapture(0)
    window_name = 'TP2'
    cv2.namedWindow(window_name,cv2.WINDOW_NORMAL)
    cv2.resizeWindow(window_name, 800, 400)
   
    

    # display the image using opencv
    while True:

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
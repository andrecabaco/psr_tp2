#!/usr/bin/env python3
import cv2
import numpy as np
from copy import deepcopy
import array
import json
from pprint import pprint

def detectcolor():
    pass

def trackbars(x):
    print(x)

def main():

    vid = cv2.VideoCapture(0)
    window_name = "Original"
    window_name2 = "Segmented"

    cv2.namedWindow(window_name, cv2.WINDOW_AUTOSIZE)
    cv2.namedWindow(window_name2, cv2.WINDOW_AUTOSIZE)

    cv2.createTrackbar("Max B", window_name2, 0, 255, trackbars)
    cv2.createTrackbar("Min B", window_name2, 0, 255, trackbars)
    cv2.createTrackbar("Max G", window_name2, 0, 255, trackbars)
    cv2.createTrackbar("Min G", window_name2, 0, 255, trackbars)
    cv2.createTrackbar("Max R", window_name2, 0, 255, trackbars)
    cv2.createTrackbar("Min R", window_name2, 0, 255, trackbars)


    while True:

        lvl1 = cv2.getTrackbarPos("Max B", window_name2)
        lvl2 = cv2.getTrackbarPos("Min B", window_name2)
        lvl3 = cv2.getTrackbarPos("Max G", window_name2)
        lvl4 = cv2.getTrackbarPos("Min G", window_name2)
        lvl5 = cv2.getTrackbarPos("Max R", window_name2)
        lvl6 = cv2.getTrackbarPos("Min R", window_name2)

        limit_dict = {'B': {'max': lvl1, 'min': lvl2},
            'G': {'max': lvl3, 'min': lvl4},
            'R': {'max': lvl5, 'min': lvl6}}
        
        lvlmax = np.array([limit_dict['B']['max'], limit_dict['G']['max'], limit_dict['R']['max']])
        lvlmin = np.array([limit_dict['B']['min'], limit_dict['G']['min'], limit_dict['R']['min']])

        retval, frame = vid.read()
        flip_video = cv2.flip(frame, 1)
        cv2.imshow(window_name, flip_video)

        mask_frame = cv2.inRange(frame, lvlmin, lvlmax)
        flip_video2 = cv2.flip(mask_frame, 1)
        cv2.imshow(window_name2, flip_video2)

        pressed_key = cv2.waitKey(1)

        if pressed_key == ord('q'):
            break

        elif pressed_key == ord('w'):
            file_name = 'limits.json'
            with open(file_name, 'w') as file_handle:
                json.dump(limit_dict, file_handle) # d is the dicionary
            pprint(limit_dict)
            break

    vid.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
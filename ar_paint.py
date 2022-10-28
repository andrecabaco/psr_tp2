#!/usr/bin/env python3

import cv2
import argparse 
import json

#Definição de Argumentos/help menu
parser = argparse.ArgumentParser(description="Definition of test mode")

parser.add_argument("-j", "--json", help="Full path to json file.", type=str, required=True)
parser.add_argument("-usp", "--use_shake_prevention", help="Shake prevention.", action="store_true", default=False)
parser.add_argument("-uvs", "--use_video_stream", help="Use video stream as canvas.", action="store_true", default=False)                        
args = parser.parse_args()

#use_shake_prevention = args.use_shake_prevention
# use_video_stream = args.use_video_stream

def normal_mode():

    print("Normal mode in execution...")

    jsonfile = open('limits.json', 'r')
    data = jsonfile.read()
    print(data)

    vid = cv2.VideoCapture(0)
    window_name = "Orignal"
    window_name2 = "Segmented"
    window_name3 = "Mask Largest component"
    window_name4 = "Canvas"
    blank_image = cv2.imread("/home/nunoc99/Desktop/MEAI/PSR/Parte_07/White-400x600px2-600x400-21732.png", cv2.IMREAD_COLOR)

    cv2.namedWindow(window_name, cv2.WINDOW_AUTOSIZE)
    cv2.namedWindow(window_name2, cv2.WINDOW_AUTOSIZE)
    cv2.namedWindow(window_name3, cv2.WINDOW_AUTOSIZE)
    cv2.namedWindow(window_name4, cv2.WINDOW_AUTOSIZE)

    while True:

        retval, frame = vid.read() 
        flip_video = cv2.flip(frame, 1)
        cv2.imshow(window_name, flip_video)

        cv2.imshow(window_name2, flip_video)
        cv2.imshow(window_name3, flip_video)
        cv2.imshow(window_name4, blank_image)

        pressed_key = cv2.waitKey(1)

        if pressed_key == ord('q'):
            break

    vid.release()
    cv2.destroyAllWindows()

def usp_mode():
    print("Use shake prevention mode in execution...")

def uvs_mode():
    print("Use video stream drawing mode in execution...")

def main():

    if args.json != None and args.use_shake_prevention != True:
        normal_mode()
    elif args.json != None and args.use_shake_prevention != False:
        usp_mode()
    elif args.json != None and args.use_video_stream != False:
        uvs_mode()
    else:
        print("Define your arguments correctly or type -h to display the HELP menu.")


if __name__ == "__main__":
    main()
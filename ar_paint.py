#!/usr/bin/env python3

from tokenize import blank_re
import cv2
import argparse 
import json
import numpy as np
from colorama import Fore, Style
from copy import deepcopy

#Definição de Argumentos/help menu
parser = argparse.ArgumentParser(description="Definition of test mode")

parser.add_argument('-j','--json',help='Full path to json file.',required=True, type=argparse.FileType('r'))
parser.add_argument("-usp", "--use_shake_prevention", help="Shake prevention.", action="store_true", default=False)
parser.add_argument("-uvs", "--use_video_stream", help="Use video stream as canvas.", action="store_true", default=False)                        
args = parser.parse_args()

#use_shake_prevention = args.use_shake_prevention
# use_video_stream = args.use_video_stream

def selectbiggestComponents(image):
    connectivity=8
    nLabels, output, stats, centroids = cv2.connectedComponentsWithStats(image, connectivity,cv2.CV_32S)
    sizes = stats[1:, -1]
    nLabels = nLabels - 1
    x = None
    y = None
    final_image = np.zeros(output.shape, dtype=np.uint8)
    largest_component=0

    for k in range(0, nLabels):
        if sizes[k] >= largest_component:
            
            x, y = centroids[k + 1]
            largest_component = sizes[k]
            final_image[output == k + 1] = 255

    return (final_image, x, y)

def normal_mode():

    print("Normal mode in execution...")

    with args.json as file:
        limits=json.load(file)
        # print(limits)
    limits_dict=limits['limits_dict']

    lvlmax = np.array([limits_dict['B']['max'], limits_dict['G']['max'], limits_dict['R']['max']])
    lvlmin = np.array([limits_dict['B']['min'], limits_dict['G']['min'], limits_dict['R']['min']])

    vid = cv2.VideoCapture(0)
    window_name = "Orignal"
    window_name2 = "Segmented"
    window_name3 = "Mask Largest component"
    window_name4 = "Canvas"
    blank_image = np.zeros((480, 640, 3)) + 255
    #blank_image = cv2.imread("white_image.png", cv2.IMREAD_COLOR)
    thickness=3
    clr=(0,255,255)
    lapis=5
    centroides=[]


    cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
    cv2.namedWindow(window_name2, cv2.WINDOW_NORMAL)
    cv2.namedWindow(window_name3, cv2.WINDOW_NORMAL)
    cv2.namedWindow(window_name4, cv2.WINDOW_NORMAL)

    while True:

        retval, frame = vid.read() 

        # blank_image = np.ones((original_dimensions[0], original_dimensions[1], 3), dtype = np.uint8)
        # blank_image = 255* blank_image
        # flip_video = cv2.flip(frame, 1)
        

        #display masked resulting frame
        mask_frame = cv2.inRange(frame, lvlmin, lvlmax)
        flip_video2 = cv2.flip(mask_frame, 1)
        cv2.imshow(window_name2, flip_video2)

        #mask largest component result frame
        mask_largest = selectbiggestComponents(mask_frame)
        flip_video3 = cv2.flip(mask_largest[0], 1)
        cv2.imshow(window_name3, flip_video3)
        x=mask_largest[1]
        y=mask_largest[2]
        centroide=(int(x),int(y)) 
        centroides.append(centroide)
        k=centroides.index(centroide)
        start_point=centroides[k-1]
        end_point=centroides[k]


        #painting de mask largest component on original image
        frame_copy=np.copy(frame)
        frame_copy[mask_largest[0]==255]=(0,255,0)
        
        #adição da cruz na imagem original
        cv2.line(frame_copy, (int(x) - 5,int(y)), (int(x) + 5, int(y)), (0, 0, 255), 3)
        cv2.line(frame_copy, (int(x), int(y) + 5), (int(x), int(y) - 5), (0, 0, 255), 3)

        flip_video4 = cv2.flip(frame_copy, 1)
        cv2.imshow(window_name, flip_video4)


        #desenhar na tela branca.
        cv2.line(blank_image, start_point, end_point, clr, thickness)
        flip_video5=cv2.flip(blank_image, 1)
        cv2.imshow(window_name4, flip_video5)

        pressed_key = cv2.waitKey(1)

        if pressed_key == ord('q'):
            break
        elif pressed_key == ord('w'): # save drawing
            cv2.imwrite("/home/nunoc99/Desktop/MEAI/PSR/Git_Work/psr_tp2", flip_video5)

        elif pressed_key == ord('c'): # clean the canvas
            flip_video5 = deepcopy(blank_image)
            print("The canvas is clean.")
            pass

        elif pressed_key == ord('r'): # change color to red
            clr = (0,0,255)
            print("Color changed to" + Fore.RED + "RED" + Style.RESET_ALL)

        elif pressed_key == ord('g'): # change color to green
            clr = (0,255,0)
            print("Color changed to" + Fore.GREEN + "GREEN" + Style.RESET_ALL)

        elif pressed_key == ord('b'): # change color to blue
            clr = (255,0,0)
            print("Color changed to" + Fore.BLUE + "BLUE" + Style.RESET_ALL)

        elif pressed_key == ord('+'): # increase pencil line size
            pass

        elif pressed_key == ord('-'): # decrease pencil line sizw
            pass

        
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
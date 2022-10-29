#!/usr/bin/env python3

from tokenize import blank_re
import cv2
import argparse 
import json
import numpy as np

#Definição de Argumentos/help menu
parser = argparse.ArgumentParser(description="Definition of test mode")

parser.add_argument("-j", "--json", help="Full path to json file.", type=str, required=True)
parser.add_argument("-usp", "--use_shake_prevention", help="Shake prevention.", action="store_true", default=False)
parser.add_argument("-uvs", "--use_video_stream", help="Use video stream as canvas.", action="store_true", default=False)                        
args = parser.parse_args()

#use_shake_prevention = args.use_shake_prevention
# use_video_stream = args.use_video_stream

def selectbiggestComponents(image):
    connectivity=8
    nLabels, output, stats, centroids = cv2.connectedComponentsWithStats(image, connectivity,cv2.CV_32S)
    final_image = np.zeros(output.shape, dtype=np.uint8)
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
    #blank_image = cv2.imread("white_image.png", cv2.IMREAD_COLOR)



    cv2.namedWindow(window_name, cv2.WINDOW_AUTOSIZE)
    cv2.namedWindow(window_name2, cv2.WINDOW_AUTOSIZE)
    cv2.namedWindow(window_name3, cv2.WINDOW_AUTOSIZE)
    #cv2.namedWindow(window_name4, cv2.WINDOW_AUTOSIZE)

    while True:

        retval, frame = vid.read() 

        original_dimensions = frame.shape


        blank_image = np.ones((original_dimensions[0], original_dimensions[1], 3), dtype = np.uint8)
        blank_image = 255* blank_image

        cv2.namedWindow(window_name4, cv2.WINDOW_AUTOSIZE)



        flip_video = cv2.flip(frame, 1)
        cv2.imshow(window_name, flip_video)

        #display masked resulting frame
        mask_frame = cv2.inRange(frame, lvlmin, lvlmax)
        flip_video2 = cv2.flip(mask_frame, 1)
        cv2.imshow(window_name2, flip_video2)
        #mask largest component result frame
        
        mask_largest = selectbiggestComponents(mask_frame)
        flip_video3 = cv2.flip(mask_largest[0], 1)
        cv2.imshow(window_name3, flip_video3)
        
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
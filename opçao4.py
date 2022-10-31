#!/usr/bin/env python3
import math
from random import random
import cv2
import sys
import argparse
import random
import numpy as np

def posInt(s: str) -> int:          
    
    try:
        v = int(s)
    except ValueError:
        raise argparse.ArgumentTypeError(f'expected integer, got {s!r}')
    if v <= 0:
        raise argparse.ArgumentTypeError(f'expected positive integer, got {v}')
    return v

parser=argparse.ArgumentParser(
    description = '''Definition of test mode ''') 
parser.add_argument('-rdm', '--random_division_mode', action='store_true', 
    help = " division of screen")
parser.add_argument('-mv', '--max_value',nargs='?', const=10, type=posInt, required=True,
    help = " Input number of divisions.")
if len(sys.argv) == 1:
    parser.print_help(sys.stderr)
    sys.exit(1)
args = parser.parse_args()  

def dist(x,y):
    x1=x[0]-y[0]
    y1=x[1]-y[1]

    distancia=round(math.sqrt((x1**2)+(y1**2)),3)
    return distancia


def main():

    window_name = "Orignal"
    blank_image = np.zeros((480, 640, 3))
    blank_image.fill(255)
    cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
    points=args.max_value
    coordenadas=[]
    distancias=[]
    dist_init=10000
    color=(0,0,0)
    thickness=10

    for k in range(1,points+1):
        x=random.randint(0,640)
        y=random.randint(0,480)
        coordenada=(x,y)
        coordenadas.append(coordenada)
        
        if k==1:
            pass
        else:
            distancia=dist(coordenadas[k-1],coordenadas[k-2])
            distancias.append(distancia)

    while len(distancias)>0:
        for i in range (0,len(distancias)):
            if distancias[i]<=dist_init:
                dist_init=distancias[i]

        j=distancias.index(dist_init)
        
        
        cv2.line(blank_image, coordenadas[j], coordenadas[j-1], color, thickness)
        cv2.imshow(window_name, blank_image)
        
        distancias.remove(dist_init)
        
    
    

    
    window_name2 = "painted"
    cv2.namedWindow(window_name2, cv2.WINDOW_NORMAL)

    while True:
        

        
        pressed_key = cv2.waitKey(1)

        if pressed_key == ord('q'):
            break

    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
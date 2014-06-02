import pygame
import sys
import random
import copy
from random import randint
from pygame.locals import *
pygame.init()
#mainclock= pygame.time.Clock()
width = 960  # 1920 = full
height = 540 # 1080 = full
tilesize = 10 # 10
tileborder = 1 # 1
window=pygame.display.set_mode((width,height,),FULLSCREEN,32)
#window=pygame.display.set_mode((width,height,),0,32)
#pygame.display.set_caption('Grasslands')
game = True

pygame.mouse.set_visible(0)
W=(255,255,255)
BL=(0,0,0)
GR=(20,20,20)
R=(255,0,0) # red = 255,0,0
G=(0,255,0) # green = 0,255,0
B=(0,0,255) # blue = 0,0,255
P=(100,100,100)

fire = []


i = 0
ii = 0
grid = []

while i < width/tilesize:
    row = []
    grid.append(row)
    i += 1
    
gridcolor = copy.deepcopy(grid)
gridobjects = copy.deepcopy(grid)




i=0
ii=0
while i < width/tilesize:
    grid[i].append(pygame.Rect(i*tilesize,ii*tilesize,tilesize-tileborder,tilesize-tileborder))
    gridcolor[i].append(BL)
    gridobjects[i].append("grass")
    # 0 = blue
    # 1 = red
    # 2 = black
    #
    ii += 1
    print(ii)
            
    if ii >= height/tilesize:
        ii = 0
        i += 1
        print(i)


        
while True:
    while game == True:
      
        window.fill (BL)
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
            if event.type== KEYDOWN:
                if event.key== ord('f'):
                    gridobjects[randint(1,(width/tilesize)-1)][randint(1,(height/tilesize)-1)] = "spark"
                    print("spark")
                  
                if event.key== ord('g'):
                    gridobjects[randint(1,(width/tilesize)-1)][randint(1,(height/tilesize)-1)] = "seed"
                    print("seed")
                    
                if event.key==ord('h'):
                    gridobjects[randint(1,(width/tilesize)-1)][randint(1,(height/tilesize)-1)] = "royal"
                    print("royal")
                    
                if event.key==ord('j'):
                    gridobjects[randint(1,(width/tilesize)-1)][randint(1,(height/tilesize)-1)] = "gold"
                    print("gold")
                    
                if event.key==ord('k'):
                    gridobjects[randint(1,(width/tilesize)-1)][randint(1,(height/tilesize)-1)] = "water"
                    print("water")
                    
                if event.key == ord('w'):
                    pygame.quit()
                    sys.exit()
               
                
            #if event.type==KEYUP:
                #if event.key== ord('s'):
                    #i = 0
        i = 0
        for list in grid:
            ii = 0
            for z in list:
                pygame.draw.rect(window,gridcolor[i][ii],z)
                ii+=1
            i+=1


        i=0
        for list in gridobjects:
            ii = 0
            for z in list:
                
                if z == "burnt":
                    gridcolor[i][ii] = BL
                    
                elif z == "royal":
                    gridcolor[i][ii] = [128,50,128]
                    gridobjects[i][ii] = "purple"

                elif z == "purple":
                    gridcolor[i][ii] = [128,0,128]
                    if i+1 < (width/tilesize) and ii+1 < (height/tilesize) and gridobjects[i+1][ii+1] == "burnt":
                        gridobjects[i+1][ii+1] = "royal"
                    if ii+1 < (height/tilesize) and i-1 > -1 and gridobjects[i-1][ii+1] == "burnt":
                        gridobjects[i-1][ii+1] = "royal"                       
                    if ii-1 > -1 and i+1 < (width/tilesize) and gridobjects[i+1][ii-1] == "burnt":
                        gridobjects[i+1][ii-1] = "royal"
                    if ii-1 > -1 and i-1 > -1 and gridobjects[i-1][ii-1] == "burnt":
                        gridobjects[i-1][ii-1] = "royal"

                elif z == "gold":
                    gridcolor[i][ii] = [255, 255, 0]
                    gridobjects[i][ii] = "yellow"

                elif z == "yellow":
                    gridcolor[i][ii] = [255, 215, 0]
                    if i+2 < (width/tilesize) and ii+2 < (height/tilesize) and gridobjects[i+2][ii+2] == "burnt":
                        gridobjects[i+2][ii+2] = "gold"
                    if ii+2 < (height/tilesize) and i-2 > -1 and gridobjects[i-2][ii+2] == "burnt":
                        gridobjects[i-2][ii+2] = "gold"                       
                    if ii-2 > -1 and i+2 < (width/tilesize) and gridobjects[i+2][ii-2] == "burnt":
                        gridobjects[i+2][ii-2] = "gold"
                    if ii-2 > -1 and i-2 > -1 and gridobjects[i-2][ii-2] == "burnt":
                        gridobjects[i-2][ii-2] = "gold"

                        
                elif z == "seed":
                    gridcolor[i][ii] = [50,255,50]
                    gridobjects[i][ii] = "short grass"
                elif z == "short grass":
                    gridcolor[i][ii] = [10,255,10]
                    gridobjects[i][ii] = "grass"
                elif z == "grass":
                    gridcolor[i][ii] = G
                    gridobjects[i][ii] = "tall grass"
                    
                elif z == "tall grass":
                    gridcolor[i][ii] = [0,180,0]
                    if i+1 < (width/tilesize) and (gridobjects[i+1][ii] == "burnt" or gridobjects[i+1][ii] == "purple" or gridobjects[i+1][ii] == "yellow"):
                        gridobjects[i+1][ii] = "seed"
                    if ii+1 < (height/tilesize) and (gridobjects[i][ii+1] == "burnt" or gridobjects[i][ii+1] == "purple" or gridobjects[i][ii+1] == "yellow"):
                        gridobjects[i][ii+1] = "seed"                       
                    if i-1 > -1 and (gridobjects[i-1][ii] == "burnt" or gridobjects[i-1][ii] == "purple" or gridobjects[i-1][ii] == "yellow"):
                        gridobjects[i-1][ii] = "seed"
                    if ii-1 > -1 and (gridobjects[i][ii-1] == "burnt" or gridobjects[i][ii-1] == "purple" or gridobjects[i][ii-1] == "yellow" ):
                        gridobjects[i][ii-1] = "seed"
                        
                elif z == "spark":
                    gridcolor[i][ii] = R
                    gridobjects[i][ii] = "fire"
                    
                elif z == "fire":
                    gridobjects[i][ii] = "burnt"
                    gridcolor[i][ii] = R
                    
                    if i+1 < (width/tilesize) and (gridobjects[i+1][ii] == "tall grass" or gridobjects[i+1][ii] == "purple" or gridobjects[i+1][ii] == "purple"):
                        gridobjects[i+1][ii] = "spark"
                    if ii+1 < (height/tilesize) and (gridobjects[i][ii+1] == "tall grass" or gridobjects[i][ii+1] == "purple" or gridobjects[i][ii+1] == "purple"):
                        gridobjects[i][ii+1] = "spark"                       
                    if i-1 > -1 and (gridobjects[i-1][ii] == "tall grass" or gridobjects[i-1][ii] == "purple" or gridobjects[i-1][ii] == "purple"):
                        gridobjects[i-1][ii] = "spark"
                    if ii-1 > -1 and (gridobjects[i][ii-1] == "tall grass" or gridobjects[i][ii-1] == "purple" or gridobjects[i][ii-1] == "purple"):
                        gridobjects[i][ii-1] = "spark"

                elif z == "water":
                    gridcolor[i][ii] = B
                    gridobjects[i][ii] = "blue"

                elif z == "blue":
                    gridobjects[i][ii] = "flood"
                    gridcolor[i][ii] = B
                    
                    if i+1 < (width/tilesize) and (gridobjects[i+1][ii] == "tall grass" or gridobjects[i+1][ii] == "purple" or gridobjects[i+1][ii] == "yellow"):
                        gridobjects[i+1][ii] = "water"
                    if ii+1 < (height/tilesize) and (gridobjects[i][ii+1] == "tall grass" or gridobjects[i][ii+1] == "purple" or gridobjects[i][ii+1] == "yellow"):
                        gridobjects[i][ii+1] = "water"                       
                    if i-1 > -1 and (gridobjects[i-1][ii] == "tall grass" or gridobjects[i-1][ii] == "purple" or gridobjects[i-1][ii] == "yellow"):
                        gridobjects[i-1][ii] = "water"
                    if ii-1 > -1 and (gridobjects[i][ii-1] == "tall grass" or gridobjects[i][ii-1] == "purple" or gridobjects[i][ii-1] == "yellow"):
                        gridobjects[i][ii-1] = "water"

                elif z == "flood":
                    gridcolor[i][ii] = B
                    gridobjects[i][ii] = "burnt"


                    
                ii+=1
            i+=1
        
        #mainclock.tick(80)###default = 80
        pygame.display.update()
       











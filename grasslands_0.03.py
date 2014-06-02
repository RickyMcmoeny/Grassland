import pygame
import sys
import random
import copy
from math import pow, sqrt
from random import randint
from pygame.locals import *
pygame.init()
#mainclock= pygame.time.Clock()
width = 960  # 1920 = full | 960 = half
height = 540 # 1080 = full | 540 = half
tilesize = 10 # 10
tileborder = 1 # 1
window=pygame.display.set_mode((width,height,),FULLSCREEN,32)
#window=pygame.display.set_mode((width,height,),0,32)
pygame.display.set_caption('Grasslands')
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

weather = 0


i = 0
ii = 0
grid = []

while i < width/tilesize:
    row = []
    grid.append(row)
    i += 1
    
gridcolor = copy.deepcopy(grid)
gridobjects = copy.deepcopy(grid)
gridwater = copy.deepcopy(grid)

cows = [] #the amazing unisex cow
# [x, y, destination x, destinatoin y, food]




i=0
ii=0
while i < width/tilesize:
    grid[i].append(pygame.Rect(i*tilesize,ii*tilesize,tilesize-tileborder,tilesize-tileborder))
    gridcolor[i].append(BL)
    gridobjects[i].append("grass")
    gridwater[i].append(300)
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
                if event.key== ord('a'):
                    cowX = randint(1,(width/tilesize)-1)
                    cowY = randint(1,(height/tilesize)-1)
                    cows.append([cowX, cowY, cowX, cowY, 100])
                    print("Cow")
                    
                if event.key== ord('v'):
                    weather = 300
                    print("weather: ")
                    print(weather)
                    
                if event.key== ord('x'):
                    weather = 0
                    print("weather: ")
                    print(weather)

                if event.key== ord('c'):
                    weather = 100
                    print("weather: ")
                    print(weather)
                    
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
                    if(gridwater[i][ii] > 50):
                        gridobjects[i][ii] = "earth"

                elif z == "earth":
                    gridcolor[i][ii] = [70,33,10]
                    

                elif z == "seed":
                    gridcolor[i][ii] = [50,255,50]
                    if gridwater[i][ii] >= 50:
                        gridobjects[i][ii] = "short grass"
                        gridwater[i][ii] -= 50
                        
                elif z == "short grass":
                    gridcolor[i][ii] = [10,255,10]
                    if gridwater[i][ii] >= 80:
                        gridobjects[i][ii] = "grass"
                        gridwater[i][ii] -= 80
                        
                elif z == "grass":
                    gridcolor[i][ii] = G
                    if gridwater[i][ii] >= 1000:
                        gridobjects[i][ii] = "tall grass"
                        gridwater[i][ii] -= 1000
                    
                elif z == "tall grass":
                    gridcolor[i][ii] = [0,180,0]
                    if gridwater[i][ii] >= 150:
                        if i+1 < (width/tilesize) and (gridobjects[i+1][ii] == "earth" or gridobjects[i+1][ii] == "purple" or gridobjects[i+1][ii] == "yellow"):
                            gridobjects[i+1][ii] = "seed"
                        if ii+1 < (height/tilesize) and (gridobjects[i][ii+1] == "earth" or gridobjects[i][ii+1] == "purple" or gridobjects[i][ii+1] == "yellow"):
                            gridobjects[i][ii+1] = "seed"                       
                        if i-1 > -1 and (gridobjects[i-1][ii] == "earth" or gridobjects[i-1][ii] == "purple" or gridobjects[i-1][ii] == "yellow"):
                            gridobjects[i-1][ii] = "seed"
                        if ii-1 > -1 and (gridobjects[i][ii-1] == "earth" or gridobjects[i][ii-1] == "purple" or gridobjects[i][ii-1] == "yellow" ):
                            gridobjects[i][ii-1] = "seed"
                        gridwater[i][ii] -= 150
                        
                elif z == "spark":
                    gridcolor[i][ii] = R
                    gridobjects[i][ii] = "fire"
                    
                elif z == "fire":
                    if(randint(0,200))==0:
                        gridobjects[i][ii] = "seed"
                    else:
                        gridobjects[i][ii] = "burnt"
                    gridwater[i][ii] = 0
                    gridcolor[i][ii] = R
                    
                    if i+1 < (width/tilesize) and (gridobjects[i+1][ii] == "tall grass" or gridobjects[i+1][ii] == "grass" or gridobjects[i+1][ii] == "grass"):
                        gridobjects[i+1][ii] = "spark"
                    if ii+1 < (height/tilesize) and (gridobjects[i][ii+1] == "tall grass" or gridobjects[i][ii+1] == "grass" or gridobjects[i][ii+1] == "grass"):
                        gridobjects[i][ii+1] = "spark"                       
                    if i-1 > -1 and (gridobjects[i-1][ii] == "tall grass" or gridobjects[i-1][ii] == "grass" or gridobjects[i-1][ii] == "grass"):
                        gridobjects[i-1][ii] = "spark"
                    if ii-1 > -1 and (gridobjects[i][ii-1] == "tall grass" or gridobjects[i][ii-1] == "grass" or gridobjects[i][ii-1] == "grass"):
                        gridobjects[i][ii-1] = "spark"

                elif z == "water":
                    gridcolor[i][ii] = B
                    gridobjects[i][ii] = "blue"
                
                ii+=1
            i+=1

        if(weather > 0):
            i=0
            while i < weather:
                x = randint(0,(width/tilesize)-1)
                y = randint(0,(height/tilesize)-1)
                gridwater[x][y] += randint(1, weather)
                gridcolor[x][y] = B
                i+=1
            if weather > 250 and (randint(0,100)==0):
                gridobjects[x][y] = "spark"
                print("lightning strike")
                i=0
                for list in grid:
                    ii=0
                    for z in list:
                        gridcolor[i][ii] = [248,248,255]
                        ii+=1
                    i+=1

                
            #weather -= 1

                    
        i=0
        while i < len(cows):
            #print(cows[i])
            #check for starved cow
                
            
            if abs(cows[i][0]-cows[i][2]) > abs(cows[i][1]-cows[i][3]): # move the cow to it's target
                if(cows[i][0] > cows[i][2]) and cows[i][0]-1 > 0:
                    cows[i][0] -= 1
                elif(cows[i][0] < cows[i][2]) and cows[i][0]+1 < width/tilesize:
                    cows[i][0] += 1
            elif abs(cows[i][0]-cows[i][2]) < abs(cows[i][1]-cows[i][3]):
                if(cows[i][1] > cows[i][3]) and cows[i][1]-1 > 0:
                    cows[i][1] -= 1
                elif(cows[i][1] < cows[i][3]) and cows[i][1]+1 < height/tilesize:
                    cows[i][1] += 1

                
            gridcolor[cows[i][0]][cows[i][1]] = [248,248,255] #display the cow

            if(gridobjects[cows[i][0]][cows[i][1]] == "tall grass"): #cow eats grass
                gridobjects[cows[i][0]][cows[i][1]] = "seed"
                cows[i][4] += 50
            #else: #no grass :,(


            cows[i][2] += randint(-1, 1) #wander around aimlessly for grass
            cows[i][3] += randint(-1, 1)

            cows[i][4] -= 2
            if(cows[i][4] > 300):
                cows[i][4] = 50
                cows.append(copy.deepcopy(cows[i]))
                i+=1
            elif(cows[i][4] <= 0):
                cows.pop(i)
                print("dead cow")
            else:
                i+=1
                
            #print(cows[i][2])
            #print(cows[i][3])
        
        # [x, y, destination x, destinatoin y, food]


            


            
        #mainclock.tick(80)###default = 80
        pygame.display.update()
       











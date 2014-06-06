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


foodvalue = 50
reproductionvalue = 500
startingfood = 100
upkeepvalue = 1


lightningthreshhold = 250
bigweather = 300
mediumweather = 200


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
# [x, y, destination x, destinatoin y, startingfood, foodvalue, reproductionvalue, upkeepvalue, carniverous]




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
    #print(ii)
            
    if ii >= height/tilesize:
        ii = 0
        i += 1
        #print(i)


        
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
                    cows.append([cowX, cowY, cowX, cowY, startingfood, foodvalue, reproductionvalue, startingfood, upkeepvalue, 0])
                    print("Cow")
                    
                if event.key== ord('v'):
                    weather = bigweather
                    print("weather: ")
                    print(weather)
                    
                if event.key== ord('x'):
                    weather = 0
                    print("weather: ")
                    print(weather)

                if event.key== ord('c'):
                    weather = mediumweather
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
                #gridcolor[x][y] = B
                i+=1
            if weather > lightningthreshhold and (randint(0,100)==0):
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
                if(cows[i][0] > cows[i][2]) and cows[i][0]-1 >= 0:
                    cows[i][0] -= 1
                elif(cows[i][0] < cows[i][2]) and cows[i][0]+1 < width/tilesize:
                    cows[i][0] += 1
            elif abs(cows[i][0]-cows[i][2]) < abs(cows[i][1]-cows[i][3]):
                if(cows[i][1] > cows[i][3]) and cows[i][1]-1 >= 0:
                    cows[i][1] -= 1
                elif(cows[i][1] < cows[i][3]) and cows[i][1]+1 < height/tilesize: 
                    cows[i][1] += 1

            if cows[i][9] == 0:
                colora=255-cows[i][6]
                colorb=255-cows[i][5]
                colorc=255-cows[i][8]
            else:
                colora=0+cows[i][6]
                colorb=0+cows[i][5]
                colorc=0+cows[i][8]

            

            if colora > 255:
                colora = 255
            if colorb > 255:
                colorb = 255
            if colorc > 255:
                colorc = 255

            if colora < 0:
                colora = 0
            if colorb < 0:
                colorb = 0
            if colorc < 0:
                colorc = 0
            
                
            gridcolor[cows[i][0]][cows[i][1]] = [colora ,colorb,colorc] #display the cow

            if(gridobjects[cows[i][0]][cows[i][1]] == "tall grass") and cows[i][9] == 0: #cow eats grass
                gridobjects[cows[i][0]][cows[i][1]] = "seed"
                cows[i][4] += foodvalue
            if(cows[i][9] == 1): # vampiric cattle
                cc = 0
                while cc < len(cows):
                    if(cows[cc][0] == cows[i][0] and cows[cc][1] == cows[i][1] and cc != i and cows[cc][9] == 0):
                           cows[i][4] += cows[cc][4]
                           cows[cc][4] = 0
                    cc+=1
                       
                
            #else: #no grass :,(
        # [x, y, destination x, destinatoin y, food, foodvalue, reproductionvalue, startingfood, upkeepvalue]


            cows[i][2] += randint(-1, 1) #wander around aimlessly for grass
            cows[i][3] += randint(-1, 1)

            cows[i][4] -= upkeepvalue
            if(cows[i][4] > reproductionvalue):
                cows[i][4] = cows[i][7]
                newcowstartingfood = cows[i][7]+randint(-1, 1)
                #newcowfoodvalue = cows[i][5]+randint(-1,1)
                newcowreproductivevalue = cows[i][6]+randint(-1, 1)

                carniverous = cows[i][9]
                if cows[i][9] == 0:
                    if randint(0,500) == 32:
                        carniverous = 1
                        
                if cows[i][9] == 1:
                    if randint(0,500) == 64:
                        carniverous = 0

                newcowupkeepvalue = cows[i][8]+randint(-1, 1)+10*carniverous

                if newcowupkeepvalue < 1:
                    newcowupkeepvalue = 1

                xyz = 10+10*carniverous
                if newcowupkeepvalue <= 9 +10*carniverous:
                    xyz = xyz - newcowupkeepvalue
                else:
                    xyz = 1
                    
               
                newcowfoodvalue = newcowupkeepvalue * 50
                newcowreproductivevalue = (newcowstartingfood*xyz)+newcowfoodvalue
                

                    
                
                cows.append([cows[i][0], cows[i][1], cows[i][2], cows[i][3], newcowstartingfood, newcowfoodvalue, newcowreproductivevalue, newcowstartingfood, newcowupkeepvalue, carniverous])
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
       











import pygame
from pygame import key
import pygame.freetype
import itertools
class Sorting():

    def __init__(self, list1, surface,x,y):
        self.surface = surface
        self.list = list1
        self.x = x
        self.y = y
        self.Font = pygame.freetype.SysFont('Sans', 15)
        self.size = (680/(len(self.list)))
        self.speed = self.size * 4
        self.space=(700-(self.size * len(self.list)))/len(self.list)
        self.color = (187, 142, 212)
        self.highlightColor = (230, 184, 255)
        self.surfColor = (51, 54, 56)
        self.iterations = 0

    def paint(self):
        pygame.event.pump()
        
        
        for i in range(len(self.list)):
            pygame.draw.rect(self.surface, self.color, pygame.Rect(self.x + (self.size+self.space) * i, self.y-self.list[i], self.size, self.list[i]))
            
            #sized = self.Font.render_to(self.surface, ((self.x + 49 * i)+15,self.y + 30), str(self.list[i]), (0,0,0))
            
        pygame.draw.line(self.surface, self.color, (40,500), (760,500), 1)
        comparisond = self.Font.render_to(self.surface, (700,540), str(self.iterations), (255,255,255))
    def bubble_sort(self):
        for i in range(len(self.list) - 1):
            for j in range(len(self.list) - i - 1):
                if self.list[j] > self.list[j + 1]:
                    t = self.list[j]
                    self.list[j] = self.list[j + 1]
                    self.list[j + 1] = t
                self.surface.fill(self.surfColor)
                
                self.paint()
                self.highlight(j+1)

                
                if(len(self.list) > 75):
                    pygame.time.delay(int(1))
                else:
                    pygame.time.delay(int(self.speed))

                pygame.display.update()
                self.iterations += 1

    def partition(self, start, end):
        pivot_index = start
        pivot = self.list[pivot_index]
        
        while start < end:
            self.surface.fill(self.surfColor)
                
            self.paint()
            self.highlight(start)
            self.highlight(end)
            pygame.time.delay(int(self.speed))

            pygame.display.update()
            while start < len(self.list) and self.list[start] <= pivot:
                start += 1
            while self.list[end] > pivot:
                end -= 1
            if(start < end):
                self.list[start], self.list[end] = self.list[end], self.list[start]
            self.iterations += 1
        self.list[end], self.list[pivot_index] = self.list[pivot_index], self.list[end]
        return end
     

    def quick_sort(self,start, end):
        if (start < end):
            p = self.partition(start, end)

            self.quick_sort(start, p - 1)
            self.quick_sort(p + 1, end)
            self.surface.fill(self.surfColor)
            self.paint()

            pygame.display.update()
    def insertionSort(self):
        for i in range(1, len(self.list)):
            key = self.list[i]
            j = i-1
            while j >= 0 and key < self.list[j]:
                self.list[j + 1] = self.list[j]
                j -= 1

                self.surface.fill(self.surfColor)
                
                self.paint()
                self.highlight(j+1)
                self.iterations += 1
                pygame.time.delay(int(self.speed))

                pygame.display.update()
            self.list[j + 1] = key


        self.surface.fill(self.surfColor)
        self.paint()
        
        

        pygame.display.update()


    def highlight(self,i):
        pygame.draw.rect(self.surface, self.highlightColor, pygame.Rect(self.x + (self.size+self.space) * i, self.y-self.list[i], self.size, self.list[i]))


    
    
  
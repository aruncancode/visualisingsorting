import pygame, random


class Visualise():

    def __init__(self, screen, width, line_count):
        self.screen = screen
        self.black = (0,0,0)
        self.white = (255,255,255)
        self.lines = []
        self.width = width
        self.line_count = line_count
        self.true = 1
        pygame.init() 
    
    def bubbleSort(self, ar):
        x = len(ar)
        for i in range(x):
            for j in range(0, x-i-1):
                print(ar[j].num)
                if ar[j].num > ar[j+1].num:
                    ar[j].num, ar[j+1].num = ar[j+1].num, ar[j].num

    def run(self):
        for e in range(1, self.line_count+1):
            self.lines.append(Line(self.screen,800, e, self.line_count))
        while self.true:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.true=0

            for line in self.lines:
                line.draw()
                pygame.display.flip()
            
            self.bubbleSort(self.lines)
            print(self.lines)
            
    
class Line():
    def __init__(self, screen,width, n, num_lines):
        self.screen = screen
        self.width = 800
        self.num = n
        self.line_count = num_lines
        self.create(width, num_lines, n)

    def create(self, width, line_count, line):
            height = random.randint(200, 800)
            self.x = (int(line * (width/line_count)) , height)
            self.y = (int(line * (width/line_count)), 800)

    def draw(self):
            pygame.draw.line(self.screen, (255,255,255), self.x, self.y, 1)
            pygame.display.update()

    def move(self):
            self.x -= 1



# class Sort():

#     def __init__(self):
#         super().__init__()
        
#     def bubbleSort(self, ar):
#         n = len(ar)
#         for i in range(n):
#             for j in range(0, n-i-1):
#                 if ar[j].n > ar[j+1].n:
#                     ar[j].n, ar[j+1].n = ar[j+1].n, ar[j].n
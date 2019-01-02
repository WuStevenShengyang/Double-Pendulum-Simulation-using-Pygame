import pygame
import math
pygame.init()

BLACK = [0, 0, 0]
WHITE = [255, 255, 255]
RED = [255, 0, 0]
BLUE = [0, 0, 255]
GREEN = [0, 255, 0]
PI = math.pi

class doublePendulum():
    def __init__(self, theta1, theta2, color):
        self.theta1 = theta1
        self.theta2 = theta2

        self.x1 = 0
        self.y1 = 0
        
        self.x2 = 0
        self.y2 = 0

        self.endPoints = []
          
        self.l1 = 130
        self.l2 = 130
   
        self.m1 = 0.1
        self.m2 = 0.1
   
        self.v1 = 0
        self.v2 = 0
   
        self.a1 = 0
        self.a2 = 0
   
        self.g = 1

        self.color = color

        self.screen = pygame.display.get_surface()
        self.width, self.height = self.screen.get_size()

    def __firstPosition(self):
        self.x1 = self.l1 * math.sin(self.theta1) + self.width / 2
        self.y1 = self.l1 * math.cos(self.theta1) + self.height / 4

    def __secondPosition(self):
        self.x2 = self.l1 * math.sin(self.theta1) + self.l2 * math.sin(self.theta2) + self.width / 2
        self.y2 = self.l1 * math.cos(self.theta1) + self.l2 * math.cos(self.theta2) + self.height / 4
        
    def __acceleration1(self):
        exp1 = -self.g * (2 * self.m1 + self.m2) * math.sin(self.theta1)
        exp2 = self.m2 * self.g * math.sin(self.theta1 - 2 * self.theta2)
        exp3 = 2 * math.sin(self.theta1 - self.theta2) * self.m2 * ((self.v2 * self.v2) * self.l2 + (self.v1 * self.v1) * self.l1 * math.cos(self.theta1 - self.theta2))
        exp4 = self.l1 * (2 * self.m1 + self.m2 - self.m2 * math.cos(2 * self.theta1 - 2 * self.theta2))

        self.a1 = (exp1 - exp2 - exp3) / (exp4)

    def __acceleration2(self):
        exp1 = 2 * math.sin(self.theta1 - self.theta2)
        exp2 = (self.v1 * self.v1) * self.l1 * (self.m1 + self.m2)
        exp3 = self.g * (self.m1 + self.m2) * math.cos(self.theta1)
        exp4 = (self.v2 * self.v2) * self.l2 * self.m2 * math.cos(self.theta1 - self.theta2)
        exp5 = self.l2 * (2 * self.m1 + self.m2 - self.m2 * math.cos(2 * self.theta1 - 2 * self.theta2))

        self.a2 = (exp1 * (exp2 + exp3 + exp4)) / (exp5)
        
        
    def draw(self):
        pygame.draw.circle(self.screen, self.color, (int(self.x1), int(self.y1)), 17)
        pygame.draw.line(self.screen, BLACK, (int(self.width / 2), int(self.height / 4)), (int(self.x1), int(self.y1)), 3)

        pygame.draw.circle(self.screen, self.color, (int(self.x2), int(self.y2)), 17)
        pygame.draw.line(self.screen, BLACK, (int(self.x1), int(self.y1)), (int(self.x2), int(self.y2)), 3)


    def run(self):
        self.__firstPosition()
        self.__secondPosition()

        self.endPoints.append((self.x2, self.y2))

        self.__acceleration1()
        self.__acceleration2()

        self.v1 += self.a1
        self.v2 += self.a2

        self.theta1 += self.v1
        self.theta2 += self.v2

    def trace(self):
        for i in range(len(self.endPoints) - 1):
            pygame.draw.line(self.screen, self.color, (int(self.endPoints[i][0]), int(self.endPoints[i][1])),
                (int(self.endPoints[i + 1][0]), int(self.endPoints[i + 1][1])), 2)

def main():
    w = pygame.display.set_mode((600, 400))
    w.fill(WHITE)
    view = True

    clock = pygame.time.Clock()
    
    pendulum1 = doublePendulum(PI / 2, PI / 2, BLUE)
    pendulum2 = doublePendulum(PI / 2, PI / 3, BLACK)

    while view:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                view = False

        pendulum1.run()
        pendulum1.draw()
        pendulum1.trace()

        pendulum2.run()
        pendulum2.draw()
        pendulum2.trace()

        clock.tick(50)
        pygame.display.flip()
        w.fill(WHITE)


if __name__ == "__main__":
    main()
        
        

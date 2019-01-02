import pygame
import math
pygame.init()

WHITE = [255, 255, 255]
BLACK = [0, 0, 0]
PI = math.pi
g = 1

#First Rod Position
def firstPosition(length1, theta1, theta2):
    x1 = length1 * math.sin(theta1) + 300
    y1 = length1 * math.cos(theta1) + 70

    return x1, y1

#Second Rod Position
def secondPosition(length1, length2, theta1, theta2):
    x2 = length1 * math.sin(theta1) + length2 * math.sin(theta2) + 300
    y2 = length1 * math.cos(theta1) + length2 * math.cos(theta2) + 70

    return x2, y2

def acceleration1(m1, m2, theta1, theta2, l1, l2, v1, v2):
    """
    if theta1 > PI:
        theta1 = theta1 - PI
    if theta2 > PI:
        theta2 = theta2 - PI
        """
        
    exp1 = -g * (2 * m1 + m2) * math.sin(theta1)
    exp2 = m2 * g * math.sin(theta1 - 2 * theta2)
    exp3 = 2 * math.sin(theta1 - theta2) * m2 * ((v2 * v2) * l2 + (v1 * v1) * l1 * math.cos(theta1 - theta2))
    exp4 = l1 * (2 * m1 + m2 - m2 * math.cos(2 * theta1 - 2 * theta2))

    return (exp1 - exp2 - exp3) / (exp4)

def acceleration2(m1, m2, theta1, theta2, l1, l2, v1, v2):
    """

    if theta1 > PI:
        theta1 = theta1 - PI
    if theta2 > PI:
        theta2 = theta2 - PI
        """

    exp1 = 2 * math.sin(theta1 - theta2)
    exp2 = (v1 * v1) * l1 * (m1 + m2)
    exp3 = g * (m1 + m2) * math.cos(theta1)
    exp4 = (v2 * v2) * l2 * m2 * math.cos(theta1 - theta2)
    exp5 = l2 * (2 * m1 + m2 - m2 * math.cos(2 * theta1 - 2 * theta2))

    return (exp1 * (exp2 + exp3 + exp4)) / (exp5)

#Main
def main():
    w = pygame.display.set_mode((600, 400))
    w.fill(WHITE)
    view = True

    clock = pygame.time.Clock()
    
    theta1 = PI / 2
    theta2 = PI / 2
    
    v1 = 0
    v2 = 0
    
    a1 = 0
    a2 = 0

    #First Rod
    l1 = 130
    m1 = 0.1
    x1, y1 = firstPosition(l1, theta1, theta2)

    #Second Rod
    l2 = 130
    m2 = 0.1
    x2, y2 = secondPosition(l1, l2, theta1, theta2)    

    endPoints = []
    
    while view:
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                view = False

        #Draw        
        pygame.draw.circle(w, BLACK, (int(x1), int(y1)), 17)
        pygame.draw.line(w, BLACK, (300, 70), (int(x1), int(y1)))

        pygame.draw.circle(w, BLACK, (int(x2), int(y2)), 17)
        pygame.draw.line(w, BLACK, (int(x1), int(y1)), (int(x2), int(y2))) 

        #Re-calculate positions
        x1, y1 = firstPosition(l1, theta1, theta2)
        x2, y2 = secondPosition(l1, l2, theta1, theta2)
        endPoints.append((x2, y2))
        
        #Calculating Acceleration
        a1 = acceleration1(m1, m2, theta1, theta2, l1, l2, v1, v2)
        a2 = acceleration2(m1, m2, theta1, theta2, l1, l2, v1, v2)

        #Draw Endpoints
        for i in range(len(endPoints) - 1):
            pygame.draw.line(w, BLACK,(int(endPoints[i][0]), int(endPoints[i][1])),
                (int(endPoints[i + 1][0]), int(endPoints[i + 1][1])), 1)

                
        v1 += a1
        v2 += a2
        
        theta1 += v1
        theta2 += v2

        clock.tick(30)
        pygame.display.flip()
        w.fill(WHITE)


if __name__ == "__main__":
    main()

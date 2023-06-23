import pygame

'''
When we want to call a method such that we pass in a string and get as a return
value a new object, we are essentially calling a factory method. The type of 
the object is determined by the string that is passed to the method. This makes
it easy to extend the code you write by allowing you to add functionality to 
your software, which is accomplished by adding a new class and extending the 
factory
'''


class Shape(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        raise NotImplementedError()

    @staticmethod
    def factory(type: str = None):
        if type == "Circle":
            return Circle(100, 100)
        if type == "Square":
            return Square(100, 100)
        assert 0, f'Bad shape requested: {type}'

    def move(self, direction):
        if direction == 'up':
            self.y -= 4
            if self.y < 0:
                self.y = 0
        elif direction == 'down':
            self.y += 4
            if self.y > 580:
                self.y = 580
        elif direction == 'left':
            self.x -= 4
            if self.x < 0:
                self.x = 0
        elif direction == 'right':
            self.x += 4
            if self.x > 780:
                self.x = 780


class Square(Shape):
    def draw(self):
        pygame.draw.rect(
            screen,
            (255, 255, 0),
            pygame.Rect(self.x, self.y, 20, 20)
        )


class Circle(Shape):
    def draw(self):
        pygame.draw.circle(
            screen,
            (0, 255, 255),
            (self.x, self.y),
            10
        )


if __name__ == '__main__':
    screen_width = 800
    screen_height = 600
    x = 100
    y = 100

    # square = Square(x, y)
    # circle = Circle(x, y)
    # at first by default the object will be the square
    square = Shape.factory(type='Cricle')
    circle = Shape.factory(type='Square')
    obj = square
    screen = pygame.display.set_mode(size=(screen_width, screen_height))
    player_quits = False
    while not player_quits:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                player_quits = True
            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_c]:
                if obj.__class__ is Square:
                    obj = circle
                    circle.x = square.x
                    circle.y = square.y
            if pressed[pygame.K_s]:
                if obj.__class__ == Circle:
                    obj = square
                    square.x = circle.x
                    square.y = circle.y
            if pressed[pygame.K_UP]:
                obj.move('up')
            if pressed[pygame.K_DOWN]:
                obj.move('down')
            if pressed[pygame.K_LEFT]:
                obj.move('left')
            if pressed[pygame.K_RIGHT]:
                obj.move('right')
            screen.fill((0, 0, 0))
            # pygame.draw.rect(screen, (255, 255, 0), pygame.Rect(x, y, 20, 20))
            obj.draw()
        pygame.display.flip()

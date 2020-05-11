from Section09_Decorator.RegularDecorator.Circle import Circle
from Section09_Decorator.RegularDecorator.ColoredShape import ColoredShape
from Section09_Decorator.RegularDecorator.TransparentShape import TransparentShape

if __name__ == '__main__':
    circle = Circle(2)
    print(circle)
    red_circle = ColoredShape(circle, "red")
    print(red_circle)
    # ColoredShape doesn't have resize()
    # red_circle.resize(3)
    red_half_transparent_square = TransparentShape(red_circle, 0.5)
    print(red_half_transparent_square)
    # nothing prevents double application
    mixed = ColoredShape(ColoredShape(Circle(3), 'red'), 'blue')
    print(mixed)

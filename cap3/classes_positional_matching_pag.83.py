class Color:
    __match_args__ = ('red', 'green', 'blue')
    def __init__(self, r, g, b, name='anonymous'):
        self.name = name
        self.red, self.green, self.blue = r, g, b

color_red = Color(255, 0, 0, 'red')
color_blue = Color(0, 0, 255)
for subject in (42.0, color_red, color_blue):
    match subject:
        case float(x):
            print('float', x)
        case Color(red, green, blue, name='red'):
            print(subject)
            print(type(subject).__name__, subject.name, red, green, blue)
        case Color(red, green, 255) as color:
            print(subject)
            print(color)
            print(type(subject).__name__, color.name, red, green, color.blue)
        case _:
            print(type(subject), subject)

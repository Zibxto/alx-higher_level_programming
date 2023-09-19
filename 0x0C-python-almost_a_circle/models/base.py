#!/usr/bin/python3
"""
Module base
Contains a class called Base
"""


class Base:
    """This class represents a base class"""
    __nb_object = 0

    def __init__(self, id=None):
        """ Class constructor"""
        if id is not None:
            self.id = id
        else:
            __class__.__nb_object += 1
            self.id = __class__.__nb_object

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        returns the JSON string representation of list_dictionaries
        """
        import json
        if list_dictionaries is None or list_dictionaries == {}:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """Returns Python obj of JSON string representation"""
        if json_string is None or len(json_string) == 0:
            json_string = "[]"
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """Save json strings of all instances into file"""
        objs = []
        if list_objs is not None:
            for o in list_objs:
                objs.append(cls.to_dictionary(o))
        filename = cls.__name__ + ".json"
        with open(filename, "w") as f:
            f.write(cls.to_json_string(objs))

    @classmethod
    def create(cls, **dictionary):
        """Returns instance with attributes already set"""
        if cls.__name__ == "Square":
            dummy = cls(1)
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Returns list of instances"""
        filenamee = cls.__name__ + ".json"
        my_list = []
        try:
            with open(filenamee, "r") as f:
                instances = cls.from_json_string(f.read())
            for i, dic in enumerate(instances):
                my_list.append(cls.create(**instances[i]))
        except Exception as e:
            print(f"{e} error occured")
        return my_list

    @classmethod
    def save_to_file_csv(cls, list_objs):
        filename = cls.__name__ + ".csv"
        with open(filename, 'w', newline='') as f:
            writer = csv.writer(f)
            for o in list_objs:
                if cls.__name__ == "Rectangle":
                    writer.writerow([o.id, o.width, o.height, o.x, o.y])
                if cls.__name__ == "Square":
                    writer.writerow([o.id, o.size, o.x, o.y])

    @classmethod
    def load_from_file_csv(cls):
        objs = []
        filename = cls.__name__ + ".csv"
        with open(filename, 'r', newline='') as f:
            reader = csv.reader(f)
            for row in reader:
                if cls.__name__ == "Rectangle":
                    dic = {"id": int(row[0]),
                           "width": int(row[1]),
                           "height": int(row[2]),
                           "x": int(row[3]),
                           "y": int(row[4])}
                if cls.__name__ == "Square":
                    dic = {"id": int(row[0]),
                           "size": int(row[1]),
                           "x": int(row[2]),
                           "y": int(row[3])}
                o = cls.create(**dic)
                objs.append(o)
        return objs

    @staticmethod
    def draw(list_rectangles, list_squares):
        """
        Opens a windows and draws all the Rectangles and Square
        """
        import turtle

        t = turtle.Turtle()
        t.screen.bgcolor("#7a0b4c")
        t.pensize(3)
        t.shape("turtle")

        t.color("#f2f2f2f2")
        for rectangle in list_rectangles:
            t.showturtle()
            t.up()
            t.goto(rectangle.x, rectangle.y)
            t.down()
            for i in range(2):
                t.forward(rectangle.width)
                t.left(90)
                t.forward(rectangle.height)
                t.left(90)
            t.hideturtle()

        t.color("#b5e3d8")
        for square in list_squares:
            t.showturtle()
            t.up()
            t.goto(square.x, square.y)
            t.down()
            for i in range(2):
                t.forward(square.width)
                t.left(90)
                t.forward(square.height)
                t.left(90)
            t.hideturtle()

        turtle.done()

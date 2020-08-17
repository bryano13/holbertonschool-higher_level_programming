#!/usr/bin/python3
""" 101-main """
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

if __name__ == "__main__":

    list_rectangles = [Rectangle(100, 40),]
    list_squares = [Square(80, 30, 70)]

    Base.draw(list_rectangles, list_squares)

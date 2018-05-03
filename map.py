import pygame as pg


tileBrick = 1
tileEmpty = 29


class Map:

    def __init__(self):

        self.spriteSheet = pg.image.load("graphics/tiles.png")
        self.tileWidth = 16
        self.tileHeight = 16
        self.mapWidth = 30
        self.mapHeight = 28
        self.tiles = []
        self.map = {}

    def create(self):

        with open(self.spriteSheet, "r") as file:
            for line in file:
                for sprite in line:
                    cropped = pg.Surface((16,16))
                    self.tiles.append(cropped)
            tiles = self.tiles

        return tiles


    def render(self):

        




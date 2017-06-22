"""
A genuinely simple map I will use to draw some tiles on screen for testing
"""

import worldbuilding

class map():
    def __init__(self):
        self.title = "Example map"
        self.description = "This is the example map"
        self.text = "test"
        self.mapArray = [ worldbuilding.tile_soil(0, 0), worldbuilding.tile_soil(0, 32), worldbuilding.tile_soil(0, 64), worldbuilding.tile_soil(0, 96), worldbuilding.tile_soil(0, 32),worldbuilding.tile_soil(32, 32), worldbuilding.tile_soil(64, 64), worldbuilding.tile_soil(96, 96)]

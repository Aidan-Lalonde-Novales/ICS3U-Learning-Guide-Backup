#!/usr/bin/env python3

# Created by Aidan Lalonde-Novales
# Created April 2022
# This file contains Learning Guide 02's code.

import stage
import ugame


def game_scene():
    # this function is the main game game_scene

    # image banks
    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")
    image_bank_sprites = stage.Bank.from_bmp16("space_aliens.bmp")

    # sets the background, 10x8
    background = stage.Grid(image_bank_background, 10, 8)

    ship = stage.Sprite(image_bank_sprites, 5, 75, 66)

    # creates a stage, sets to 60fps
    game = stage.Stage(ugame.display, 60)
    # order of layers
    game.layers = [ship] + [background]
    # render the background and sprite list, most likely once per scene
    game.render_block()

    # repeat forever, game loop
    while True:
        # get user input

        # update game logic

        # redraw Sprites
        game.render_sprites([ship])
        game.tick()


if __name__ == "__main__":
    game_scene()

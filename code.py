#!/usr/bin/env python3

# Created by Aidan Lalonde-Novales
# Created April 2022
# This file contains Learning Guide 04's code.

import stage
import ugame

import constants


def game_scene():
    # this function is the main game game_scene

    # image banks
    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")
    image_bank_sprites = stage.Bank.from_bmp16("space_aliens.bmp")

    # sets the background, 10x8
    background = stage.Grid(image_bank_background, 10, 8)

    ship = stage.Sprite(image_bank_sprites, 5, 75, constants.SCREEN_Y - (2 * constants.SPRITE_SIZE))

    # creates a stage, sets to 60fps
    game = stage.Stage(ugame.display, 60)
    # order of layers
    game.layers = [ship] + [background]
    # render the background and sprite list, most likely once per scene
    game.render_block()

    # repeat forever, game loop
    while True:
        # get user input
        keys = ugame.buttons.get_pressed()

        # A button to fire
        if keys & ugame.K_X != 0:
            print("A")
        if keys & ugame.K_O != 0:
            print("B")
        if keys & ugame.K_START != 0:
            print("Start")
        if keys & ugame.K_SELECT != 0:
            print("Select")

        if keys & ugame.K_RIGHT != 0:
            if ship.x < (constants.SCREEN_X - constants.SPRITE_SIZE):
                ship.move((ship.x + constants.SPRITE_MOVEMENT_SPEED), ship.y)
            else:
                ship.move((constants.SCREEN_X - constants.SPRITE_SIZE), ship.y)
                
        if keys & ugame.K_LEFT != 0:
            if ship.x > 0:
                ship.move((ship.x - constants.SPRITE_MOVEMENT_SPEED), ship.y)
            else:
                ship.move(0, ship.y)

        if keys & ugame.K_UP != 0:
            ship.move(ship.x, ship.y - 1)
        if keys & ugame.K_DOWN != 0:
            ship.move(ship.x, ship.y + 1)

        # update game logic

        # redraw Sprites
        game.render_sprites([ship])
        game.tick()  # wait until refresh rate finishes


if __name__ == "__main__":
    game_scene()

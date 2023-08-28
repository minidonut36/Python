"""
A really simple domino game.
"""

import boneyard as yard
# boneyard must have these functions: create, tiles_remaining, and draw

import domino as doms
# domino must have these functions: create, as_str, get_left, get_right


the_yard = yard.create()
game_over = False

while not game_over:
    if yard.tiles_remaining(the_yard) == 0:
        print('Ran out of dominoes')
        game_over = True
    else:
        input('Press return to continue')
        tile = yard.draw(the_yard)
        print('Got tile %s' % (doms.as_str(tile)))
        if doms.get_left(tile) == 6 or doms.get_right(tile) == 6:
            print('Got a SIX!!!')
            game_over = True

print("Game Over.")

"""
I affirm that I have carried out the attached academic endeavors with full academic honesty,
in accordance with the Union College Honor Code and the course syllabus.
"""
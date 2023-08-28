"""
A simple pocker game

:author: Chris Hegang Kim
:note: I affirm that I have carried out the attached academic endeavors with full academic honesty,
in accordance with the Union College Honor Code and the course syllabus.

:reflection: Imported a file called table for the modularity.
Used named constants like ATTEMPTS because it is convenient to change their values throughout the code.
Used helper functions like t.first_row() for the modularity.
"""

import table as t

ATTEMPTS = 10000
MAX_COLUMNS = 10

def play_rounds():
    """
    Starts the entire program running and prints the output table

    :return:
    """
    total_attempt = 0

    t.first_row()

    for i in range (MAX_COLUMNS):
        total_attempt += ATTEMPTS

        t.output_table(t.get_result(total_attempt))

if __name__ == "__main__":
    play_rounds()
"""
    This file is a collection of useful functions for outputting text to the terminal.
    Eventually this will become obsolete as we move towards a 2D game, but for now this should suffice.
    We will need to import this to a file to call the functions, and I'm so new to Python
    That I'm not sure if there is a better way of doing this
"""

#Will return a neatly formatted list, with 1 based index of items
def print_out_ordered_list(input):
    index = 1
    results = ""
    for item in input:
        results += str(index) + " " +  str(item) + "  \n"
        index = index + 1

    return results
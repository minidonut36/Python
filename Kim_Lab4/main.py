"""
A simple die game
"""

from die import *

SIDE12 = 12

def main():
    D6 = Die()
    D12 = Die(SIDE12)

    while not D12.is_twice(D6) and not D6.is_twice(D12):
        input("Press return")

        D6.roll()
        D12.roll()

        print("D6: ", D6, "D12: ", D12)

    print("We have won, and the program ends")

if __name__ == "__main__":
    main()
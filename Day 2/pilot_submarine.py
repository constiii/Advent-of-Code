# import libraries
from bs4 import BeautifulSoup
import os


# create class to solve the challenge
class Submarine:

    """ This class solves the Day 1 challenge from https://adventofcode.com/2021/day/2"""

    def __init__(self, folder: str, file_name: str):
        """
        Initialize instance of class and defines working directory and html file name

        Parameters:
        -----------
        folder: string
            the working directory of where the html file is located
        file_name: string
            the name of the html file
        """
        self.folder = folder
        self.file_name = file_name
        os.chdir(self.folder)

    def read_input(self):
        """
        Read html input from downloaded website (https://adventofcode.com/2021/day/2/input) and return a list of submarine moving commands.
        """
        with open(self.file_name) as html_input:
            # open html file
            soup = BeautifulSoup(html_input, "html.parser")

            # extract html content 
            content = soup.get_text()
            content = content.replace("\n", ",")

            # create list of integer inputs and delete empty entry
            input = content.split(sep = ",")
            input.remove("")
            self.input = input

            # close html file
            html_input.close()
            
    def calculate_positioning(self):
        """
        Calculate the position of the submarine given the html input (first part of the challenge)
        """
        self.depth = int(0)
        self.horizontal = int(0)

        for element in self.input:
            command, value = element.split(sep = " ")
            if command == "forward":
                self.horizontal += int(value)
            elif command == "down":
                self.depth += int(value)
            elif command == "up":
                self.depth -= int(value)

    def calculate_positioning_with_aim(self):
        """
        Calculate the position of the submarine given the html input (second part of the challenge)
        """
        self.depth = int(0)
        self.horizontal = int(0)
        self.aim =int(0) 

        for element in self.input:
            command, value = element.split(sep = " ")
            if command == "forward":
                self.horizontal += int(value)
                self.depth += self.aim * int(value)
            elif command == "down":
                self.aim += int(value)
            elif command == "up":
                self.aim -= int(value)

    def multiply_position(self):
        """
        Perform final calculation to solve the challenge: https://adventofcode.com/2021/day/2
        """
        return int(self.depth * self.horizontal)


if __name__ == "__main__":
   
   # solve challenge with time complexity O(n)
   submarine = Submarine(folder = "C:/Users/z003h4bh/Desktop/Advent of Code/Advent-of-Code/Day 2", file_name = "input.html")
   submarine.read_input()
   #submarine.calculate_positioning() # first part of the challenge
   submarine.calculate_positioning_with_aim() # second part of the challenge
   submarine.multiply_position()
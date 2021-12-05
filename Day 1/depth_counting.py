# import libraries
from bs4 import BeautifulSoup
import os


# create class to solve the challenge
class DepthCounter:

    """ This class solves the Day 1 challenge from https://adventofcode.com/2021/day/1"""

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
        Read html input from downloaded website (https://adventofcode.com/2021/day/1/input) and return a list of integer depth measures.
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
            self.input = [int(x) for x in input]

            # close html file
            html_input.close()

    def count_depth_increase(self):
        """
        Perform calculation to solve the challenge: https://adventofcode.com/2021/day/1 (first part of the challenge)
        """
        counter = 0
        for element in range(1,len(self.input)):
            if self.input[element] > self.input[element-1]:
                counter += 1

        return counter

    def count_depth_increase_window(self):
        """
        Perform calculation to solve the challenge: https://adventofcode.com/2021/day/1 (second part of the challenge)
        """
        counter = 0
        for element in range(1,(len(self.input)-2)):
            if sum(self.input[element:element+3]) > sum(self.input[element-1:element+2]):
                counter += 1

        return counter


if __name__ == "__main__":
   
   # solve challenge with time complexity O(n)
   counter = DepthCounter(folder = "C:/Users/z003h4bh/Desktop/Advent of Code/Advent-of-Code/Day 1", file_name = "input.html")
   counter.read_input()
   counter.count_depth_increase()
   counter.count_depth_increase_window()
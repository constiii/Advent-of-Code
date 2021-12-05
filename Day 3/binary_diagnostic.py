# import libraries
from bs4 import BeautifulSoup
import os


# create class to solve the challenge
class BinaryDiagnostic:

    """ This class solves the Day 3 challenge from https://adventofcode.com/2021/day/3"""

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
        Read html input from downloaded website (https://adventofcode.com/2021/day/3/input) and return a list of submarine moving commands.
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
            
    def calculate_normal(self):
        """
        Calculate the gamma and epsilon values (decimal) given the html input (first part of the challenge)   
        """
        self.gamma_binary = str("")
        self.epsilon_binary = str("")

        for figure in range(0, len(self.input[0])):
            zeros = int(0)
            ones = int(0)

            for element in self.input:
                if element[figure] == "0":
                    zeros += int(1)
                elif element[figure] == "1":
                    ones += int(1)
            if zeros >= ones: 
                gamma_figure = "0"
                epsilon_figure = "1"
            else:
                gamma_figure = "1"
                epsilon_figure = "0"

            self.gamma_binary += str(gamma_figure)
            self.epsilon_binary += str(epsilon_figure)

        self.gamma_decimal = int(self.gamma_binary, 2)
        self.epsilon_decimal = int(self.epsilon_binary, 2)

        return self.gamma_decimal, self.epsilon_decimal

    def helper_evaluate(self, observations, position, type):
        """
        Helper function to shrink the list of observations
        """
        zeros = int(0)
        ones = int(0)

        for element in observations:
            if element[position] == "0":
                zeros += int(1)
            elif element[position] == "1":
                ones += int(1)
        if zeros > ones: 
            max_value = "0"
            min_value = "1"
        elif zeros < ones:
            max_value = "1"
            min_value = "0"
        elif zeros == ones and type == "oxigen":
            max_value = "1"
            min_value = "0"
        elif zeros == ones and type == "co2":
            max_value = "0"
            min_value = "1"

        return max_value, min_value
    
    def calculate_advanced(self):
        """
        Calculate the oxigen and co2 values (decimal) given the html input (second part of the challenge)   
        """
        self.oxigen = self.input.copy()
        self.co2 = self.input.copy()

        # oxigen
        while len(self.oxigen) > 1:
            for figure in range(0, len(self.input[0])):
                print(figure)
                max_value, min_value = self.helper_evaluate(self.oxigen, figure, "oxigen")
                self.oxigen = [x for x in self.oxigen if str(x[figure]) == str(max_value)]
                print(self.oxigen)
        self_oxigen_decimal = int(self.oxigen[0], 2)

        # co2
        while len(self.co2) > 1:
            for figure in range(0, len(self.input[0])):
                max_value, min_value = self.helper_evaluate(self.co2, figure, "co2")
                self.co2 = [x for x in self.co2 if str(x[figure]) == str(min_value)]
        self_co2_decimal = int(self.co2[0], 2)

        return self_oxigen_decimal, self_co2_decimal

    def multiply(self, first_number, second_number):
        """
        Perform final calculation to solve the challenge: https://adventofcode.com/2021/day/3
        """
        return int(first_number * second_number)


if __name__ == "__main__":
   
   # solve challenge with time complexity O(n)
   binary_diagnostic = BinaryDiagnostic(folder = "C:/Users/z003h4bh/Desktop/Advent of Code/Advent-of-Code/Day 3", file_name = "input.html")
   binary_diagnostic.read_input()
   #gamma, epsilon = binary_diagnostic.calculate_normal()
   #binary_diagnostic.multiply(gamma, epsilon) # first challenge
   oxigen, co2 = binary_diagnostic.calculate_advanced()
   binary_diagnostic.multiply(oxigen, co2) # second challenge

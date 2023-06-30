import sys
import csv
import math
import os
from collections import namedtuple
import logging 

#This program illustrates basic OOP skills. 
# This was one of my first attempts at solving a problem with OOP. 
# The program takes data from a text file, converts specific fields to a tuple, and then displays specific information.  

class AutoMPG():
    #You can create class variables here outside of the constructor. 
    #Given the instructions I am creating objects and then creating variables under the constructor. 
    #Later when you do child classes you'll pass in the parent class into the parentheses. 

    def __init__(self, make, model, year, mpg):
        self.make = make 
        self.model = model
        self.year = int(year)
        self.mpg = float(mpg)
    

    def __str__(self):
        text = f"Make: {self.make}  Model: {self.model}  Year: {self.year}  MPG: {self.mpg}"
        return text


    def __repr__(self):
        self.__str__()
      

    def __eq__(self, other):
        print (f'Debug: {str(self)} == str({other})')
        if type(self) == type(other):
            return self.make == other.make and self.model == other.model and self.year == other.year and self.mpg == other.mpg
        else:
            return NotImplemented

    def __lt__(self, other):
        # Compare make
        if self.make < other.make:
            return True
        elif self.make > other.make:
            return False
        
        # Compare model
        if self.model < other.model:
            return True
        elif self.model < other.model:
            return False
        
        #Compare year

        if self.year < other.year:
            return True
        elif self.year < other.year:
            return False

        # Compare MPG

        if self.mpg < other.mpg:
            return True
        elif self.mpg < other.mpg:
            return False

        # Default return (they are "equal")
        return False
        
    
    def __hash__(self):
        return hash(self.__str__())

class AutoMPGData:

    def __init__(self):
        self.data = []
        self._load_data() 
    
    def __iter__(self):
        return iter(list(self.data))
        
    def _clean_data(self):
        with open("auto-mpg.data.txt") as rf:
            lines = rf.readlines()
            ##print(type(lines))
            ## For loop to get around type error 
        with open("auto-mpg.clean.txt", "w") as wf:
            for i in range(len(lines)):
                wf.write(str.expandtabs(lines[i],3))
            wf.close()
        rf.close()
        
    def _load_data (self):
        Record = namedtuple('Record', ['MPG', 'Cylinders', 'Displacement', 'Horsepower', 'Weight', 'Acceleration', 'ModelYear', 'Origin', 'CarName'])
        print("Running _load_data")
        path = '/auto-mpg.clean.txt'
        #Check for a clean file. If not, then run Clean Data function. 
        if os.path.exists(path) is False:
            self._clean_data()
            with open("auto-mpg.clean.txt") as ld:
                csv_reader = csv.reader(ld, skipinitialspace=True, delimiter = ' ')
                print("Opening",path)
                #Iterate over the csv_reader list
                for row in csv_reader:
                    #Do something and refer to Record Class
                    print(row)
                    # Create a Record object from the list created when reading the row (unpack the list)
                    rec = Record(*row)
                    # Parse out make and model from rec.CarName
                    # make is the first word
                    # model is everything else
                    words = rec.CarName.split(" ")
                    make = words[0]
                    model = " ".join(words[1:])
                    # Use the Record object to then create an AutoMPG object
                    a = AutoMPG(make, model, rec.ModelYear, rec.MPG)
                    # Add that object to self.data
                    self.data.append(a)

        else:
            with open("auto-mpg.clean.txt") as ld:
                csv_reader = csv.reader(ld, skipinitialspace=True, delimiter = ' ')
                print("Opening",path)
                #Iterate over the csv_reader list
                for row in csv_reader:
                    #Do something and refer to Record Class
                    print(row)
                    # Create a Record object from the list created when reading the row (unpack the list)
                    rec = Record(*row)
                    # Parse out make and model from rec.CarName
                    # make is the first word
                    # model is everything else
                    words = rec.CarName.split(" ")
                    make = words[0]
                    model = " ".join(words[1:])
                    # Use the Record object to then create an AutoMPG object
                    a = AutoMPG(make, model, rec.ModelYear, rec.MPG)
                    # Add that object to self.data
                    self.data.append(a)

        logging.basicConfig(filename='autompg2.log', level=logging.INFO, filemode='w')

        logging.info(a)

def main():
    for a in AutoMPGData():
        print ('AutoMPG   ', a)
if __name__ == "__main__":

    main()
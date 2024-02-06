#Program to Count the Number of Factors in any number
import math


class Solution():

    def countNumberOfFactorsUnoptimised(number):
        numberOfFactors = 0
        for i in range (1, int(number)+1):
            if(int(number) % i ==0):
                numberOfFactors=numberOfFactors+1

        return numberOfFactors

    # Logic : Factors come in pairs
    def countNumberOfFactorsOptimised(number):
        number = int(number)
        numberOfFactors = 0
        i = 1

        while i <= math.sqrt(number):
            if (number % i == 0):
                # If divisors are equal, count one
                if (number/ i == i):
                    numberOfFactors=numberOfFactors+1
                else:
                    # Otherwise count two
                    numberOfFactors = numberOfFactors + 2
            i = i + 1

        return numberOfFactors

    number = input("Enter a Integer: ")
    print("The number of factors is " , countNumberOfFactorsOptimised(number))



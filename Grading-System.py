# Fraol Dechasa
'''
Analysis - create a program to read a list of test grades from a file that assigns
each grades and student numbers to its specific letter grades.

specification- input- prompt the user to input the name of the file
                process- calculate the mean, median, and standard deviation
                outline - prints out the student number, their grades and letter for their grades
                          prints out the mean, median and standard deviation of the grades

Design- import the math library
        create a function called mean()
        calculate the average of the grades by using an accumulator
        return the mean
        create a function called stdDev()
        create an accumulator loop to calculate the standard deviation
        return the standard deviation
        create a function called median
        calculate the median of the grades
        return median for the function
        create a main function
        create a exception handler
        prompt the user for input of the file
        create a for accumulator loop for the grades of the score and the score
        create another for loop to print out the report
        specify the exception
        call the function main


'''
# import the math library
import math
# define a function that calculates the mean.
def mean(nums):
    # initializing the num accumulator
    total = 0.0
    # accumulator for summing the grades
    for num in nums:
        total = total + num
        # return the mean value
    return total / len(nums)


# define a function that calculates the standard deviation
def stdDev(nums, xbar):
    # intialization variable
    sumDevSq = 0.0
    # accumulator for calculating standard deviation
    for num in nums:
        dev = num - xbar
        sumDevSq = sumDevSq + dev * dev
        # return
    return math.sqrt(sumDevSq / (len(nums) - 1))


# define a function that calculates the median

def median(nums):
    # sort the nums list in order
    nums.sort()
    size = len(nums)
    # Divide  it by 2 to check if its an odd or even number
    midPos = size // 2
    # used a condition to get the appropriate equation for the median
    if size % 2 == 0:
        median = (nums[midPos] + nums[midPos - 1]) / 2.0
    else:
        median = nums[midPos]
        # return the median
    return median

# define the main function that
def main():
    try:
        # prompts the user to input the filename

        filename = input(" The name of the file: ")
        infile = open(filename, 'r')

        # create a empty list for the score, letter , and lst

        lst = []
        letter = []
        score = []

    # create a for loop that grades the scores and appends values to the lists
        for i in infile:

            x, y = i.split()
            y = float(y)
            lst.append(i)
            score.append(y)

            # conditions for reporting the grades

            if y >= 90:
                y = "A"
            elif y >= 80:
                y = "B"
            elif y >= 70:
                y = "C"
            elif y >= 60:
                y = "D"
            else:
                y = "F"
            letter.append(y)

        # initialization variable for the letter of the grades

        c = -1
        # create a for loop that prints student ID, score, letter of the grade
        for i in lst:
            c = c + 1
            a, b = i.split()
            print(a, b, letter[c])

    # assign the mean, median, and standard deviation to the variables and round the numbers.

        m = round(mean(score), 5)
        dev = round(stdDev(score, m), 5)
        md = round(median(score), 5)

    # print the variables assigned to the functions
        print()
        print("Mean score: ", m, end="\n")
        print("Standard deviation score : ", dev, end="\n")
        print("Median score : ", md)

    # create a for loop that counts the number of student that is in the range of their specific letters
        for i in ['A', 'B', 'C', 'D', 'F']:
            amount = letter.count(i)
            print()
            print(amount, 'students got a', i)

        # exception handler for the file input
    except FileNotFoundError:
        print("The file name you entered is not in the directory ")

# call the man function
main()




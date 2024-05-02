#
# (a)(i)
#a python program using function and conditions to display the grades that the students will be recieving.
#the grades are:
#90% - 100% grade is A
#80% - 89% GRADE IS B
#70% - 79% GRADE IS C
#60% - 69% GRADE IS D
#50% -59% GRADE IS E
#<50% FAIL
def calculate_grade(percentage):
    if percentage >= 90:
        return "A"
    elif percentage >= 80:
        return "B"
    elif percentage >= 70:
        return "C"
    elif percentage >= 60:
        return "D"
    elif percentage >= 50:
        return "E"
    else:
        return "FAIL"

def main():
    try:
        percentage = float(input("Enter the student's percentage: "))
        if percentage < 0 or percentage > 100:
            print("Percentage must be between 0 and 100.")
        else:
            grade = calculate_grade(percentage)
            print(f"The student's grade is: {grade}")
    except ValueError:
        print("Invalid input. Please enter a numeric value.")

if __name__ == "__main__":
    main()




#(a)(ii)
#a python program to convert tempratures to and from celsius and fahrenheit
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def main():
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = celsius_to_fahrenheit(celsius)
    print("Temperature in Fahrenheit:", fahrenheit)

if __name__ == "__main__":
    main()


#(b)(i)
#using a function and variables, create a program that calculates the area of a triangle of base = 2, and height = 3. formula A= 1/2*b*h

def area_of_triangle(b, h):
    return 1/2 * b * h

#let base be b, and height be h as variables
b = 2
h = 3

triangle_area = area_of_triangle(b, h)
print("Area of the triangle:", triangle_area)



# #b(ii)
# #in a loop, write python function to sum all the numbers in a list
#sample_list=[9,2,3,5,8]

def sum_list(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

sample_list = [9, 2, 3, 5, 8]
print("Sum of the numbers in the list:", sum_list(sample_list))







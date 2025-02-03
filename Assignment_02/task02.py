# Simple Area Calculator for various shapes
# 1. Input Shape Choice from User
print("Calculate the area of following shapes:")
print("1. Circle")
print("2. Rectangle")
print("3. Square")
print("4. Triangle")

# Circle
print("Area of circle:")
radius = float(input("Enter radius for circle: "))
circle_area = 3.14 * radius* radius # radius = pi * r^2
print("Area of circle is: ", circle_area)
    
# rectangle
print("\nArea of rectangle:")
length = float(input("Enter length of rectangle: "))
width = float(input("Enter width of rectangle: "))
rectangle_area = length*width
print("Area of rectange is: ", rectangle_area)
  
# square  
print("\nArea of square:")
side = float(input("Enter length of one side of square: "))
square_area = side*side
print("Area of square is: ", square_area)
    
# triangle
print("\nArea of triangle:")
base = float(input("Enter base: "))
height = float(input("Enter height: "))
triangle_area = 0.5 * base * height
print("Area of Triangle is: ", triangle_area)
    
# print results
print("\nPrint areas of all shapes:")
print("The area of the circle is:", circle_area)
print("The area of the rectangle is:", rectangle_area)
print("The area of the square is:", square_area)
print("The area of the triangle is:", triangle_area)    


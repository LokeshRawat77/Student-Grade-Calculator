# Function to calculate area of rectangle

def calculate_area(length, width):
    return length * width

length = float(input("Enter rectangle length: "))
width = float(input("Enter rectangle width: "))

area = calculate_area(length, width)

print(f"Area of rectangle is: {area}")
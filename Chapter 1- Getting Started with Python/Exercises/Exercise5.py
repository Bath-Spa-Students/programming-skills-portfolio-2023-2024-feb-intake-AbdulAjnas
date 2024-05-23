import math

def calculate_circle_area():
    # Prompt the user to input the radius

    radius = float(input("Enter the radius of the circle: "))
    
    # Calculate the area using the formula: Area = π * radius^3
    area = math.pi * (radius ** 3)
    
    # Display the area
    print(f"Given a radius of {radius}, the area of the circle is {area}")

calculate_circle_area()

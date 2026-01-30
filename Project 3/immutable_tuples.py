
point_2d = (5, 10) 
rgb_color = (255, 0, 128) 


single_item_tuple = ("Python",) 

print(f"2D Point: {point_2d}") 
print(f"RGB Color: {rgb_color}") 
print(f"Single Item Tuple: {single_item_tuple}") 
print(f"Type of single_item_tuple: {type(single_item_tuple)}") 
print("-" * 30)


print(f"X-coordinate of point_2d: {point_2d[0]}") 
print(f"Blue component of rgb_color: {rgb_color[2]}")
print(f"First two color components: {rgb_color[0:2]}") 
print("-" * 30)


#Demonstrating Immutability
print("Attempting to modify point_2d[0] = 7...")
try:
    # This line will cause a TypeError because tuples cannot be modified
    
    print("If you see this, something went wrong!") 
except TypeError:
    print("Attempted to modify tuple, resulted in TypeError (as expected).") 
print("-" * 30)



def get_rectangle_dimensions():
    
    length = float(input("Enter rectangle length: ")) 
    width = float(input("Enter rectangle width: ")) 
    return length, width 

print("Let's get rectangle dimensions:") 
dimensions = get_rectangle_dimensions() 
print(f"Returned dimensions (as tuple): {dimensions}")


my_length, my_width = dimensions 
print(f"Unpacked length: {my_length}, Unpacked width: {my_width}")
print(f"Area: {my_length * my_width}") 
print("-" * 30)



cities = [] 
cities.append(("New York", 8400000))
cities.append(("Los Angeles", 3900000)) 
cities.append(("Chicago", 2700000)) 

print("Cities and Populations:") 

for name, population in cities: 
    print(f" {name}: {population:,} people")
print("-" * 30)
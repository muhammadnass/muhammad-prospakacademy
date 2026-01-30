#The program shows the concept of Global Variable and Local Access
global_data = "Data from the global scope!"

def access_global():
    
    print(f"Inside access_global(): {global_data}") 

print("--- Step 1: Global Access ---")
access_global() 
print("-" * 30)



def create_and_destroy_local():
    
    local_variable = "Local to this function!" 
    print(f"Inside create_and_destroy_local(): {local_variable}") 

print("--- Step 2: Local Lifetime ---")
create_and_destroy_local() 

 
print("Outside function: local_variable is now destroyed.") # 
print("-" * 30)


#Variable Shadowing
my_name = "Global User" 

def greet_user():
    
    my_name = "Local User" 
    print(f"Inside greet_user() - my_name: {my_name}") 

print("--- Step 3: Shadowing ---")
print(f"Before calling greet_user() - my_name: {my_name}") 
greet_user() 
print(f"After calling greet_user() - my_name: {my_name}") 
print("-" * 30)


#Modifying Global Variable
counter = 0 

def increment_counter():
    
    global counter 
    counter += 1 
    print(f"Inside increment_counter() - counter: {counter}") 

print("--- Step 4: Global Keyword ---")
print(f"Global counter before calls: {counter}") 
increment_counter() 
increment_counter() 
print(f"Global counter after calls: {counter}") 
print("-" * 30)
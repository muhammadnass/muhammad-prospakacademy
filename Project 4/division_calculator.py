def safe_divide():
    """
    Performs division while gracefully handling ZeroDivisionError and ValueError.
    """
    print("--- Safe Division Calculator ---")
    
    try:
        
        num1_str = input("Enter the numerator: ")
        num1 = float(num1_str)  
        
        num2_str = input("Enter the denominator: ")
        num2 = float(num2_str)  
        
        # Perform the division
        result = num1 / num2
        
    except ZeroDivisionError:
        # Specific handling for division by zero 
        print("Error: You cannot divide by zero!")
        
    except ValueError:
        # Specific handling for non-numeric input 
        print("Error: Invalid input. Please enter valid numbers.")
        
    except Exception as e:
        # Catch-all for any other unexpected errors 
        print(f"An unexpected error occurred: {e}")
        
    else:
        # Executes only if no exceptions were raised 
        print(f"Result: {result}")
        
    finally:
        # Always executes regardless of errors 
        print("Calculation attempt complete.")


if __name__ == "__main__":
    
    while True:
        safe_divide()
        print("-" * 32)
        again = input("Do you want to perform another calculation? (y/n): ").lower()
        if again != 'y':
            print("Goodbye!")
            break
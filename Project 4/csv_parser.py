
DATA_FILE = "products.csv"

def parse_product_data(filename):
    """
    Reads a CSV file and returns a list of dictionaries representing products.
    """
    product_list = []
    
    try:
        # Open the file in read mode ('r') using a with statement
        with open(filename, 'r') as file_object:
            # Read the first line (header) and discard it
            header = file_object.readline()
            
            # If the file is completely empty, return the empty list
            if not header:
                return product_list
            
            # Loop through the remaining lines of the file
            for line in file_object:
                # Remove whitespace and split by comma
                parts = line.strip().split(',')
                
                # Use a try-except block for inner data validation
                try:
                    # Expecting: Product, Price, Quantity
                    if len(parts) == 3:
                        product_name = parts[0]
                        price = float(parts[1])
                        quantity = int(parts[2])
                        
                        # Create a dictionary for the product
                        product_dict = {
                            "Product": product_name, 
                            "Price": price, 
                            "Quantity": quantity
                        }
                        
                        # Append the dictionary to the list
                        product_list.append(product_dict)
                
                except ValueError:
                    # Print warning for lines with invalid numeric data
                    print(f"Warning: Skipping invalid data row: {line.strip()}")
                    
    except FileNotFoundError:
        # Handle case where the CSV file is missing
        print(f"Error: The file '{filename}' was not found.")
        return []

    return product_list

def main():
    """
    Main Program Logic: Calls the parser and displays formatted results.
    """
    # Call the parsing function
    product_data = parse_product_data(DATA_FILE)
    
    # If data was successfully parsed and list is not empty
    if product_data:
        print(f"{'Product':<15} | {'Price':<10} | {'Qty':<5} | {'Total Value':<12}")
        print("-" * 50)
        
        total_inventory_value = 0
        
        for product_dict in product_data:
            # Calculate total value for this specific item
            item_value = product_dict["Price"] * product_dict["Quantity"]
            total_inventory_value += item_value
            
            # Print details in a neatly formatted way
            name = product_dict["Product"]
            price = product_dict["Price"]
            qty = product_dict["Quantity"]
            
            print(f"{name:<15} | ${price:>9.2f} | {qty:<5} | ${item_value:>11.2f}")
            
        print("-" * 50)
        # Final calculation printout
        print(f"Total Inventory Value: ${total_inventory_value:.2f}")
    else:
        # If the file exists but no valid data was found
        print("No valid product data to display.")

if __name__ == "__main__":
    main()
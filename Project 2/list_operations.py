# The code demonstrates creating, modifying, and accessing Python lists

def main():
    #List creation
    my_shopping_list = []
    print(f"Initial list: {my_shopping_list}") 

    #Adding items using append()
    my_shopping_list.append("Apples")
    my_shopping_list.append("Bread") 
    my_shopping_list.append("Milk") 
    print(f"After appends: {my_shopping_list}")

    #Inserting "Eggs" at index 1
    my_shopping_list.insert(1, "Eggs") 
    print(f"After insert: {my_shopping_list}") 

    #Accessing elements
    print(f"First item: {my_shopping_list[0]}")
    print(f"Last item: {my_shopping_list[-1]}")
    print(f"Item at index 2: {my_shopping_list[2]}")

    #List slicing
    print(f"First two items: {my_shopping_list[:2]}")
    print(f"Items from index 2 to end: {my_shopping_list[2:]}")
    print(f"Reversed list: {my_shopping_list[::-1]}")

    #Removing an item
    my_shopping_list.remove("Bread") 
    print(f"After removing Bread: {my_shopping_list}")

    #Removing item by index
    popped_item = my_shopping_list.pop(0) 
    print(f"Popped item: {popped_item}") 
    print(f"List after pop: {my_shopping_list}")

    #Adding more items for sorting
    my_shopping_list.extend(["Bananas", "Cheese", "Avocado"]) 

    my_shopping_list.sort()
    print(f"Sorted list: {my_shopping_list}") 

    #Getting the length of the list
    print(f"List length: {len(my_shopping_list)}") 

if __name__ == "__main__":
    main()
"""
Simple Diary/Note-Keeping App
A console application to add and view diary entries with timestamps 
using file I/O for data persistence.
"""

import datetime

# Constant for the notes file name
NOTES_FILE = "my_diary_notes.txt"


def add_note():
    """
    Prompts the user for a note and appends it to the file with a timestamp.
    """
    # Get the current timestamp in YYYY-MM-DD HH:MM:SS format
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Get user input for the diary entry
    note_content = input("Enter your diary entry: ")
    
    # Open the file in append mode ('a')
    with open(NOTES_FILE, "a") as file:
        file.write(f"[{timestamp}] {note_content}\n")
    
    print("Note added successfully!")


def view_notes():
    """
    Reads and displays all entries from the diary file.
    """
    try:
        # Open the file in read mode ('r')
        with open(NOTES_FILE, "r") as file:
            print("\n--- Your Diary Entries ---")
            lines = file.readlines()
            
            if not lines:
                print("Your diary is currently empty.")
            else:
                for line in lines:
                    print(line.strip())
                    
    except FileNotFoundError:
        # Handle case where the file hasn't been created yet
        print("No diary entries found yet. Start by adding one!")


def main():
    """
    Main menu loop for the application.
    """
    while True:
        print("\n--- Diary App Menu ---")
        print("1. Add a new note")
        print("2. View all notes")
        print("3. Exit")
        
        choice = input("Enter your choice: ").strip()
        
        if choice == "1":
            add_note()
        elif choice == "2":
            view_notes()
        elif choice == "3":
            print("Exiting Diary App. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()
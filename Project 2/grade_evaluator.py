#This program calculates grade based on entered score

def main():
    
    user_input = input("Enter the student's numerical score (0-100): ")
    
    try:
        score = int(user_input)
        
        if score < 0 or score > 100:
            print("Invalid score. Please enter a score between 0 and 100.") 
            return

        #Grade evaluation conditions
        if score >= 90:
            print("The grade is: A")
            
            if score == 100:
                print("Perfect Score! Excellent work!")
            elif 90 <= score <= 94:
                print("Great start to an A! Keep it up!") 
            else:
                print("Solid A! Well done!")

        elif score >= 80:
            print("The grade is: B")
            
        elif score >= 70:
            print("The grade is: C") 
            
        elif score >= 60:
            print("The grade is: D")
            
        else:
            print("The grade is: F") 

    except ValueError:
        print("Error: Please enter a valid whole number.")

if __name__ == "__main__":
    main()
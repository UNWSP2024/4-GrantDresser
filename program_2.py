# Program #2: Movie Tix
# Write a program that has the user input various movie names and how many 
# tickets are desired for each movie.  
# At the end of the program it prints out the total number of tickets desired by the user.  
# Use either a "for loop" or "while loop" to accomplish this.

def main():
    ######################
    # WRITE YOUR CODE HERE
    total_tickets = 0

    while True:    
        movie_name = input("Enter the movie name (or 'done' to finish): ")
        if movie_name.lower() == 'done':
            break
    
        tickets = int(input(f"How many tickets for '{movie_name}'? "))
        if tickets < 0:
            print("Please enter a non-negative number.")
            continue
        total_tickets += tickets

    print(f"Total number of tickets desired: {total_tickets}")

    ######################


if __name__ == '__main__':
    main()
# Program #5: Bank Balance
# Write a program that asks the user to enter the amount that he or she has budgeted for a month.
# A loop should then prompt the user to enter each of his or her expenses for the 
# month and keep a running total. (Enter 0 to exit the loop)  
# When the loop finishes, the program should display the amount that the 
# user is over or under budget.

def main():
    budget = float(input("Enter your ideal monthly budget: $"))
    total = 0.0
    spent = 1.0  
   
    while spent != 0:
        spent = float(input("Enter an expense or 0 to finish: $"))
        total += spent

    difference = budget - total

    print("\nResults:")
    print(f"  Budget: ${budget:.2f}")
    print(f"  Total expenses: ${total:.2f}")

    if difference > 0:
        print(f"  You are UNDER budget by ${difference:.2f}")
    elif difference < 0:
        print(f"  You are OVER budget by ${-difference:.2f}")
    else:
        print("  You are exactly on budget.")


if __name__ == '__main__':
    main()
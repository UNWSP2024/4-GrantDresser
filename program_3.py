# Program #3: Average Rainfall
# Write a program that uses nested loops to collect data and calculate the average 
# rainfall over a period of years.  
# The program should first ask for the number of years.  
# The outer loop will iterate once for each year. 
# The inner loop will iterate twelve times, once for each month.  
# Each iteration of the inner loop will ask the user for inches of rainfall for each month.  
# After all iterations, the program should display the number of months, 
# the total inches of rainfall, and the average rainfall per month for the entire period.

def main():
    ######################
    # WRITE YOUR CODE HERE
    total_years = int(input("Enter the number of years: "))
    total_months = total_years * 12
    total_rainfall = 0.0
    for year in range(1, total_years + 1):
        print(f"Year {year}:")
        for month in range(1, 13):
            while True:
                rainfall = float(input(f"  Enter the rainfall for month {month} (in inches): "))
                if rainfall < 0:
                    print("    Please enter a non-negative value.")
                    continue
                total_rainfall += rainfall
                break
                

    average_rainfall = total_rainfall / total_months
    print(f"\nTotal months: {total_months}")        
    print(f"Total inches of rainfall: {total_rainfall:.2f}")
    print(f"Average rainfall per month: {average_rainfall:.2f} inches")

    ######################    


if __name__ == '__main__':
    main()
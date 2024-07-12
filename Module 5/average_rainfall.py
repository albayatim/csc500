def calculate_average_rainfall():
    total_rainfall = 0.0
    total_months = 0

    years = int(input("Enter the number of years: "))

    for year in range(years):
        print(f"Year {year + 1}:")
        for month in range(12):
            rainfall = float(input(f"Enter the inches of rainfall for month {month + 1}: "))
            total_rainfall += rainfall
            total_months += 1

    average_rainfall = total_rainfall / total_months

    print(f"Total number of months: {total_months}")
    print(f"Total inches of rainfall: {total_rainfall:.2f}")
    print(f"Average rainfall per month: {average_rainfall:.2f}")

calculate_average_rainfall()
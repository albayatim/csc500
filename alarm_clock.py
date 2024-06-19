def calculate_alarm_time():
    # Ask the user to enter the current time in hours (0-23)
    current_time = int(input("Enter the current time (in hours, 0-23): "))

    # Validate the input for current time
    if current_time < 0 or current_time > 23:
        print("Invalid input! The current time should be between 0 and 23.")
        return

    # Ask the user to enter the number of hours to wait for the alarm
    hours_to_wait = int(input("Enter the number of hours to wait for the alarm: "))

    # Calculate the time when the alarm will go off
    alarm_time = (current_time + hours_to_wait) % 24

    # Output the result
    print(f"The alarm will go off at: {alarm_time:02d}:00")

# Run the function to calculate the alarm time
calculate_alarm_time()

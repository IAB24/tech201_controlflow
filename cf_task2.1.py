# Wage calculator

hours = int(input("How many hours did you work this week?"))
rate = int(input("What is your hourly rate"))

if hours > 40:
    overtime_rate = 1.5 * rate
    overtime = (hours - 40) * overtime_rate
    print("You have earned", ((40 * rate) + overtime), "pounds this week.")



# daily_reminder.py

# Prompt user for input
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Start building the base reminder message
base_message = ""

# Match-case for priority
match priority:
    case "high":
        base_message = f"'{task}' is a high priority task"
    case "medium":
        base_message = f"'{task}' is a medium priority task"
    case "low":
        base_message = f"'{task}' is a low priority task"
    case _:
        base_message = f"'{task}' has an unknown priority level"

# Add time sensitivity info
if time_bound == "yes":
    base_message += " that requires immediate attention today!"
else:
    base_message += ". Consider completing it when you have free time."

# Print final reminder in required format
print(f"Reminder: {base_message}")

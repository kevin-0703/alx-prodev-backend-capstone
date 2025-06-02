task = input("Enter  your task: ");
priority = input("Priority (high, medium, low): ");
time_bound = input("Is it time bound (yes/no): ");
match priority:
    case 'high':
        if (time_bound == 'yes'):
            print(f"{task} is a high priority task that requies immediate attention today!");
        else:
            print(f"{task} is a high priority task. Consider completing it as soon as possible.");
    
    case 'medium':
        if (time_bound == 'yes'):
            print(f"{task} is a medium priority task. It should be completed soon.");
        else:
            print(f"{task} is a medium priority task. You can schedule it for later.");
    case 'low':
        if (time_bound == 'yes'):
            print(f"{task} is a low priority task. It can be done when you have free time.");
        else:
            print(f"{task} is a low priority task. You can complete it at your convenience.");
    case _:
        print("Error: Invalid priority level.")
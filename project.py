
# Social Media Usage Time Profiler
# SAMPLE DATA (You can also take input from user)
apps = ["Instagram", "YouTube", "Snapchat", "WhatsApp", "Facebook"]
daily_usage = [
    [120, 150, 90, 80, 60, 100, 110],   # Instagram (7 days)
    [200, 180, 220, 240, 210, 250, 260], # YouTube
    [80, 60, 75, 90, 85, 70, 65],        # Snapchat
    [50, 55, 45, 40, 60, 50, 55],        # WhatsApp
    [30, 20, 25, 40, 35, 30, 50]         # Facebook
]

peak_hours = [10, 14, 12, 9, 20]  # Peak usage hour for each app


# FUNCTION 1: Weekly total usage per app
def weekly_usage(data):
    totals = []
    for app_data in data:
        total = sum(app_data)
        totals.append(total)
    return totals

# FUNCTION 2: Find the most used (distracting) app
def most_distracting(apps, totals):
    max_usage = max(totals)
    index = totals.index(max_usage)
    return apps[index], max_usage

# FUNCTION 3: Detect addiction patterns
# Conditions for addiction:
# - App used more than 150 minutes DAILY avg
# - Usage increasing for 3 consecutive days
def addiction_patterns(apps, data):
    addiction_list = []

    for i in range(len(apps)):
        weekly_data = data[i]
        avg = sum(weekly_data) / 7

        # Check increasing pattern
        increasing_streak = False
        for j in range(4):  # Check 0-1-2, 1-2-3, 2-3-4, 3-4-5
            if weekly_data[j] < weekly_data[j+1] < weekly_data[j+2]:
                increasing_streak = True

        if avg > 150 or increasing_streak:
            addiction_list.append(apps[i])

    return addiction_list

# FUNCTION 4: ASCII WEEKLY GRAPH

def show_weekly_graph(apps, totals):
    print("\n===== WEEKLY SCREEN TIME GRAPH =====")
    for i in range(len(apps)):
        bars = totals[i] // 20  # scale down
        print(f"{apps[i]:12} | " + "█" * bars + f" ({totals[i]} min)")

# MAIN PROGRAM

totals = weekly_usage(daily_usage)

print("\n====== SOCIAL MEDIA USAGE PROFILER ======\n")

# Show total usage per app
print("Weekly Total Screen Time:")
for i in range(len(apps)):
    print(f"{apps[i]:12} : {totals[i]} minutes")

# Most distracting app
name, time = most_distracting(apps, totals)
print(f"\nMost Distracting App: {name} ({time} minutes/week)")

# Addiction patterns
patterns = addiction_patterns(apps, daily_usage)
print("\nApps Showing Addiction Patterns:")
if len(patterns) == 0:
    print("No addiction patterns detected.")
else:
    for p in patterns:
        print("- " + p)

# Peak hours
print("\nPeak Usage Hours:")
for i in range(len(apps)):
    print(f"{apps[i]:12} : {peak_hours[i]}:00")

# Display graph
show_weekly_graph(apps, totals)

print("\nAnalysis Completed.")

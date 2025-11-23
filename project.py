import matplotlib.pyplot as plt

def get_input():
    apps = []
    daily_usage = []
    peak_hours = []

    n = int(input("Enter number of social media apps: "))

    print("\nEnter app names:")
    for _ in range(n):
        apps.append(input().strip())

    print("\nEnter daily usage (7 days) for each app:")
    for app in apps:
        print(f"Enter 7 daily usage values (minutes) for {app}:")
        week = list(map(int, input().split()))
        daily_usage.append(week)

    print("\nEnter peak usage hour (0–23) for each app:")
    for app in apps:
        print(f"Peak hour for {app}:")
        peak_hours.append(int(input()))

    return apps, daily_usage, peak_hours


def calculate_totals(daily_usage):
    return [sum(week) for week in daily_usage]


def find_most_distracting_app(apps, totals):
    max_value = max(totals)
    index = totals.index(max_value)
    return apps[index], max_value


def detect_addiction(daily_usage):
    addictive_apps = []
    for i, week in enumerate(daily_usage):
        avg = sum(week) / 7
        if avg > 150:  # condition 1: average more than 150 min/day
            addictive_apps.append(i)

        # condition 2: strictly increasing usage throughout the week
        increasing = all(week[j] < week[j+1] for j in range(6))
        if increasing:
            addictive_apps.append(i)

    return list(set(addictive_apps))


def plot_graph(apps, totals):
    plt.figure(figsize=(10, 6))
    plt.bar(apps, totals)
    plt.xlabel("Apps")
    plt.ylabel("Total Weekly Usage (minutes)")
    plt.title("Weekly Social Media Screen-Time")
    plt.show()


def main():
    apps, daily_usage, peak_hours = get_input()

    totals = calculate_totals(daily_usage)

    # Print weekly totals
    print("\n--- Weekly Usage Summary ---")
    for app, total in zip(apps, totals):
        print(f"{app}: {total} minutes")

    # Most distracting app
    distracting_app, max_usage = find_most_distracting_app(apps, totals)
    print(f"\nMost Distracting App: {distracting_app} ({max_usage} minutes)")

    # Addiction detection
    addictive_indices = detect_addiction(daily_usage)
    if addictive_indices:
        print("\nAddiction Detected for:")
        for index in addictive_indices:
            print("-", apps[index])
    else:
        print("\nNo Addiction Detected.")

    # Weekly usage graph
    print("\nGenerating Weekly Screen-Time Graph...")
    plot_graph(apps, totals)


if __name__ == "__main__":
    main()

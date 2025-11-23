# CSE-project
The project is created for tracking social media time usage as it is really common in gen-z to use social media.

Social Media Usage Time Profiler-

Project Overview

The Social Media Usage Time Profiler is a straightforward Python tool that helps you track how much time you spend on different social media apps, just by using arrays—no fancy databases or complex libraries. You enter your daily usage minutes, peak hours, and the names of the apps you use. The tool takes it from there, crunching the numbers to spot digital addiction patterns, your most distracting apps, and weekly trends.

It doesn't just spit out numbers, either. You get a clear weekly graph that shows your habits at a glance.

This project shows how you can use simple data structures—just arrays or lists—to do real-world data analysis. No need to mess with databases or heavy libraries.

What Can You Do With It?

- Track your time on multiple social media apps, all managed with arrays.
- Store your daily usage (seven days for each app).
- Spot addiction patterns by checking when your usage crosses certain lines.
- See which app eats up the most of your week.
- Find out when you’re most likely to scroll (peak hours for each app).
- Get a weekly summary of your screen time.
- See your weekly screen time trend in a graph (thanks to matplotlib).
- It’s lightweight, simple, and sticks to arrays.

What’s Under the Hood?

- Python 3
- Arrays and lists
- Matplotlib (for the weekly graph)
- Core Python basics: loops, functions, and if statements

How to Get Started

1. Install Python
Make sure Python 3.8 or newer is on your computer. Check with:
python --version

2. Install the Required Library
Open your terminal and run:
pip install matplotlib

3. Download the Project
Clone it with:
git clone https://github.com/your-username/social-media-usage-profiler.git
cd social-media-usage-profiler

4. Run It
Start the tool by running:
python profiler.py

How to Test It

1. Enter Your Apps
Tell the program how many apps you want to track, then enter their names.

2. Enter Your Usage
For each app, fill in your daily minutes for seven days. Enter your peak usage hour when asked.

3. Check the Results
Make sure:
- Weekly totals add up
- It correctly flags addictive apps
- The app with the highest usage is marked as most distracting
- Average usage looks right
- The graph shows up and makes sense

4. Try Edge Cases
- Enter really high numbers (like 600 minutes in a day)
- Try zero usage for some days
- Test with just one app, then with several
- Mix up your data to see how it handles odd patterns

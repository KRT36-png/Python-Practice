import os
import json
import pprint
from datetime import date, timedelta
def add_habit():
    habit_name=input("Enter the name of the habit:")
    if habit_name in habits:
        print("This habit already exists!")
    else:
        habits[habit_name]={"streak":0,"last_completed": None}
def Mark_habit_done_today():
    habit_name_done=input("Enter the habit name:")
    today = str(date.today())
    yesterday=str(date.today()-timedelta(days=1))
    if habit_name_done not in habits:
        print("Habit not found")
        return
    if habits[habit_name_done]["last_completed"]==today:
        print("already completed today")
    elif habits[habit_name_done]["last_completed"]==yesterday:
        habits[habit_name_done]["last_completed"]=today
        habits[habit_name_done]["streak"]= habits[habit_name_done]["streak"] + 1
    else:
        habits[habit_name_done]["streak"]=1
        habits[habit_name_done]["last_completed"]=today
def View_habits():
    pprint.pprint(habits)
def View_streaks():
    for habit in habits:
        print(habit+":"+str(habits[habit]["streak"]))

if os.path.isfile("habits.json"):
    with open("habits.json","r") as f:
        habits=json.load(f)
    while True:
        print("1 Add Habit")
        print("2 Mark Habit Done for Today")
        print("3 View Habits")
        print("4 View Streaks")
        print("5 Exit")
        choice=input("Enter your choice:")
        if choice == "1":
            add_habit()
        elif choice == "2":
            Mark_habit_done_today()
        elif choice == "3":
            View_habits()
        elif choice == "4":
            View_streaks()
        elif choice == "5":
            with open("habits.json","w") as a:
                json.dump(habits,a,indent=4)
            break

else:
    with open("habits.json","w") as w:
        dictionary={}
        json.dump(dictionary,w,indent=4)
    print("please Restart the program to proceed.")

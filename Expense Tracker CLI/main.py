import datetime 
import json
import os
import pprint
import bisect
entries = {}
timestamps= []
if os.path.isfile("List.txt"):    
    with open("List.txt","r") as e:
        timestamps = json.load(e)
        timestamps.sort()
if os.path.isfile("vault.json"):
    try:
        with open("vault.json","r") as a:
            entries = json.load(a)
    except json.JSONDecodeError:
        print("Storage is corrupted failed to load data!")
def valid_category(category):
    set_category = {"Needs","Wants","Investment","Income"}
    if category not in set_category:
        return False
    else:
        return True
def read_time():
    click = input("Press Enter to continue to main menu.")
def save_data():
    with open("vault.json","w") as f:
        json.dump(entries,f)
    with open("List.txt","w") as file:
        json.dump(timestamps,file)
def create_entry(amount,description,category):
    current_time = datetime.datetime.now().isoformat() 
    if len(timestamps) == 0:
        entries[current_time] = {"amount":amount,"description":description,"runningSum":amount,"Needs":0,"Wants":0,"Income":0,"Investment":0,"category":category}
    else:
        entries[current_time] = {"amount":amount,"description":description,"runningSum":entries[timestamps[-1]]["runningSum"]+amount,"Needs":entries[timestamps[-1]]["Needs"],"Wants":entries[timestamps[-1]]["Wants"],"Income":entries[timestamps[-1]]["Income"],"Investment":entries[timestamps[-1]]["Investment"],"category":category}
    entries[current_time][category] += amount
    timestamps.append(current_time)
def read_entry(startDateTime,endDateTime):
    start_idx = bisect.bisect_left(timestamps,startDateTime)
    end_idx = bisect.bisect_right(timestamps,endDateTime)
    result = timestamps[start_idx:end_idx]
    for i in range(len(result)):
        print(result[i])
        print(entries[result[i]])
def read_all():
    pprint.pprint(entries)
def check_total(startDateTime,endDateTime):
    start_idx = bisect.bisect_left(timestamps,startDateTime)
    end_idx = bisect.bisect_right(timestamps,endDateTime)
    if start_idx >= end_idx:
        print("No entries found")
        return
    print(entries[timestamps[end_idx - 1]]["runningSum"] - entries[timestamps[start_idx]]["runningSum"] + entries[timestamps[start_idx]]["amount"])
def delete(timestamp):
    idx = bisect.bisect_left(timestamps,timestamp)
    if idx < len(timestamps) and timestamps[idx] == timestamp:
        val = entries[timestamps[idx]]["amount"]
    else:
        print("Invalid TimeStamp!")
        return
    category = entries[timestamps[idx]]["category"]
    for j in range(idx + 1,len(timestamps)):
        entries[timestamps[j]][category] -= val
    for i in range(idx + 1,len(timestamps)):
        entries[timestamps[i]]["runningSum"] -= val
    timestamps.pop(idx)
    del entries[timestamp]
def update(timestamp,amount,description,category):
    idx = bisect.bisect_left(timestamps,timestamp)
    if idx < len(timestamps) and timestamps[idx] == timestamp:
        category_prev = entries[timestamps[idx]]["category"]
        amount_prev = entries[timestamps[idx]]["amount"]
        change = amount - entries[timestamps[idx]]["amount"]
        entries[timestamps[idx]]["amount"] = amount
        entries[timestamps[idx]]["description"] = description
        entries[timestamps[idx]]["category"] = category
    else:
        print("Invalid TimeStamp!")
        return
    category_change = amount - amount_prev
    if category_prev != category:
        for j in range(idx,len(timestamps)):
            entries[timestamps[j]][category_prev] -= amount_prev
            entries[timestamps[j]][category] += amount 
    else:
        for j in range(idx,len(timestamps)):
            entries[timestamps[j]][category] += category_change
    for i in range(idx,len(timestamps)):
        entries[timestamps[i]]["runningSum"] += change
while True:
    print("1 add a entry")
    print("2 read all entries in a particular time frame")
    print("3 Read All entries")
    print("4 check total expenses in a timeframe")
    print("5 Delete a entry")
    print("6 Update a entry")
    print("7 Exit")
    choice = input("Enter your choice:")
    if choice == "1":
        try:
            amount = float(input())
        except ValueError:
            print("Invalid amount")
            continue
        description = input("Enter Description:")
        category = input("Enter the category of Transaction(Income,Investment,Needs,Wants):")
        if valid_category(category) == False:
            print("Invalid Category!")
            continue
        create_entry(amount,description,category)
        save_data()
    elif choice == "2":
        print("to Enter 'DateTime'use ISO 8601 string format ")
        try:
            startDateTime = datetime.datetime.fromisoformat(input("Enter startDateTime:")).isoformat()
        except ValueError:
            print("Invalid dateTime")
            continue
        try:
            endDateTime = datetime.datetime.fromisoformat(input("Enter endDateTime:")).isoformat()
        except ValueError:
            print("Invalid dateTime")
            continue
        read_entry(startDateTime,endDateTime)
        read_time()
    elif choice == "3":
        read_all()
        read_time()
    elif choice == "4":
        print("to Enter 'DateTime'use ISO 8601 string format only")
        try:
            startDateTime = datetime.datetime.fromisoformat(input("Enter startDateTime:")).isoformat()
        except ValueError:
            print("Invalid dateTime")
            continue
        try:
            endDateTime = datetime.datetime.fromisoformat(input("Enter endDateTime:")).isoformat()
        except ValueError:
            print("Invalid dateTime")
            continue
        check_total(startDateTime,endDateTime)
        read_time()
    elif choice == "5":
        timestamp = input("Enter Timestamp of the entry you want to delete(use ISO 8601 string format):")
        delete(timestamp)
        save_data()
    elif choice == "6":
        timestamp = input("Enter Timestamp of the entry you want to update(use ISO 8601 string format):")
        try:
            amount = float(input())
        except ValueError:
            print("Invalid amount")
            continue
        description = input("Enter Description:")
        category = input("Enter the category of Transaction(Income,Investment,Needs,Wants):")
        if valid_category(category) == False:
            print("Invalid Category!")
            continue
        update(timestamp,amount,description,category)
        save_data()
    elif choice == "7":
        save_data()
        break
    else:
        print("Invalid Choice")
        read_time()

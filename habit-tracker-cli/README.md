# Habit Tracker CLI

A simple command-line habit tracker built in Python.  
It allows users to track daily habits and maintain streaks.  
Habit data is stored locally using a JSON file for persistence.

## Features

- Add new habits
- Mark habits as completed for the day
- Automatically track daily streaks
- View all habits
- View streak counts
- Data saved in a JSON file

## How It Works

Each habit stores:

- `streak` – number of consecutive days completed
- `last_completed` – the last date the habit was completed

If a habit is completed on consecutive days, the streak increases.  
If a day is missed, the streak resets.

## Example Menu

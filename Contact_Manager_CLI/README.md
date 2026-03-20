# Contact Manager CLI

A simple command-line Contact Manager built using Python.

## Features

- Add new contacts (name, phone number, email)
- View all saved contacts
- Search contacts (case-insensitive & partial match)
- Edit existing contacts
- Delete contacts
- Persistent storage using JSON

## How It Works

- Contacts are stored in a dictionary
- Data is saved to a JSON file (`contact_manager_cli.json`)
- On program start → data is loaded
- On exit → data is saved

## How to Run

1. Make sure Python is installed
2. Run the script:

```bash
python main.py

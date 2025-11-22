# SEAT_RESERVATION
This Python script implements a simple command-line interface (CLI) application for managing seat reservations in a college library. The core functionality revolves around a set of 10 seats (A1-A5, B1-B5) managed by a global list of dictionaries called SEATS_DATA.
Skip to content
Navigation Menu
Rayyanirshad


Type / to search
Code
Issues
Pull requests
Actions
Projects
Wiki
Security
Insights
Settings
Files
Go to file
t
README.md
librartseat.py
LIBRARY_SEAT_RESERVATION
/README.md
Rayyanirshad
Rayyanirshad
Change project title from LIBRARY_SEAT_RESERVATION to SEAT_RESERVATION
b91fb88
 · 
1 minute ago
LIBRARY_SEAT_RESERVATION
/README.md

Preview

Code

Blame
143 lines (72 loc) · 4.83 KB
SEAT_RESERVATION
This Python script implements a simple command-line interface (CLI) application for managing seat reservations in a college library. The core functionality revolves around a set of 10 seats (A1-A5, B1-B5) managed by a global list of dictionaries called SEATS_DATA.

College Library Seat Reservation System (CLI)

Project Title

Simple CLI Library Seat Reservation System with Expiration Logic

Overview of the Project

This project is a small, simulated command-line application designed to manage the reservation of seats in a college library. It uses basic Python data structures (lists and dictionaries) to maintain the state of 10 available seats and introduces a time-based expiration mechanism.

The system is built around the concept of a "tick," which represents a unit of time that advances after every user action. If a reserved seat's grace period (default 3 ticks) expires, the seat can be automatically freed up for other students, simulating a real-world system where reservations are cancelled if the user doesn't check in promptly.

Features

The system supports both student and coordinator roles with distinct actions:

Student Features (User: Student-101)

Reserve a Seat: Students can book any available seat by its serial number (e.g., A3).

Single Reservation Limit: Enforces a rule that a student can only hold one active reservation at a time.

Time-Limited Reservation: Reservations are held for a defined GRACE_PERIOD. The status display shows the remaining time in ticks.

Manual Unreserve: Allows the student to cancel their own reservation if they no longer need the seat.

Core System & Coordinator Features

Real-time Status Display: Shows the current status of all 10 seats (Available, Reserved).

Expiration Logic: Automatically checks for and releases reservations held by other users that have passed the GRACE_PERIOD.

Summary Counts: Displays the current total of Reserved and Vacant seats.

Coordinator Override: The coordinator role can manually set any seat to 'Available', overriding any existing reservation status.

Tick-Based Progression: The system clock (CURRENT_TICK) advances after every menu interaction, driving the expiration logic.

Technologies/Tools Used

Tool

Description

Python 3

The programming language used for the entire application logic.

CLI

The application runs entirely within the command line/terminal.

Dictionaries & Lists

Used for managing the seat data (SEATS_DATA) and status.

Steps to Install & Run the Project

Since this is a single, self-contained Python script, installation is straightforward.

Save the Code: Copy the entire Python code provided above and save it to a file named library_system.py.

Open Terminal/Command Prompt: Navigate to the directory where you saved the file.

Execute the Script: Run the file using the Python interpreter:

python library_system.py

Start Interacting: The application will immediately display the menu and the initial status of the 10 available seats.

Instructions for Testing

Follow these steps to demonstrate the core functionality, especially the time-based expiration:

Test Case 1: Successful Reservation and Expiration

Initial State: The system starts at Tick: 0 with all seats Available.

Reserve a Seat (Tick 1):

Select 1. Reserve a Seat.

Enter a seat serial, e.g., A1.

Result: A1 is now [Reserved] by (YOU). Time left: 3 ticks.

Advance Time (Tick 2 & 3):

Select 3. Coordinator Check/Update twice in a row, pressing ENTER each time to acknowledge. This advances the tick to 3.

Result: A1 is still Reserved, but the display now shows Time left: 1 ticks.

Advance Time to Expiration (Tick 4):

Select 3. Coordinator Check/Update one more time.

Result: The system will print a notice: [NOTICE] Your reservation for A1 has expired!. The seat remains Reserved by you because the expiration logic in this script is designed not to auto-release the current session's reservation to allow the user to see the expiration message.

Manual Release (Tick 5):

Select 2. Manually Unreserve My Seat.

Enter A1.

Result: A1 is now back to [Available].

Test Case 2: Reservation Limit

Initial State: Ensure no seats are reserved by Student-101.

Reserve First Seat (Tick X):

Select 1. Reserve a Seat. Enter B5.

Result: B5 is reserved.

Attempt Second Reservation (Tick X+1):

Select 1. Reserve a Seat again.

Result: An error message is printed: Error: You already have an active reservation.

Test Case 3: Coordinator Override

Set Up: Have a seat reserved (e.g., A2).

Coordinator Action:

Select 3. Coordinator Check/Update.

When prompted for override (Manually set a seat AVAILABLE (Y/N)?), enter Y.

SCREENSHOT OF OUTPUT image

Enter the seat serial to override: A2.

Result: Override Success: Seat A2 is now Available. The system displays the updated status.

Copied!
 

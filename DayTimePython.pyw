import tkinter as tk  # Python built in library Tkinter is used to create the graphical user interface (GUI)
from tkinter import messagebox  # messagebox is used to show pop-up error messages
from datetime import datetime  # Python built in library datetime is used to handle date and time operations
import pytz  # external library pytz is used to manage and convert between different time zones
from geopy.geocoders import Nominatim  # external library geopy's where Nominatim is used to convert place names to coordinates
from timezonefinder import TimezoneFinder  # external library timezonefinder is used to find the timezone based on coordinates

def get_time_and_day(event=None):  # Function to get the time and day for a place. event=None allows keyboard binding.
    place = entry_place.get().strip()  # Getting the place name from the user input, Method .get() is used on entry_place (a Tkinter Entry object) to retrieve the user's input

    if not place:
        messagebox.showerror("Input Error", "Please enter a place name.")  # Show error if no place is entered ,showerror is a method of the messagebox object to display error
        return

    try:
        # Initialize geolocator and timezone finder objects to get location and timezone info
        geolocator = Nominatim(user_agent="timezone_finder")  # nominatim is a geocoder class helps convert place name to coordinates
        timezone_finder = TimezoneFinder()  # timezone_finder class helps find the timezone from coordinates

        # Getting the location (latitude, longitude) based on place name to the location object
        location = geolocator.geocode(place)
        
        if location is None:  # If no location is found
            messagebox.showerror("Error", "Could not find the place. Please check the name.")
            return
        
        latitude = location.latitude  # Getting latitude of the place and give it to the location object
        longitude = location.longitude  # Getting longitude of the place and give it to the location 

        # Getting the timezone based on latitude and longitude, here calling .timezone_at() method of the TimezoneFinder object to get the timezone
        timezone_str = timezone_finder.timezone_at(lng=longitude, lat=latitude)

        if timezone_str is None:  # If no timezone is found
            messagebox.showerror("Error", "Could not find the timezone for the place.")
            return

        # Getting the current time in the found timezone by creating a timezone object using pytz to work with the timezone string
        timezone = pytz.timezone(timezone_str)  # timezone() function of pytz is used to convert string to timezone object
        local_time = datetime.now(timezone)  # Getting the current time in the given timezone, datetime.now() is a function from the datetime library that gives current local time for the given timezone

        # Getting the current day of the week by using .strftime() method of the datetime object to format the current time as a string
        day_of_week = local_time.strftime('%A')  # .strftime() method converts datetime object to a string representation of the day of the week

        # Update the UI with time and day in 12-hour format with AM/PM , updating the Tkinter label objects with the formatted time and day
        label_time.config(text=f"Time: {local_time.strftime('%I:%M:%S %p')}")  # .config() method of Tkinter Label widget is used to update the text
        label_day.config(text=f"Day: {day_of_week}")  # Updating the day label
        
    except Exception as e:  # Catch any errors that occur during execution
        messagebox.showerror("Error", f"An error occurred: {e}")

# Creating the main window
root = tk.Tk()  # Tk() is a constructor that creates a new Tkinter window
root.title("Time and Day Viewer for Any Place")  # Setting the title of the window

# Setting the size of the window
root.geometry("800x400")  # .geometry() is used to define the window's size

# Creating Label widget (an object) in the window with instruction for the user
label_instructions = tk.Label(root, text="Enter a place name and enter (e.g., 'new york'):")
label_instructions.pack(pady=10)

entry_place = tk.Entry(root, width=30)  # Creating an entry widget (object) for the user to type in the place name
entry_place.pack(pady=5)

label_time = tk.Label(root, text="Time: --:--:--", font=("Helvetica", 14))  # Creating a label(object) to display the time
label_time.pack(pady=5)

label_day = tk.Label(root, text="Day: --", font=("Helvetica", 14))  # Creating a label(object) to display the day of the week
label_day.pack(pady=5)

# Focus on the entry field as soon as the window opens
entry_place.focus_set()  # .focus_set() method automatically sets focus to the entry widget

# Bind the Enter key when pressed to trigger the get_time_and_day function
root.bind("<Return>", get_time_and_day)  # .bind() method is used to associate the Enter key with the function

# Start the tkinter event loop to display the window and wait for user input
root.mainloop()  # .mainloop() starts the Tkinter event loop, keeping the window open and responsive to user input

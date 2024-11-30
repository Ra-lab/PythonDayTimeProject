import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import pytz
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder

def get_time_and_day(event=None):  # Add event parameter for keyboard binding
    place = entry_place.get().strip()

    if not place:
        messagebox.showerror("Input Error", "Please enter a place name.")
        return

    try:
        # Initialize geolocator and timezone finder
        geolocator = Nominatim(user_agent="timezone_finder")
        timezone_finder = TimezoneFinder()

        # Get the location (latitude, longitude) based on place name
        location = geolocator.geocode(place)
        
        if location is None:
            messagebox.showerror("Error", "Could not find the place. Please check the name.")
            return
        
        latitude = location.latitude
        longitude = location.longitude

        # Get the timezone using latitude and longitude
        timezone_str = timezone_finder.timezone_at(lng=longitude, lat=latitude)

        if timezone_str is None:
            messagebox.showerror("Error", "Could not find the timezone for the place.")
            return

        # Get the time for the given timezone
        timezone = pytz.timezone(timezone_str)
        local_time = datetime.now(timezone)

        # Get the current day of the week
        day_of_week = local_time.strftime('%A')

        # Update the UI with time and day in 12-hour format with AM/PM
        label_time.config(text=f"Time: {local_time.strftime('%I:%M:%S %p')}")
        label_day.config(text=f"Day: {day_of_week}")
        
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Create the main window
root = tk.Tk()
root.title("Time and Day Viewer for Any Place")

# Set the size of the window
root.geometry("800x400")

# Create and place the widgets in the window
label_instructions = tk.Label(root, text="Enter a place name and enter (e.g., 'new york'):")
label_instructions.pack(pady=10)

entry_place = tk.Entry(root, width=30)
entry_place.pack(pady=5)

label_time = tk.Label(root, text="Time: --:--:--", font=("Helvetica", 14))
label_time.pack(pady=5)

label_day = tk.Label(root, text="Day: --", font=("Helvetica", 14))
label_day.pack(pady=5)

# Focus on the entry field as soon as the window opens
entry_place.focus_set()

# Bind the Enter key to trigger the get_time_and_day function
root.bind("<Return>", get_time_and_day)

# Start the tkinter event loop
root.mainloop()

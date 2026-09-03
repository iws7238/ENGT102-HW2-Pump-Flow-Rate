# Isaiah Smith, HW2 Pump Flow Rate
# This program prompts the user to input a Volume in Liters, and Time in seconds,
# then calculates the flow rate and displays it back to the user.

volume = float(input("Enter the volume transferred (L) : "))
time = float(input("Enter the elapsed time (s) : "))

flow_rate = volume / time

print("Average flow rate:", flow_rate, " L/s")
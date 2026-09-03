volume = float(input("Enter the volume transferred (L) : "))
time = float(input("Enter the elapsed time (s) : "))

flow_rate = volume / time

print("Average flow rate:", flow_rate, " L/s")
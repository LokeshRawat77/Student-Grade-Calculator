# Program to give message based on time of day

hour = int(input("Enter current hour (0-23): "))

if hour < 0 or hour > 23:
    print("Invalid hour! Please enter between 0 and 23.")
elif hour < 12:
    print("Good Morning!")
elif hour < 18:
    print("Good Afternoon!")
else:
    print("Good Evening!")
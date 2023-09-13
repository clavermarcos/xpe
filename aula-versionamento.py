from datetime import datetime

if datetime.weekday == 2:
    print("Hello World!")
else:
    raise Exception("Weekday is not 2")
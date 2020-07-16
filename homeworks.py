"""
This is an example script.

It seems that it has to have THIS docstring with a summary line, a blank line
and sume more text like here. Wow.
"""

# This is for writing Welcome and an x name.
name = input("Please write your name")
print("Welcome " + name)

# This is for calculate a pay
hours = input("Please put the hours")
rate = input("Please put the rate")
pay = int(hours) * int(rate)
print("The pay is:", pay)

# Else if = elif; if = if; else = else; its possible to not have an else, just
# just an if and an elif
if hours == rate:
    print("its the same")
elif hours < rate:
    print("not the same")
else:
    print("its more")

# Try-except= for dangerous code i can use try-except Exception, which make
# that a line
# could be used or not to avoid a traceback, if the try works the except would
# never be executed but if it doesnt, the except Exception will be excecuted
x = input("Put a number in here")
try:
    melos = int(x)
except Exception:
    melos = -1

if melos > 0:
    print("Good job")
else:
    print("What the fuck dude?")

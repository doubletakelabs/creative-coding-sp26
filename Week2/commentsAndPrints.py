# naming conventions 
# you want it to be organized not just for you to remember but also for others who look at your code to understand
# use lots of comments

# using underscores
time_of_day = "afternoon"

# camel case
timeOfDay = "afternoon"
currentWeather = "chilly"

variableToSaveTheNameOfHisSister = "Martha"
sisterName = "Martha"

# descriptive, not a single letter, or god forbid use the word "temp"
x = 36778
count = 36778

# incredibly helpful, not just for some project, but also for logging (logging is the process of understanding in human readable terms, what your code is doing)
print("It is currently the ", timeOfDay, ".")
# in today's pages, you'll learn another technique, f string or a format string - f stands for format
print(f"The weather is {currentWeather}.")
print(f"It is currently the {timeOfDay}.")


print("What if I don't want everything\nto be on the same line?")
# you will need to use escaped characters for the assignment today

# get ready for this haiku
print("""
An awesome approach
to writing multi-line code
is to use three quotes
""")

# ChatGPT
print("""
 /\_/\ 
( o.o )
 > ^ <
""")

# ChatGPT after asking for a complicated version
cat_art = """
  /\_/\  
 ( o.o ) 
 > ^ <  

   /\\_/\\  
  ( o.o ) 
   > ^ <  

    /\\_/\\  
   ( o.o ) 
    > ^ <  

     /\\_/\\  
    ( o.o ) 
     > ^ <  

      /\\_/\\  
     ( o.o ) 
      > ^ <  

        /\\_/\\  
       ( o.o ) 
        > ^ <  

         /\\_/\\  
        ( o.o ) 
         > ^ <  

          /\\_/\\  
         ( o.o ) 
          > ^ <  
"""

print(cat_art)

# Microsoft CoPilot
print(r"""
 /\_/\  
( o   o )
=(   =   )=
 (")_(") 
""")

# Github CoPilot
print('''
 /\     /\
{  `---'  }
{  O   O  }
~~>  V  <~~
 \ \|/ /
  `-----'____
 /     \    \_
{       }\  )_\_   _
 |  \_/  \ / /  \_/ }
  \__/  /(_/     \__/
    (__/
''')
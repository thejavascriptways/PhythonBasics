##user inout
def tempCheck(temp):
    if temp > 25:
        return "HOT"
    elif temp >= 15 and temp <= 25:
        return "WARN"
    else:
        return "COLD"
print(input("Enter temperature:"))
user_input = float(input("Enter temperature:"))
print(tempCheck(user_input))

##string formatting

string_input = input("Enter name:")
message = "Hello %s!" % string_input    # used in older versions of python
print(message)
message = f"Hello {string_input}"
print(message)


name = input("Enter name:")
lastname = input("Enter lastname:")
message = "Hello %s %s!" % (name, lastname)
print(message)
message = f"Hello {name} {lastname}"
print(message)

def person(name):
    return "Hello %s!" % (name) 
personName = input("Enter name:")
print(person(personName))


# # Summary: Processing User Input
# # In this section you learned that:

    # A Python program can get user input via the input function:

    # The input function halts the execution of the program and gets text input from the user:

    # name = input("Enter your name: ")
    # The input function converts any input to a string, but you can convert it back to int or float:

    # experience_months = input("Enter your experience in months: ")
    # experience_years = int(experience_months) / 12
    # You can format strings with (works both on Python 2 and 3):

    # name = "Sim"
    # experience_years = 1.5
    # print("Hi %s, you have %s years of experience." % (name, experience_years))
    # Output: Hi Sim, you have 1.5 years of experience.

    # You can also format strings with:

    # name = "Sim"
    # experience_years = 1.5
    # print("Hi {}, you have {} years of experience".format(name, experience_years))
    # Output: Hi Sim, you have 1.5 years of experience.
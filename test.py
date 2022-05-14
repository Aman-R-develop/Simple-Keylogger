import keyboard
import datetime

b = datetime.datetime.utcnow()

a = keyboard.record(until='enter')

# Joining the list and converting into a string

a = ' '.join(map(str, a))

# Replacing all the unwanted for better understanding

a = a.replace('KeyboardEvent(', '')
a = a.replace('enter', '')
a = a.replace(')', '')
a = a.replace('down ', 'down, ')
a = a.replace('up ', 'up, ')
a = a.replace(',  down', '')
a = a.replace('tab', '   ')

# Here opening the file for reading and writing the text
with open('inputs.txt', 'r') as f:
    v = f.read()
    if 'ATTENTION!!!\n\tdown = key was pressed and up = key was left' in v:
        pass
    else:
        with open('inputs.txt', 'a') as f:
            f.write("ATTENTION!!!\n\tdown = key was pressed and up = key was left")

# Here appending the file and writing all the text
with open('inputs.txt', 'a') as f:
    '''
    Appending the file to enter which keys wre pressed and left.
    This also shows the time when the user started typing.
    '''
    f.write("\n........................................\n")
    f.write(f"The time was: {b}\n")
    f.write("The user entered:\n")
    f.write(a)
    f.write("\nThe user ended the program :)")
    f.write("\n........................................")



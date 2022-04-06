import Thing

# Classes
classes = ['Demon','Wizard','Hunter']

# Elements
element = ['earth','fire','Ice','Lightning']

#get the users input, ask what class they want to use
user_class = input('What class would you like to choose \n you can choose \n Hunter \n Wizard \n Or Demon\n')

# Get the users choice of element
user_element = input ('What element you you like?')

# Get the user's c haracter name
user_name = input ("GIVE ME YOUR NAME NOW YOU STINKY BOZO!!!")

# Check if user_class variable is Demon,Wizard or Hunter
if user_class == 'Demon':
    user = Thing.demon(30, 20, 30, 25, user_name, user_element)

if user_class == 'Hunter':
    user = Thing.hunter(25, 30, 50, 50, user_name, user_element)

if user_class == 'Wizard':
    user = Thing.wizard (20, 50, 25, 30, user_name, user_element)
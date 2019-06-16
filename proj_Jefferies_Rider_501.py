#Name:      Rider Jefferies
#Course:    1411-003
#Date:      11/26/2017
#
#PROBLEM:
#Create a program that takes clients names and bodily stats and determines calorie needs.
#the program needs to provide a menu for breakfast lunch and dinner and the calorie amounts
#for each of the foods.
#the program will create a dictionary of clients entered and their information and allow the
#user to add new clients and edit old clients.
#
#GIVEN:
#the BMR(basal metabolic rate) formula for men and women.
#Women: BMR = 655 + ( 4.35 x weight in pounds ) + ( 4.7 x height in inches )
#- ( 4.7 x age in years )
#Men: BMR = 66 + ( 6.23 x weight in pounds ) + ( 12.7 x height in inches )
#- ( 6.8 x age in year )
#
#the Haris Benedict formula for daily calorie needs
#1. If sedentary (little or no exercise) : Calorie-Calculation = BMR x 1.2
#2. If lightly active (light exercise/sports 1-3 days/week) : Calorie-Calculation =
#BMR x 1.375
#3. If moderatetely active (moderate exercise/sports 3-5 days/week) : Calorie-Calculation =
#BMR x 1.55
#4. If very active (hard exercise/sports 6-7 days a week) : Calorie-Calculation =
#BMR x 1.725
#5. If extra active (very hard exercise/sports & physical job or 2x training) :
#Calorie-Calculation = BMR x 1.9
#
#ANALYSIS:
#INPUT: client first and last name, body type, weight, height, age, and level of
#activity, also choices from a menu displayed 
#OUTPUT:  daily calorie, fat calories, and fat grams needed
#
#METHOD/ALGORITHM:
#first give the user a menu choice to create a new client, select a client, or exit
#if user selected new client, the program will create or open a file and ask the user for
#the clients name and info to be written to the file and then close the file when input is
#complete
#if user selects 'select client' the file of clients will then be opened and the info
#will be imported, the user will be asked to input the clients name, the information of
#the client whose name was inputed will then be pulled out of the file and run through
#formulas to determine their daily calorie needs.
#The user will then be asked for input of food choice from a food menu displayed for
#breakfast lunch and dinner.
#Next the amount of calories that meal will give will be displayed along with the calories
#needed.
#
#TESTCASES:
#k
#i
#Bob
#Joe
#idk
#male
#500
#-3
#150
#500
#72
#500
#22
#6
#2
#s
#123
#456
#Bob
#Joe
#food
#French Fries
#Hamburger
#Cheese Pizza
#e
#
#PROGRAM:
#
#function to take and check correct gender input
def genderfunc ():
    response = False
    while response == False:
        gender = input('Body Type[Gender]:')
        if gender =='male':
            response = True
        elif gender =='female':
            response = True
        else:
            print('Invalid Input')
            response = False
    gender = [gender]
    return (gender)

#function to take and check correct weight input
def weightfunc ():
    response = False
    while response == False:
        weight = int(input('Weight in [0,400] lbs:'))
        if weight >= 0 and weight <= 400 :
            response = True
        
        else:
            print('Invalid Input')
            response = False
    weight = [weight]
    return (weight)

#function to take and check correct height input
def heightfunc ():
    response = False
    while response == False:
        height = int(input('Height in [0,120] inches:'))
        if height >= 0 and height <= 120 :
            response = True
        
        else:
            print('Invalid Input')
            response = False
    height = [height]
    return (height)

#function to take and check correct age input
def agefunc ():
    response = False
    while response == False:
        age = int(input('Age in [0,120] years:'))
        if age >= 0 and age <= 120 :
            response = True
        
        else:
            print('Invalid Input')
            response = False
    age = [age]
    return (age)

#function to take and check correct activity level input
def activityfunc ():
    response = False
    while response == False:
        activity = int(input('Activity level in [1,5]:'))
        if activity > 0 and activity < 6 :
            response = True
        
        else:
            print('Invalid Input')
            response = False
    activity = [activity]
    return (activity)

#function to create the program menu choice and check correct input
def get_menu_choice ():
    print('Welcome to the Calorie program menu:')
    print('[i]nput client info')
    print('[s]elect client')
    print('[e]xit')
    good_menu_choice = False
#set up a test for wrong input in the choices
    while not good_menu_choice:
        choice = input('Enter menu choice [i,s,e]: ')
        if choice != 'i' and choice !='s' and choice!='e':
            print(choice,'is invalid - please try again')
        else:
            good_menu_choice = True
    return choice

#function to display food menu
def get_food_choice ():
    
    print('Foods(total calories, fat in grams)')
    print('French Fries, (570, 30)')
    print('Onion Rings, (350, 16)')
    print('Hamburger, (670, 39)')
    print('Cheeseburger, (760, 47)')
    print('Grilled Chicken Sandwich, (470, 10)')
    print('Egg Buiscuit, (300, 12)')
    print('Mozzarella Sticks, (849, 56)')
    print('Cheese Pizza, (300, 11)')
    print('Macaroni and Cheese, (300, 7)')
    print('Glazed Chicken and Veggies, (497, 7)')
    print('')
    good_menu_choice = False
#set up a test for wrong input in the choices
    while not good_menu_choice:
        print('(Press \'Enter key\' with an empty response to go to next meal.)')
        print('')
        choice = input('Enter food choice: ')
        if choice != 'French Fries' and choice !='Onion Rings'and choice!='Hamburger' and choice!='Cheeseburger'and choice!='Grilled Chicken Sandwich'and choice!='Egg Buiscuit'and choice!='Mozzarella Sticks'and choice!='Cheese Pizza'and choice!='Macaroni and Cheese'and choice!='Glazed Chicken and Veggies'and choice!='':
            print(choice,'is invalid - please try again')
        else:
            good_menu_choice = True
    return choice



#__BEGINNIG OF PROGRAM__________________________________________________________________________________________________________
#import the csv to read and write to a csv file
import csv
user_menu_choice = ''
#set up program to run as long as the user doesn't chose to [e]xit
while user_menu_choice != 'e':
#create of open file to hold the dictionary of the clients and their stats
    clientfile=open("listclients.csv",'r')
    reader = csv.reader(clientfile)
#set up empty vaariables to be used later in the program
    info = []
    clientlist = []
    key = ''
    value = []
    cli_dict = {key:value}
#call on the menu functon
    user_menu_choice = get_menu_choice()
    
#____IF USER DECIDES TO ENTER/EDIT CLIENT____________________________________________________________________________________________ 
#set up statement if user enters i for input client info
    if user_menu_choice == 'i':
#go through the file and translate it into a dictionary
        for row in reader:
            for i in row:
                if i != '':
                    values = row[0:5]
                    cli_dict[row[5]] = values    
        clientfile.close()
#ask the user for the client first and last name
        name = input("Enter first name")
        name += input("Enter last name")
        
#call on the functions to gather stats from user        
        gender_val = genderfunc()
        info += gender_val
        weight_val = weightfunc()
        info += weight_val
        height_val = heightfunc()
        info += height_val
        age_val = agefunc()
        info += age_val
        activity_val = activityfunc()
        info += activity_val
        cli_dict[name] = info
        
#open and write dictionary back to the csv file
        clientfile = open("listclients.csv",'w')
        writer = csv.writer(clientfile)
        for key,value in cli_dict.items():
            clientlist = value + [key]
            
            if clientlist == ['']:
                clientlist.pop()
            writer.writerow(clientlist)
        clientfile.close()
        
#___IF USER CHOOSES TO SELECT A CLIENT_____________________________________________________________________________________________________        
#set up statement for if user input is s for select client
    elif user_menu_choice == 's':
#translate the file back into a dictionary
        realname = False
        for row in reader:
                for i in row:
                    if i != '':
                        values = row[0:5]
                        cli_dict[row[5]] = values
#ask the user for the client name to search for and check if it exists as a key in the dict
        while realname == False:
            name = input("Enter first name")
            name += input("Enter last name")        
            if name in cli_dict:
                realname = True
            else:
                print('You entered name does not exist in the file yet.')
                print('Please enter an existing name.')
                realname =False
#if the name exists, convert the dict values down into each seperate stat
        else:
            dict_value = cli_dict[name]
            
            gender = dict_value[0]
            integers = dict_value[1:5]
            integers = [int(i) for i in integers]
            weight = integers[0]
            height=integers[1]
            age = integers[2]
            activity = integers[3]
            
#___________CALCULATE NEED BASED ON STATS___________________________________________________________________________________________
#calculate the BMR depending on the gender stat
            if gender == 'female':
                bmr = 66+ (6.23*weight) + (4.7 * height)-(4.7 * age)
                
            
            elif gender == 'male':
                bmr = 66+ (6.23 * weight)+(12.7 * height)-(6.8 * age)
#calculate the calories needed based on the Harris Benedict formula    
            if activity == 1:
                calorie = bmr * 1.2
            elif activity == 2:
                calorie = bmr * 1.375
            elif activity == 3:
                calorie = bmr * 1.55
            elif activity == 4:
                calorie = bmr * 1.725
            elif activity == 5:
                calorie = bmr * 1.9
#calculate all of the different needs and the amount of calories needed to lose weight
            calorie = (round(calorie,3))
            fatcal1 = calorie * .20
            fatcal1 = (round(fatcal1,4))
            fatcal2 = calorie * .30
            fatcal2 = (round(fatcal2,4))
            fatgram1 = fatcal1 / 9
            fatgram1 =(round(fatgram1,2))
            fatgram2 = fatcal2 / 9
            fatgram2 =(round(fatgram2,2))
            reducecal = calorie * .10
            weightloss = calorie - reducecal
            weightloss = (round(weightloss,3))
            fatloss1 = weightloss *.20
            fatloss1 = (round(fatloss1,3))
            fatloss2 = weightloss * .30
            fatloss2 = (round(fatloss2,3))
            gramloss1 = fatloss1 / 9
            gramloss1 = (round(gramloss1,3))
            gramloss2 = fatloss2 / 9
            gramloss2 = (round(gramloss2,3))
#present the user with all of their calorie stats
            print('BMR is %.3f'% bmr)
            print ('Daily calorie need is ',calorie)
            print('Daily fat calorie need is from 20%(',fatcal1,') to 30%(',fatcal2,') of the daily calorie need')
            print('In fat grams from',fatgram1,'to',fatgram2)
            
            print('')
            print('    To lose weight, reduce calories by 10% below daily', weightloss)
            print('Keep daily fat calories from',fatloss1,'to',fatloss2)
            print('In fat grams from',gramloss1,'to',gramloss2,'grams daily')
            print('')

#___________SHOW FOOD MENU AND GET RESPONSES_______________________________________________________________________________            
            print('')
            print('    !FOOD MENU!')
            mealcount = 1
            foodcal=0
            foodfat=0
#set up the food menu input reactions 
            while mealcount <4:
                ask = True
                while ask == True:
                    if mealcount == 1:
                        print('     Breakfast:')
                    elif mealcount == 2:
                        print('     Lunch:')
                    elif mealcount == 3:
                        print('     Dinner:')
                    food_choice = get_food_choice ()
                    if food_choice == 'French Fries':
                        foodcal += 570
                        foodfat += 30
                    elif food_choice == 'Onion Rings':
                        foodcal+= 350
                        foodfat+=16
                    elif food_choice == 'Hamburger':
                        foodcal+= 670
                        foodfat+=39
                    elif food_choice == 'Cheeseburger':
                        foodcal+= 760
                        foodfat+=47
                    elif food_choice == 'Grilled Chicken Sandwich':
                        foodcal+= 420
                        foodfat+=10
                    elif food_choice == 'Egg Buiscuit':
                        foodcal+= 300
                        foodfat+=12
                    elif food_choice == 'Mozzarella Sticks':
                        foodcal+= 849
                        foodfat+=56
                    elif food_choice == 'Cheese Pizza':
                        foodcal+= 300
                        foodfat+=11
                    elif food_choice == 'Macaroni and Cheese':
                        foodcal+= 300
                        foodfat+=7
                    elif food_choice == 'Glazed Chicken and Veggies':
                        foodcal+= 497
                        foodfat+= 7
                    elif food_choice == '':
                        ask = False
                mealcount +=1
#calculate and display the amount of calories gained with the food choices and the amount
#recomended
            foodfat = foodfat*9
            foodcal = foodcal+foodfat
            print('')
            print(name,'should have',calorie,'calories per day.')
            print('To lose weight ',name,' should have',weightloss,'calories per day.')
            print('This meal plan gives',foodcal,'calories per day.')
            print('')
#close the file 
    clientfile.close()
#set up for if user menu choice is e for exit
else:
    print('Goodbye')

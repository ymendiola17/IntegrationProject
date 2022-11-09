
#Name:Yanisley Mendiola
#Description: This project will consist of a BTS trivia. BTS is a southkorean boyband that I really like.

total_score = 0
#This variable will keep track of the points earned throughout the trivia.
name = input("What is your name? ")
print("Hello,", name+"!", "I'm Yanisley Mendiola.", end='\n') #The end string will make a new line.
print("This is my first programming project.", end='\n\n') #I added double \n to my end string operator to skip two lines to separate the introduction and the questions.
#I included this + sign to this line because I wanted to input a variable and text ext to it. A comma would separate it so I used the + to concate it.

print("Before we start, let's name all BTS members. ") #sprint2:I added a for loop to the beginning of the sruvey that will ask the user for the names of the members so I can avoid asking the same question 7 times.
for x in range(1,8):
    input("Type the name of a BTS member: ")
print("Nice! \n")

print("Now, let's get started!")
print("I will ask you some questions, choose the one you think is correct.\n")

print("In what year did BTS debut?")
print("1.2010 \n2.2013 \n3.2014 \n4.2011")
debut_year = input("Enter the number corresponding to your choice: ")

if debut_year == "2":
    print("Correct!!! \n") #Kat helped me to understand if/else statements
    total_score += 1 #this plus sign will add points to the variable total_score if they get the right answer.
                    #Sprint2: I updated the variable += to make it more efficient
else:
    print("Wrong! \nThe correct answer is 2.2013. \n")
#If they their input is the same as the the if statement, the program will say "Correct!!!. If not, it will say "Wrong".
    
print("Next question:")
print("Who is BTS's leader?")
print("1.Kim Namjoon \n2.Kim Taehyung \n3.Kim Seokjin \n4.Park Jimin")
leader = input("Enter the number corresponding to your choice: ")
if leader == "1":
    print("Correct!!! \n")
    total_score += 1
else:
    print("Wrong! \nThe correct answer is 1.Kim Namjoon. \n") #sprint2 I updated all the 'wrong' answers and included the correct answer.

print("Next question: ")
total_albums = int(input("How many albums has the band released throughout their whole career? Enter a number: "))
while not total_albums == 19: #sprint2: I added a while loop that will ask the same question until answered right
    print("Not quite. You should visit their website (ibighit.com) to find the right answer! \n")
    total_albums = int(input("Let's try again! \nEnter a different number(The correct answer is in between numbers 15-20): "))
print("\nI have to admit that was a tricky question. This answer will not affect your score! \n")


print("Next question: ")
print("BTS consists of __ members. ")
members = input("Enter a number: ")

if (members == "7") or (members == "seven") or (members == "Seven"): #I have given out several options for the answer to prevent bugs.
    print("Correct!!! \n")
    total_score = total_score + 1
else:
    print("wrong! \nThe correct answer is 7 members. \n")

print("Next question: ")
print("If 300 Army fans want to hold a stream party and the goal is to increase 10,000 views of MV, how many times does each fan have to stream the MV?")
views = input("Round your answer: ")
views = int(views)
views_answer = 10000//300 #This will calculate the number of views each fan needs in order to achieve the goal dividing 10000 views by 300 fans.

if views_answer == views:
    print("Correct!!! \n")
    total_score = total_score + 1
else:
    print("Wrong! \nThe correct answer is", views_answer, "views. \n")

print("Next question: ")
print("if you had 47 roses and wanted to give each member the same amount of roses, how many roses each member would get and how many would you have left?", end="\n")
roses = input("Enter number of roses each member would get: ")
roses = int(roses)
roses_left = input("Enter number of roses you'd have left: ")
roses_left = int(roses_left)

if (roses == 47//7 and roses_left == 47%7): #This will calculate the amount of flowers each member will get. The % will calculate the roses that will not be given out.
    print("\nBoth of you answers are correct. \n","YAY","\n",sep='<3') #This question consists of two answers. If they get both right, it will print "YAY" (next line) Both of your answers are correct. 
    total_score = total_score + 2         #Two points will be added to the total_score variable
elif (roses == 47//7 or roses_left == 47%7): #If they only get one question right, only one point will be added to the total_score variable. 
    print("Oh no! \nOne of you answers is wrong. \n")
    total_score = total_score + 1
else:
    print("Wrong! \nNone of your answers is correct \nThe correct answers are 6 and 5. \n")
#I added a sep string operator to separate the "YAY" text string using <3(hearts).

print("Next question:")
print("Suppose each member receives $5.00 for every ticket sold a concert. \nIf the stadium's capacity is 35,000 persons, \nhow much money will they earn in total, if all the tickets are sold?")
concert_tickets = input("Enter amount of money earned: (do not use commas or spaces) \n$")
concert_tickets = int(concert_tickets)
if concert_tickets == 7*5*35000: #I used multiplication to find the amount of money all members(7) received. 
    print("Correct! \n")
    total_score = total_score + 1
else:
    print("Wrong! \nThe correct answer is $1,225,000. \n")
    

print("Next question:")
print("Suppose you want to save up money to buy a concert ticket for a concert that will be held in December \nYou decide the first week you will save $2.00, and double it every week for 10 weeks.")
print("How much money will you have saved up at by the end of the 10 weeks?")
savings = int(input("Enter the amount of money you saved up: (do not use commas, or spaces) \n$"))
if savings == 2**10:
      print("Correct!!!")
      total_score = total_score + 1     
else:
    print("Wrong!\nThe correct answer is $1,024.\n") #sprint2: I added a \n to skip a line to separte the end of a question and the new question

print("Last question:")
print("You and your three friends decided to order the latest album together to avoid paying too much shipping costs. \nEach album costs $37.00 and the total cost is $174.80.")
print("What is the total shipping cost?")
shipping_cost = input("Enter your answer: (do not use commas or spaces) $")
shipping_cost = float(shipping_cost)
print("How much would each person pay in total?")
album_and_shipping_cost = input("Enter your answer: (do not use commas or spaces) $")
album_and_shipping_cost = float(album_and_shipping_cost)

if (shipping_cost <= 174.80-37*4) and (album_and_shipping_cost == 174.8/4):
    print("YAY!!! \nBoth of your answers are correct. \n")
    total_score = total_score + 2
elif (shipping_cost == 174.80-37*4) or (album_and_shipping_cost == 174.8/4):
    print("Oh no! \nOne of your answers is wrong. \n")
    total_score = total_score + 1
else:
    print("Wrong! \n The correct answers are $26.80 and $43.70 \n")


print("This is the end of the trivia.")

trivia_question = input("Did you enjoy this trivia? ")
if trivia_question != " ":
    print("Thanks for your feedback! \n")

print("Your total score is ", total_score)

if (8 < total_score <= 10): #sprint2 I changed the scoring to include <>. If user reveives a score within the ranges they will get different outputs
    print("Congrats!!!"*100)
    print("You know a lot about BTS ")
elif 6 <= total_score <= 8:
    print("Congrats!!!"*10)
else:
    print("Don't give up! You will do better next time!!! ")

print("\nThank you for answering this trivia.")

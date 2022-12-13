"""My integration project"""
__author__ = "Yanisley Mendiola"
# Description: This project will consist of a BTS trivia and k-pop trivia .
# BTS is a South-korean boy-band that I really like.

# Add parameters
# use the try function so that the user won't exit the game and avoid
# any traceback errors


def bts_trivia():
    """Once the user chooses from the main() function this function will be
    called. This function consists of trivia questions. """
    total_score = 0
    # This variable will keep track of the points earned throughout the trivia.

    print("Before we start, I will introduce the boy-band. ")

    def my_function(bts_name):
        """The purpose of this function is to print the names of the
        boy band"""
        print("~" + bts_name, "<3")

    my_function('Kim Namjoon')
    my_function("Kim Seokjin")
    my_function("Min Yoongi")
    my_function("Jung Hoseok")
    my_function("Park Jimin")
    my_function("Kim Taehyung")
    my_function("Jeon Jungkook")

    print("Now, let's get started!")
    print("I will ask you some questions.")
    print("choose the one you think is correct.\n")

    print("In what year did BTS debut?")
    print("1.2010 \n2.2013 \n3.2014 \n4.2011")
    debut_year = input("Enter the number corresponding to your choice: ")
    if debut_year == "2":
        print("Correct!!! \n")
        # Kat helped me to understand if/else statements
        total_score += 1
        # this plus sign will add points to the variable total_score if
        # they get the right answer.
        # Sprint2: I updated the variable += to make it more efficient
    else:
        print("Wrong! \nThe correct answer is 2.2013. \n")
        # If their input is the same as the if statement,
        # the program will say "Correct!!!. If not, it will say "Wrong".

    print("Next question:")

    print("Who is BTS's leader?")
    print("1.Kim Namjoon \n2.Kim Taehyung \n3.Kim Seokjin \n4.Park Jimin")
    leader = input("Enter the number corresponding to your choice: ")
    if leader == "1":
        print("Correct!!! \n")
        total_score += 1
    else:
        print("Wrong! \nThe correct answer is 1.Kim Namjoon. \n")
        # sprint2 I updated all the 'wrong' answers and included
        # the correct answer.

    print("Next question: ")

    total_albums = int(input(
        "How many albums has the band released throughout their whole career? "
        "Enter a number: "))
    while not total_albums == 19:
        # sprint2: I added a while loop that will ask the same
        # question until answered right
        print(
            "\nNot quite. You should visit their website (ibighit.com) to find"
            " the right answer! \n")
        print("Let's try again! \n")
        total_albums = int(input(
            "Enter a different number (Hint: The correct answer is in between "
            "numbers 15-20): "))
    print(
        "\nI have to admit that was a tricky question. This answer will not "
        "affect your score! \n")

    print("Next question: ")

    print("BTS consists of __ members. ")
    members = input("Enter a number: ")
    if (members == "7") or (members == "seven") or (members == "Seven"):
        # I have given out several options for the answer to prevent bugs.
        print("Correct!!! \n")
        total_score += 1
    else:
        print("wrong! \nThe correct answer is 7 members. \n")

    print("Next question: ")

    print(
        "If 300 Army fans want to hold a stream party and the goal is to "
        "increase 10,000 views of MV, \nhow many times does each fan "
        "have to stream the MV?")
    views = int(input("Round your answer: "))
    views_answer = 10000 // 300
    # This will calculate the number of views each fan needs in order to
    # achieve the goal dividing 10000 views by 300 fans.
    if views_answer == views:
        print("Correct!!! \n")
        total_score += 1
    else:
        print("Wrong! \nThe correct answer is", views_answer, "views. \n")

    print("Next question: ")

    print(
        "In a scenario where you had 47 roses and wanted to give each member"
        " the same amount of roses, \nhow many roses each member would get and"
        " \nhow many would you have left?", end=" ")
    roses = int(input("Enter number of roses each member would get: "))
    roses_left = int(input("Enter number of roses you'd have left: "))

    if roses == 47 // 7 and roses_left == 47 % 7:
        # This will calculate the amount of flowers each member will get.
        # The % will calculate the roses that will not be given out.
        print("\nBoth of you answers are correct. \n", "YAY", "\n", sep='<3')
        # This question consists of two answers.
        # If they get both right, it will print "YAY" (next line)
        # Both of your answers are correct.
        # I added a sep string operator to separate the "YAY" text string
        # using <3(hearts)
        total_score += 2
        # Two points will be added to the total_score variable
    elif roses == 47 // 7 or roses_left == 47 % 7:
        # If they only get one question right, only one point will be added
        # to the total_score variable.
        print("Oh no! \nOne of you answers is wrong. \n")
        total_score += 1
    else:
        print(
            "Wrong! \nNone of your answers is correct \nThe correct answers "
            "are 6 and 5. \n")\

    print("Next question:")

    print(
        "Suppose each member receives $5.00 for every ticket sold a concert. ")
    print(
        "If the stadium's capacity is 35,000 persons, \nhow much money will "
        "they earn in total if all tickets are sold?")
    concert_tickets = int(input(
        "Enter amount of money earned: (do not use commas or spaces) \n$"))
    if concert_tickets == 7 * 5 * 35000:
        # I used multiplication to find the amount of $ all members received
        print("Correct! \n")
        total_score += 1
    else:
        print("Wrong! \nThe correct answer is $1,225,000. \n")

    print("Next question:")
    print(
        "Suppose you want to save up money to buy a concert ticket for a "
        "concert that will be held in December \nYou decide the first week you"
        " will save $2.00, and double it every week for 10 weeks.")
    print(
        "How much money will you have saved up at by the end of the 10 weeks?")
    savings = int(input(
        "Enter the amount of money you saved up: (do not use commas, "
        "or spaces) \n$ "))
    if savings == 2 ** 10:
        print("Correct!!!")
        total_score += 1
    else:
        print("Wrong!\nThe correct answer is $ 1,024.\n")
        # sprint2: I added a \n to skip a line to separate the end of a
        # question and the new question

    print("Last question:")

    print(
        "You and your three friends(4 people) decided to order the latest"
        " album together to avoid paying too much shipping costs. "
        "\nEach album costs $37.00 and the total cost is $174.80.")
    print("What is the total shipping cost?")
    shipping_cost = float(
        input("Enter your answer: (do not use commas or spaces) $"))
    print("How much would each person pay in total?")
    album_and_shipping_cost = float(
        input("Enter your answer: (do not use commas or spaces) $"))

    if (shipping_cost <= 174.80 - 37 * 4) and (
            album_and_shipping_cost == 174.8 / 4):
        print("YAY!!! \nBoth of your answers are correct. \n")
        total_score += 2
    elif (shipping_cost == 174.80 - 37 * 4) or (
            album_and_shipping_cost == 174.8 / 4):
        print("Oh no! \nOne of your answers is wrong. \n")
        total_score += 1
    else:
        print("Wrong! \n The correct answers are $26.80 and $43.70 \n")

    print("This is the end of the trivia.")

    print("Your total score is ", total_score, "out of 10.")

    if 8 < total_score <= 10:
        # sprint2 I changed the scoring to include <>. If user receives a score
        # within the ranges they will get different outputs
        print("Congrats!!!\n" * 20)
        print("You know a lot about BTS ")
    elif 6 <= total_score <= 8:
        print("Congrats!!!" * 10)
    else:
        print("Don't give up! You will do better next time!!! ")

    trivia_question = input("Did you enjoy this trivia? ")
    if trivia_question != " ":
        print("Thanks for your feedback! \n")


def kpop_trivia():
    """If called, this function will prompt a different trivia from the
    function above"""
    total_score = 0
    print("Let's begin this trivia")
    print("First question")

    print("Which member of BlackPink has not released a solo song as of 2022?")
    print("1. Rosé \n2. Jisoo \n3. Jennie \n4. Lisa")
    black_pink = int(input("Enter a number: "))
    if black_pink == 2:
        print("Correct!!!")
        total_score += 1
    else:
        print("Your answer is incorrect. The correct answer is '2.Jisoo'")

    print("Next question")

    print("BangChan and Felix from Stray Kids have a different ethnicity "
          "from the rest of the group. \nWhat is their ethnicity?")
    print("1. Chinese \n2. Thai \n3. Japanese \n4. Australian")
    stray_kids = int(input("Enter a number: "))
    if stray_kids == 4:
        print("Correct!!!")
        total_score += 1
    else:
        print("Your answer is incorrect. The correct answer is "
              "'4. Australian'")

    print("Next Question")

    print("Which TWO songs did Kim Taehyung sing for a TV-Show? ")
    print("1. Christmas Tree \n2. Snow flower \n3. Scenery \n4. Sweet Night")
    kth1 = int(input("Enter first number: "))
    kth2 = int(input("Enter second number: "))
    if kth1 == 1 and kth2 == 4:
        print("Correct!!!")
        total_score += 2
    elif kth1 == 4 and kth2 == 1:
        print("Correct!!!")
        total_score += 2
    elif kth1 == 4 or kth2 == 1:
        print("Oh no! One of your answers is wrong!"
              "\nThe correct answers are 1.Christmas Tree and 4. Sweet Night")
        total_score += 1
    elif kth1 == 1 or kth2 == 4:
        print("Oh no! One of your answers is wrong!"
              "\nThe correct answers are 1. Christmas Tree and 4. Sweet Night")
        total_score += 1
    else:
        print("Both of your answers were wrong. \nThe correct answers are"
              "1. Christmas Tree and 4. Sweet Night")
    # Final_sprint: I included several options since the user could type
    # the answers in different forms. By doing this I reduced the possibilities
    # of getting an error.

    print("Next question")

    print("How many languages does Jackson Wang speak? ")
    print("1. One \n2. Two \n3. Three \n4. Four")
    jackson_w = int(input("Enter a number: "))
    if jackson_w == 3:
        print("Correct!!!")
        total_score += 1
    else:
        print("Your answer is incorrect. The correct answer is  3. Three."
              "He speaks Chinese, Korean, and English! ")

    print("Next question")
    print("Which song did TXT debut with? ")
    print("1. Crown \n2. I know I love you \n3. Blue Hour \n4. Anti-Romantic")
    txt = int(input("Enter a number: "))
    if txt == 1:
        print("Correct!!!")
        total_score += 1
    else:
        print("Your answer is incorrect.The correct answer is 1.Crown")

    print("Next question")
    print("Which entertainment company is in the TOP 1 in South Korea? ")
    print("1. SM Entertainment \n2. JYP Entertainment \n3. Hybe "
          "\n4.JY Entertainment")
    top1 = int(input("Enter a number: "))
    if top1 == 3:
        print("Correct!!!")
        total_score += 1
    else:
        print("Your answer is incorrect.The correct answer is 3. Hybe")

    print("Next question")
    print("What is the name of the show created by HYBE Entertainment to "
          "recruit \ntheir new boy-band named 'Enhypen'")
    print("1. NTC \n2. Intro to I-land \n3. HYBE-ring \n4. Rising Stars ")
    new_group = int(input("Enter a number: "))
    if new_group == 2:
        print("Correct!!!")
        total_score += 1
    else:
        print("Your answer is incorrect. The correct answer is "
              "2. Intro to I-land")

    print("Next question")
    print("What is the name of the name of the podcast where BM, Ashley, and "
          "Peniel \ntalk about all the ups and downs of work, love, "
          "and adulthood?")
    print("1. Daebak Show \n2. DIVE Studios \n3. Get Real \n4. Adulting")
    podcast = int(input("Enter a number: "))
    if podcast == 3:
        print("Correct!!!")
        total_score += 1
    else:
        print("Your answer is incorrect. The correct answer is 3. Get Real ")

    print("Last question. \n")
    print("What is Jessi's show called ?")
    print("1. Jessi's Showterview \n2. Jessi's Tea Party \n3. Jessi Lies "
          "\n4. Jessi Interviews")
    jessi_show = int(input("Enter a number: "))
    if jessi_show == 1:
        print("Correct!!!")
        total_score += 1
    else:
        print("Your answer is incorrect. \nThe correct answer is 1. Jessi's"
              "Showterview. \n")

    print("This is the end of the trivia \n")
    print("Your total score is ", total_score, "out of 10.")

    if 8 < total_score <= 10:
        # I reused the code from the other trivia to avoid  re-writing it
        # again. I only had to make some adjustments for the code to work in
        # this function.
        print("Congrats!!!\n" * 20)
        print("You know a lot about K-pop")
    elif 6 <= total_score <= 8:
        print("Congrats!!!\n" * 10)
    else:
        print("Don't give up! You will do better next time!!! ")

    trivia_question = input("Did you enjoy this trivia? ")
    if trivia_question != " ":
        print("Thanks for your feedback! \n")


def main():
    """The main function will prompt the user an introduction to the
     program. It will also let the user decide which function to
      prompt next."""
    name = input("What is your name? ")
    print("Hello,", name + "!", "I'm Yanisley Mendiola.", end=' ')
    # The end string will make a new line.
    print("This is my first programming project.", end='\n\n')
    # I added double \n to my end string operator to skip two lines
    # to separate the introduction and the questions.
    # I included this + sign to this line because I wanted to input a variable
    # and text to it. A comma would separate it, so I used + to concatenate it.
    print("I created two different trivia quizzes for you.")
    print("The first trivia consists of questions about different "
          "K-pop groups. ")
    print("The second trivia consists of questions about BTS. \n")

    user = input("Please choose number one(1) or two(2) to begin: \n")

    if user == "one" or user == "One" or user == "1":
        kpop_trivia()
    elif user == "Two" or user == "two" or user == "2":
        bts_trivia()

    print("Thank you for participating in my first programming project!")


main()

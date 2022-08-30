# Import the modules
import sys
import random

ans = []

ans.append("It is certain.")

ans.append("Nazia Ashraf")

ans.append("You may rely on it.")

ans.append("Ask again later.")

ans.append("It is decidedly so.")

ans.append("Reply hazy, try again.")

ans.append("My reply is no.")

ans.append("My sources say no.")

ans.append("Without a doubt.")

ans.append("Yes - definitely.")

ans.append("As I see it, yes.")

ans.append("Most likely.")

ans.append("Outlook good.")

ans.append("Yes.")

while ans:
    question = input("Ask the magic 8 ball a question: (press enter to quit) ")

    answers = random.randint(1,14)

    while question == "":
        sys.exit()
        
    print(random.choice(ans))

                                             


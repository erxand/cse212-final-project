stack_o_pancakes = []
counter = 0
full = False
while not full:
    print("Options:\n0. \"I\'m full\"\n1. Get pancake\n2. Eat pancake\n3. Count # of pancakes\n4. Stack details")
    response = int(input("What would you like to do? "))
    match response:
        case 0:
            full = True
        case 1:
            counter += 1
            stack_o_pancakes.append(f"pancake #{counter}")
            print("There you go, another pancake!")
        case 2:
            stack_o_pancakes.pop()
            print("Wow you ate that fast, was it good?")
        case 3:
            print(f"Hmm... it looks like I've given you {counter} pancakes and you have {len(stack_o_pancakes)} on your plate.")
            print("I'm really bad at math, how many does that mean you've eaten?")
        case 4:
            for i in range(len(stack_o_pancakes)):
                print(f"The pancake in the {i + 1} spot was the {stack_o_pancakes[i][-1]} pancake made.")
            print("Funny how that works out, huh?")
        case _:
            print("C'mon you know that's not an option. What do you want to do?")
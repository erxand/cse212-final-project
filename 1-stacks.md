# Stacks
Stacks are one of the most basic types of data structures. In this tutortial they will be the easiest to learn and implement. If you understand how to look for a certain card in a deck of cards, then you can understand how to look for data in a stack.

## Structure
To easily explain how a stack works we can use a deck of cards. Picture the cards stacked like normal on a table. In the real world you can pick up the stack of cards and take the bottom card, or you could pick up a portion of the deck and take a middle card. In our example, to go along with the data structure, we have really really fat fingers. We can't pick all the cards up off the table, we can't even grab half the deck. All we can do is slide the top card off and take that one. If we were to look at each card in the deck we'd have to take them off one at a time. We also can't put a card back in the middle, we're too uncoordinated. If we want to add a new card to the deck we have to just put it on top.

This is how our data structure works. If we want to look at the "bottom" datum we need to iterate through each datum in the data. The "bottom" datum is also the first added to the stack. If we want to add something to the middle of the stack we would have to pull data off one at a time until we get to the spot, put in the new datum, and then put everything else back on top in order.

## Basic Functions
| Stack Operation | Description | Python Code | O(?) |
| --- | --- | --- | --- |
| push(_x_) | Puts _x_ on the "top" of the stack | stack.append(x)| O(1) |
| pop() | Removes and returns the item from the "top" of the stack. | value = stack.pop() | O(1) |
| size() | Return the size of the stack. | length = len(stack) | O(1) |
| empty() | Returns ```true``` if the length of the stack is zero. | if len(stack) == 0: | O(1) |


## Example: Stack of Pancakes
In this example we can see Python's dynamic array being used as a stack, as Python doesn't have a perfect stack structure. In this code example we use three of the four basic functions listed above, can you figure out which one isn't used?
```python
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
```
If you want to run this exact program the file is (here)[stacks_example.py], or just copy and paste this into your IDE.

## Problem: Coin Holder
Please write a program to solve the following problem:
We have a little coin holder, you put your coin in the top and it rolls down into the appropriate spot. The smaller spots come first, that way the bigger ones keep going until they hit their spot. This way every coin falls in the correct spot. However, sometimes the coin doesn't go where it's supposed to, the quarter spot is the worst because any of the other coins can fit in that spot. We want to take out all non-quarters from the quarters spot. Unfortunately we can't just empty the whole thing at once, it's built in a way that we have to take them back out one at a time.

The quarters spot will be represented as a list of tuples. Each tuple represents a coin, quarters being ("Q", x), dimes ("D", x), nickels ("N", x) and pennies ("P", x), x representing the year the coin was minted. By including the year of the coin we can be assured that the coins are returned back in the proper order, characteristic of a stack. Your task is to iterate through the list and remove everything that isn't a quarter and then put it back in in the order you took it out.

Here are some premade lists you can use to check your program:
```python
list_1 = [("Q", 2002), ("Q", 1997), ("P", 2015), ("Q", 2011), ("D", 1971), ("D", 2020), ("Q", 2013), ("Q", 1999), ("P", 2001)]
list_2 = [("Q", 2002), ("Q", 1997), ("Q", 2011), ("Q", 2013), ("Q", 1999)]
list_3 = [("P", 2012), ("N", 1986), ("P", 2010), ("N", 2011), ("D", 1919), ("D", 2022), ("P", 2009), ("N", 1980), ("P", 2011)]
```

Here is what the results should be for each list:
```python
list_1 = [("Q", 2002), ("Q", 1997), ("Q", 2011), ("Q", 2013), ("Q", 1999)]
list_2 = [("Q", 2002), ("Q", 1997), ("Q", 2011), ("Q", 2013), ("Q", 1999)]
list_3 = []
````

Possible solution [here](stacks_problem_solution.py), only view this once you have completed the problem on your own or feel you cannot progress any further.

## Links
[Welcome Page](0-welcome.md)

[Outline](outline.md)

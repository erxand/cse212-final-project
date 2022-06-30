# Stacks
Stacks are one of the most basic types of data structures. In this tutortial they will be the easiest to learn and implement. If you understand how to look for a certain card in a deck of cards, then you can look for data in a stack.

## Structure
To easily explain how a stack works we can use a deck of cards. Picture the cards stacked like normal on a table. In the real world you can pick up the stack of cards and take the bottom card, or you could pick up a portion of the deck and take a middle card. In our example, to go along with the data structure, we have really really fat fingers. We can't pick all the cards up off the table, we can't even grab half the deck. All we can do is slide the top card off and take that one. If we were to look at each card in the deck we'd have to take them off one at a time. We also can't put a card back in the middle, we're too uncoordinated. If we want to add a new card to the deck we have to just put it on top.

This is how our data structure works. If we want to look at the "bottom" datum we need to iterate through each datum in the data. The "bottom" datum is also the first added to the stack. If we want to add something to the middle of the stack we would have to pull data off one at a time until we get to the spot, put in the new datum, and then put everything else back on top in order.

## Basic Functions
| Stack Operation | Description | Python Code | O(?) |
| --- | --- | --- | --- |
| push(_x_) | Puts _x_ on the "top" of the stack | my_stack.append(x)| O(1) |
| pop() | Removes and returns the item from the "top" of the stack. | value = my_stack.pop() | O(1) |
| size() | Return the size of the stack. | length = len(my_stack) | O(1) |
| empty() | Returns ```true``` if the length of the stack is zero. | if len(my_stack) == 0: | O(1) |


## Example
```python
def tell_him():
    print("dingus put some actual code here")
```

## Problem to Solve
[problem file](https://crouton.net/)

## Links
[Welcome Page](0-welcome.md)

[Outline](outline.md)

## Plan
Required content:
* example python code
* tables
* diagrams
* example of a solved problem
* unfinished problem for the student

Tutorial Structure:
* Introduction
* Structure
* Basic Functions
* Example
* Problem to Solve

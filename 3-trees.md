# Trees
A tree is used as a way to store data. They are very organized and because of that they are very fast to search. Trees will probably be the hardest data structure in this tutorial to understand, but if you already understood the linked list you will have an easier time learning trees.

## Structure
A binary tree is essentially a two-dimensional upgraded linked list, instead of the head pointing to one value it points to two. Each value thereafter also points to two values, unless there isn't a value available for that spot. A binary tree is, by definition, ordered. You can't make one properly without ordering it. The first item, the "head", is supposed to be roughly the middle number or item in this ordered list. The item to the "left" of the head has a lower value than the head, and the item to the "right" of the head has a higher value of the head. Each of these items has their following two items organized the same way.

Don't quite understand it yet? Check out this picutre:
![1200px-Binary_search_tree svg](https://user-images.githubusercontent.com/97632407/178615031-1070645a-68d6-46e3-9543-7463422526be.png)

Still don't understand it? Let me give an example of searching through this tree. Say we're looking for the value 18. We check the head, it has a value of 10. Since 10 is less than what we want, now we check the item to the right. This item is 15. Since 18 is bigger than 15 we check to the right again. This item is 20. Since 18 is smaller than 20, we check to the left. This item is 18, we found it!

## Basic Functions
table

## Example: idk man
example here

## Problem: idk man
problem here

## Links
[Welcome Page](0-welcome.md)

[Outline](outline.md)

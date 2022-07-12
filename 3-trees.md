# Trees
A tree is used as a way to store data. They are very organized and because of that they are very fast to search. Trees will probably be the hardest data structure in this tutorial to understand, but if you already understood the linked list you will have an easier time learning trees.

## Structure
A binary tree is essentially a two-dimensional upgraded linked list, instead of the head pointing to one value it points to two. Each value thereafter also points to two values, unless there isn't a value available for that spot. A binary tree is, by definition, ordered. You can't make one properly without ordering it. The first item, the "head", is supposed to be roughly the middle number or item in this ordered list. The item to the "left" of the head has a lower value than the head, and the item to the "right" of the head has a higher value of the head. Each of these items has their following two items organized the same way.

Don't quite understand it yet? Check out this picture:
![1200px-Binary_search_tree svg](https://user-images.githubusercontent.com/97632407/178615031-1070645a-68d6-46e3-9543-7463422526be.png)

Let me give an example of searching through this tree. Say we're looking for the value 7. We start at the head, which is 8, and we ask whether 7 is less or more than the head. 7 is less so we go to the left. This takes us to the next node, which is 3. 7 is bigger than 3 so we go right. Now we're at 6, 7 is bigger so we go right again. This takes us to 7, that's what we were looking for! This took us 4 steps, we went 8, 3, 6, 7. If we were to search through a normal sorted list it would've taken 5 steps, going 1, 3, 4, 6, 7. The tree took 4 steps and the normal list took 5, you could argue that that's a negligible difference. However, this is the longest it will ever take us to search this tree. If we're looking for 13 it would also take us 4 steps with the tree, but we'd have to iterate through all 9 elements before we'd find it in a normal sorted list.

Every time we double the size of the tree it only increases the search time by one step, but every time we double the size of a normal list it could double the search steps as well. See why binary trees are useful? They're pretty cool!

## Basic Functions
| Stack Operation | Description | Python Code | O(?) |
| --- | --- | --- | --- |
| insert(x) | Insert _x_ into the tree. | python | O(log n) |
| remove(x) | Remove _x_ from the tree. | python | O(log n) |
| contains(x) | Determine if _x_ is in the tree. | python | O(log n) |
| traverse_forward | Iterate through all objects from smallest to largest. | python | O(n) |
| traverse_reverse | Iterate through all objects from largest to smallest. | python | O(n) |
| height(node) | Determine the height of a tree from the node. If the height of the tree is needed, provide the root node. | python | O(n) |
| size() | Return the size of the tree. | python | O(1) |
| empty() | Returns true if the root node is empty. This can also be done by checking the size for 0. | python | O(1) |

## Example: idk man
example here

## Problem: idk man
problem here

## Links
[Welcome Page](0-welcome.md)

[Outline](outline.md)

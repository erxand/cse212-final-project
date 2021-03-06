# Trees
A tree is used as a way to store data. They are very organized and because of that they are very fast to search. Trees will probably be the hardest data structure in this tutorial to understand, but if you already understood the linked list you will have an easier time learning trees.

## Structure
A binary tree is essentially a two-dimensional upgraded linked list, instead of the head pointing to one value it points to two. Each value thereafter also points to two values, unless there isn't a value available for that spot. A binary tree is, by definition, ordered. You can't make one properly without ordering it. The first item, the "head", is supposed to be roughly the middle number or item in this ordered list. The item to the "left" of the head has a lower value than the head, and the item to the "right" of the head has a higher value of the head. Each of these items has their following two items organized the same way.

Don't quite understand it yet? Check out this picture:
![1200px-Binary_search_tree svg](https://user-images.githubusercontent.com/97632407/178615031-1070645a-68d6-46e3-9543-7463422526be.png)

Let me give an example of searching through this tree. Say we're looking for the value 7. We start at the head, which is 8, and we ask whether 7 is less or more than the head. 7 is less so we go to the left. This takes us to the next node, which is 3. 7 is bigger than 3 so we go right. Now we're at 6, 7 is bigger so we go right again. This takes us to 7, that's what we were looking for! This took us 4 steps, we went 8, 3, 6, 7. If we were to search through a normal sorted list it would've taken 5 steps, going 1, 3, 4, 6, 7. The tree took 4 steps and the normal list took 5, you could argue that that's a negligible difference. However, this is the longest it will ever take us to search this tree. If we're looking for 13 it would also take us 4 steps with the tree, but we'd have to iterate through all 9 elements before we'd find it in a normal sorted list.

Every time we double the size of the tree it only increases the search time by one step, but every time we double the size of a normal list it could double the search steps as well. See why binary trees are useful? They're pretty cool!

## Basic Functions
| Stack Operation | Description | O(?) |
| --- | --- | --- |
| insert(x) | Insert _x_ into the tree. | O(log n) |
| remove(x) | Remove _x_ from the tree. | O(log n) |
| contains(x) | Determine if _x_ is in the tree. | O(log n) |
| traverse_forward | Iterate through all objects from smallest to largest. | O(n) |
| traverse_reverse | Iterate through all objects from largest to smallest. | O(n) |
| height(node) | Determine the height of a tree from the node. If the height of the tree is needed, provide the root node. | O(n) |
| size() | Return the size of the tree. | O(1) |
| empty() | Returns true if the root node is empty. This can also be done by checking the size for 0. | O(1) |

## Example: Searhing an Organized Maze
Let's imagine for a bit here. I haven't ever heard of a maze like this, but say we come to a maze where instead of there being one entrance and one exit, there is one entrance and lots of dead ends, but no exit. In each intersection and dead end there is a numbered item, with signs in the intersections saying what the next item is. If we were to walk through this maze in search of an item the signs would be very useful in helping us locate the item. Say we have items 1-100, and we're looking for item #42. The first intersection we come across is item #50, there is a sign pointing to the left to item #25 and a sign pointing to the right to item #75. We walk to the left, because we know that item #42 would be in the direction of item #25 instead of item #75. We would continue with that pattern and logic until we found item #42.

Here's some example code for searching the maze. This is done by creating a native \_\_contains\_\_ function. I reccommend you look at the whole code file, as there is a lot more that goes into getting a binary search tree to this point. It will also help a lot to check out this file, because you'll use it so you don't have to start from scratch with your practice problem.
```python
def __contains__(self, data):
    return self._contains(data, self.root)

def _contains(self, data, node):
    if node != None:
        if data == node.data:
            return True
        if data < node.data:
            return self._contains(data, node.left)
        if data > node.data:
            return self._contains(data, node.right)
```

The full program file is [here](trees_example.py).

## Problem: Messing with People in an Organized Maze
Say your maze here is a tourist attraction, after all it is a pretty unique way to organize your stuff. You like to mess with people. Make it so you can block off part of the maze so people can't find those items, and then open it back up just to confuse them. Using [this](trees_example.py) file (it's the same one used for the example above), add functionality to remove a branch starting at a certain value from the maze, and functionality to add a branch back in. Use the \_\_contains\_\_ function from the example to make sure you removed the item, then use that function again once you've added the item back to make sure it was successful. Hint: you might want to give the Maze class methods for adding and removing nodes instead of just data so you can keep everything after it.

Once you feel you have either completed this problem or gotten too stuck, check [the solution](trees_problem_solution.py) and compare it with your own.

## Links
[Welcome Page](0-welcome.md)

[Outline](outline.md)

## Beam Me Up!
![me in a tree](https://user-images.githubusercontent.com/97632407/179285718-3fbd0c19-ef6b-41cd-ac45-c555362af961.jpg)

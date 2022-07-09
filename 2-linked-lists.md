# Linked Lists
If you already have an idea of how a list or array works then you shouldn't have a hard time understanding linked lists. A linked list is essentially a unique way to create a list, it has some drawbacks but definitely has some uses. Blockchain technology is a great example of a very advanced linked list.

## Structure
You might think that you don't know what a stanchion is, but you're wrong. You've seen them before, you've probably spent more time around them than you would've liked to. You know those wait-high crowd control pole things in airports and other places to help form lines? They have the fabric divider that stretches between each pole? Those are stanchions. Stanchions are actually a great example of linked lists. Each stanchion has a connector that takes you to the next one, there is one stanchion that is the first one, it doesn't have any other stanchions connecting to it, it just starts and leads to the second one. Each stanchion after the first or the "head" has a stanchion before it that points to it, and then it points to another stanchion. This continues to the last stanchion, which doesn't point to any more because it is the last, or the "tail".

In a linked list we see the same format. A linked list is composed of nodes. Each node has two characteristics: its value and the address of the next node. To follow the example, a stanchion has itself: the pole, and the directions to the next stanchion: the cord between them. The first node is known as the head, and the last node is known as the tail. The tail doesn't contain directions to another node, it has a null value in that place.

If we want to add a new value to the middle of a linked list we, say _x_ set _x_'s directions to the value following the spot you want _x_ in and you change the directions of its predecessor to point to _x_. If you want to delete _x_ out of the linked list you simply change the directions of its predecessor to point to the value that follows _x_.

## Basic Functions
| Stack Operation | Description | Python Code | O(?) |
| --- | --- | --- | --- |
| insert_head(x) | Adds _x_ before the head, it becomes the new head | linked_list.appendleft(x) | O(1) |
| insert_tail(x) | Adds _x_ after the tail, it becomes the new tail | linked_list.append(x) | O(1) |
| insert(i, x) | Adds _x_ after node _i_. | my_deque.insert(i, x) | O(n) |
| remove_head() | Removes the head (the first item) | x = linked_list.popleft() | O(1) |
| remove_tail() | Removes the tail (the last item) | x = linked_list.pop() | O(1) |
| remove(i) | Removes node _i_. | del linked_list[i] | O(n) |
| size() | Return the size of the linked list | length = len(linked_list) | O(1) |
| empty() | Returns true if the length of the linked list is zero. | if len(linked_list) == 0: | O(1) |

## Example: Stanchions
Here we have a series of stanchions. We want to walk alongside the stanchions wherever they lead to and read the names on each stanchion. We would also like to put a stanchion in the middle of it all, and take some out along the way.
```python
class Stanchion():
    def __init__(self, name, next=None):
        self.name = name
        self.next = next

    def add_last_stanchion(self, name):
        if self.next == None:
            self.next = Stanchion(name)
        else:
            self.next.add_last_stanchion(name)

    def read_following_names(self):
        print(self.name, end=" ")
        if self.next != None:
            self.next.read_following_names()
        else:
            print()

print()
stanchion_head = Stanchion("1")
stanchion_head.add_last_stanchion("2")
stanchion_head.add_last_stanchion("3")
stanchion_head.add_last_stanchion("4")
stanchion_head.add_last_stanchion("5")
stanchion_head.read_following_names()
stanchion_head.next.next.read_following_names()
print()
```
If you want to run this exact program the file is [here](linked_lists_example.py), or just copy and paste the above code into your IDE.

## Problem: Geocaching Activity
Please write a program to solve the following problem: You are a youth leader in your local ward. You made a geocaching activity, where the youth are given a set GPS coordinates on a piece of paper, that leads them to a container with another paper and set of coordinates. This continues through several sets of coordinates. Please write a program that creates a linked list that contains the following coordinates. Give it functionality to add nodes on the end, to insert nodes in the middle, and to remove nodes from the middle and end.

Create a coordinate object that has a set of coordinates in a tuple and a pointer to the next coordinate object. Both data points serve essentially the same purpose in this activity, the pointer is doing what the coordinates would do in real life, but we're putting the coordinates in to keep track of order.

Start the linked list with the coordinates at _x_.
Add the coordinates _a_, _b_, and _c_ on the end.
Add the coordinate _d_ after _a_, in the third position.
Add the coordinates _e_ and _f_ to the end.
Remove the coordinates _c_ and _f_ from the linked list.
You should end up with a list that goes _x_, _a_, _b_, _d_, _e_.

Possible solution [here](linked_lists_problem_solution.py), only view this once you have completed the problem on your own or feel you cannot progress any further.

## Links
[Welcome Page](0-welcome.md)

[Outline](outline.md)

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
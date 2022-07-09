class Node():
    def __init__(self, coordinates, next=None):
        self.coords = coordinates
        self.next= next
    
    def add_end_node(self, coordinates):
        if self.next == None:
            self.next = Node(coordinates)
        else:
            self.next.add_end_node(coordinates)
    
    def add_placed_node(self, place, coordinates):
        if place == 0:
            new_node = Node(coordinates, self.next)
            self.next = new_node
        else:
            self.next.add_placed_node(place - 1, coordinates)
    
    def remove_node(self, coordinates):
        if self.next.coords == coordinates:
            self.next = self.next.next
        else:
            self.next.remove_node(coordinates)
    
    def print_nodes(self):
        print(self.coords)
        if self.next != None:
            self.next.print_nodes()

head = Node((43.814630, -111.784310))
head.add_end_node((40.249101, -111.650649))
head.add_end_node((21.641232, -157.927324))
head.add_end_node((41.732061, -98.099521))
head.add_placed_node(2, (41.882511, -87.623312))
head.add_end_node((37.808942, -122.198965))
head.add_end_node((39.919561, -92.785264))
head.remove_node((41.732061, -98.099521))
head.remove_node((39.919561, -92.785264))
head.print_nodes()
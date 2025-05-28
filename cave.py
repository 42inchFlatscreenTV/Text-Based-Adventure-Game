class Cave:
    def __init__(self, cave_name):
        self.name = cave_name
        self.description = None
        self.linked_caves = {}

    # getters and setters for description
    def get_description(self):
        return self.description

    def set_description(self, cave_description):
        self.description = cave_description

    # getters and setters for name
    def get_name(self):
        return self.name

    def set_name(self, new_name):
        self.name = new_name

    def set_character(self, new_character):
        self.character = new_character
    
    def get_character(self):
        return self.character

    # describe method to print description
    def describe(self):
        print(self.description)

    # method to link caves
    def link_cave(self, cave_to_link, direction):
        self.linked_caves[direction] = cave_to_link

    def get_details(self):
        print(self.name)
        print("----------")
        print(self.description)
        for direction in self.linked_caves:
            cave = self.linked_caves[direction]
            print("The " + cave.get_name() + " is " + direction)

    def move(self, direction):
        if direction in self.linked_caves:
            return self.linked_caves[direction]
        else:
            print("You can't go that way")
            return self

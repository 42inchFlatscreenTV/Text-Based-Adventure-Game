class Cave:
    def __init__(self, cave_name):
        self.name = cave_name
        self.description = None
        self.linked_caves = {}
        self.character = None

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

    # getters and setters for character 
    def set_character(self, new_character):
        self.character = new_character
    
    def get_character(self):
        return self.character

    # getters and setters for weakness
    def set_weakness(self, new_weakness):
        self.weakness = new_weakness

    def get_weakness(self):
        return self.weakness
    
    # describe method to print description
    def describe(self):
        print(self.description)

    # method to set item in cave
    def set_item(self, item):
        self.item = item

    def get_item(self):
        return self.item

    # method to link caves
    def link_cave(self, cave_to_link, direction):
        self.linked_caves[direction] = cave_to_link

    def get_details(self):
        print(self.name)
        print("----------")
        print(self.description)
        for direction in self.linked_caves:
            cave = self.linked_caves[direction]
            print("The " + str(cave.get_name()) + " is " + direction + ".\n")

    def move(self, direction):
        if direction in self.linked_caves:
            return self.linked_caves[direction]
        else:
            print("You can't go that way")
            return self

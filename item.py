class Item():
    def __init__ (self, item_name):
        self.itemname = item_name
        self.itemdescription = None
        
     # getters and setters for items
    def set_item(self, item_name):
        self.itemname = item_name

    def __str__(self):
        return self.itemname

    def set_itemname(self, name):
        self.itemname = name

    def set_itemdescription(self, description):
        self.itemdescription = description

    def get_itemdescription(self):
        return self.itemdescription
    
    
    def describe(self):
        print(
            "The [" + self.itemname + "] is here - " + self.itemdescription
        )
    
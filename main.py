from cave import Cave

# create cave objects
cavern = Cave("Cavern")
grotto = Cave("Grotto")
dungeon = Cave("Dungeon")

# set descriptions
cavern.set_description("A dank and dirty cave.")
grotto.set_description("A small cave with ancient graffiti.")
dungeon.set_description("A large cave with a rack.")

cavern.link_cave(dungeon, "south")
grotto.link_cave(dungeon, "east")
dungeon.link_cave(grotto, "west")

cavern.describe()

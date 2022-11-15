lib = shelve.open("my_library", writeback=False)
lib["Divergent trilogy"] = ["Divergent", "Insurgent", "	Allegiant"]
lib["The Lord of the Rings"] = ["The Fellowship of the Ring", "The Two Towers", "The Return of the King", "The Silmarillion"]

# write your code here
temp = lib["The Lord of the Rings"]
temp.pop()
lib["The Lord of the Rings"] = temp


print(len(lib["The Lord of the Rings"]))

lib.close()
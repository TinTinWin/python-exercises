tabby_cat = "\tI'm tabbed in."
persian_cat = "I'am split\non aline."
backslash_cat = "I'am \\ a \\ cat."

fat_cat = """
I'll do a list:
<<<<<<< HEAD
    \t* cat food
=======
    \t* Rat food
>>>>>>> 1af732950770cf1a66605ff13776d6b0dfb12065
    \t* Fishies
    \t* Catnip\n\t* Grass
    """

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)

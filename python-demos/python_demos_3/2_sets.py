# A set is an unordered container of object references
# Set items are unique
fibonacci = {0, 1, 2, 3, 5, 8, 13, 21, 34}
print(fibonacci)

accurate_fibonacci = {0, 1, 1, 2, 3, 5, 8, 13, 21, 34}
print(accurate_fibonacci)

# set from a list
colours = ['red', 'yellow', 'pink', 'green']
print(f"Colours list: {colours}")

colours += ['yellow']
colours.append('red')
print(colours)

colours_set = set(colours)
print(f"Colours Set: {colours_set}")

colours_set.add('orange')
colours_set.add('purple')
print(f"Set with added colours: {colours_set}")

# immutable sets are frozen
fixed_colours = frozenset(['red', 'green', 'blue'])
print(f"Frozen Set: {fixed_colours}")

# fixed_colours.add("This won't work!")

print("\n" + "#" * 50)

# Set Methods
print(f"Colour set before removal: {colours_set}")

colours_set.remove('yellow')
print(f"Colour set after removal: {colours_set}")

# arbitrary colour is popped
popped_colour = colours_set.pop()
print(f"Popped colour is: {popped_colour}")

# discard items from the set
colours_set.discard('purple')
print(f"Colour set after first discard: {colours_set}")

colours_set.discard('black')
print(f"Colour set after second discard: {colours_set}")

# clear the set
colours_set.clear()
print(colours_set)

print("\n" + "#" * 50)

# Exploiting Sets
print(colours)
unique_list_of_colours = list(set(colours))
print(f"Unique colour list: {unique_list_of_colours}")


# repopulate colours set
colours_set = {'red', 'yellow', 'pink', 'green', 'black', 'white', 'grey', 'orange', 'purple', 'blue'}
print(f"Colour Set: {colours_set}")
# use subtract to remove several items from a set
remaining_colours = colours_set - {'white', 'black', 'grey'}
print(f"Remaining colours: {remaining_colours}")


print("\n" + "#" * 50)
# set operators

metallic_colours = {'black', 'gold', 'silver', 'grey', 'bronze'}
print(f"Metallic colour set: {metallic_colours}")
print(f"Standard colour set: {colours_set}")

# intersection &
common_colours = colours_set.intersection(metallic_colours)
print(f"Common colours in both sets: {common_colours}")

common_colours = colours_set & metallic_colours
print(f"Common colours in both sets (using & operator): {common_colours}")

# union |
all_colours = colours_set.union(metallic_colours)
print(f"All colours in both sets: {all_colours}")

all_colours = colours_set | metallic_colours
print(f"All colours in both sets (using | operator): {all_colours}")

# difference -
non_metallic_colours = colours_set.difference(metallic_colours)
print(f"Non-metallic colours: {non_metallic_colours}")

non_metallic_colours = colours_set - metallic_colours
print(f"Non-metallic colours (using - operator): {non_metallic_colours}")

# symmetric difference ^
# items that appear in one set only
non_repeated_colours = colours_set.symmetric_difference(metallic_colours)
print(f"Non repeated colours: {non_repeated_colours}")

non_repeated_colours = colours_set ^ metallic_colours
print(f"Non repeated colours(using - operator): {non_repeated_colours}")

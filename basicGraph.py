V = ['B1', 'B2', 'H1', 'H2', 'H3', 'H4']            # 2 bosses and 4 hired people
E = [                                               # Boss 1 know boss 2 and boss 1 know hired 1 and hired 2
    ['B1', 'B2'], ['B1','H1'], ['B1','H2'],         # Boss 2 know boss 1 and boss 2 know hired 3 and hired 4
    ['B2', 'H3'], ['B2', 'H4'],                     # Every hired person know each other
    ['H1', 'H2'], ['H1', 'H3'], ['H1', 'H4'],
    ['H2', 'H3'], ['H2', 'H4'],
    ['H3', 'H4'] 
    ]

# Who know the Hired 3

def whoKnowPerson(person, E):
    friends = []                # In this list I will add every person that 'person' knows
    for p1,p2 in E:             # Making a loop to check if first or second position in list in list is known by 'person'
        if p1 == person:
            friends.append(p2)  # If it is True add second person to the 'friends' list
        elif p2 == person:
            friends.append(p1)
    return friends

print(whoKnowPerson('H3', E))
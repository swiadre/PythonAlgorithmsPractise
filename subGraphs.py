lines = {
    'AF' : ['EU', 'SA'],        # Imagine that this code is for a intercontinental delivery company
    'NA' : [],                  # AF - Africa                       
    'SA' : ['NA'],              # NA - North America            NA  <------ EU  ------> AS
    'AS' : ['AU'],              # SA - South America            ^           ^            |      Graph look like this
    'AU' : ['AF'],              # AS - Asia                     |           |            v
    'EU' : ['AS', 'NA']         # AU - Austrialia               SA  <------ AF  <------ AU
}                               # EU - Europa
                                # AN - Anctartida
request1 = {
    'AS' : ['AU'],              # In lines dictionary we can see all of possible ways to deliver package
    'AU' : ['AF'],              # In requests are 3 requests from customers
    'AF' : ['EU'],              # Request 1 is possible
    'EU' : ['NA', 'AS']         # Request 2 and 3 isn't possible
}

request2 = {
    'AF' : ['EU'],
    'EU' : ['AU'],
    'AU' : ['NA'],
}

request3 = {
    'AF' : ['SA'],
    'SA' : ['NA'],
    'NA' : ['AN']
}

def isSubGraph(V, V_sub):       # Function to check is delivery possible
    for v in V_sub.keys():      # Checking are vertices from subGraph in graph
        if not v in V.keys():
            return False
        else:
            for e in V_sub[v]:  # Checking are edges from subGraph in graph
                if not e in V[v]:
                    return False
    return True


print(isSubGraph(lines, request1))
print(isSubGraph(lines, request2))
print(isSubGraph(lines, request3))

def merge(list1, list2):
    new_list = []
    iterations = 0
    while list1 and list2:
        if list1[0] > list2[0]:
            new_list.append(list2.pop(0))
        else:
            new_list.append(list1.pop(0))
        iterations += 1
    if list1:
        new_list += list1
    else:
        new_list += list2
    iterations += 1
    return new_list, iterations

def sort1(unordered):
    '''n**2 complexity (I think)'''
    elements = [[i] for i in unordered]
    ordered = []
    iterations = 0
    for i in elements:
        result = merge(ordered, i)
        ordered = result[0]
        iterations += result[1]
    return ordered, iterations

def sort2(unordered):
    '''Only works if length of list is power of 2...'''
    elements = [[i] for i in unordered]
    iterations = 0
    while len(elements) > 1:
#        pairs = [[elements[i],elements[i+1]] for i in range(0, len(elements), 2)]
        pairs = []
        for i in range(0, len(elements), 2):
            try: pairs.append([elements[i], elements[i+1]])
            except IndexError: pairs.append([elements[i]])
        elements = []
        for i in pairs:
            try: 
                x, y = merge(i[0], i[1])
                elements.append(x)
                iterations += y
            except IndexError:
                elements.append(i)
                iterations += 1
    return elements, iterations

def sort3(unordered):
    '''This does it I think!'''
    elements = [[i] for i in unordered]
    iterations = 0
    ordered = []    
    while len(elements) > 1:
#        pairs = [[elements[i],elements[i+1]] for i in range(0, len(elements), 2)]
        if len(elements) % 2 != 0:
            x, y = merge(elements[-2], elements[-1])
            elements[-2] = x
            elements.pop(-1)
            iterations += y
        pairs = []
        for i in range(0, len(elements), 2):
            try: pairs.append([elements[i], elements[i+1]])
            except IndexError: pairs.append([elements[i]])
        elements = []
        for i in pairs:
            try: 
                x, y = merge(i[0], i[1])
                elements.append(x)
                iterations += y
            except IndexError:
                elements.append(i)
                iterations += 1
    return elements, iterations

    

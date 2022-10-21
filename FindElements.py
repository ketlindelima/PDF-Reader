# Function to find the specific elements
def find_in_list(Word_to_find, list_with_texts):
    cont = 0
    position_list = []
    result =[]
    for elements in list_with_texts:
        if elements == Word_to_find:
            position_list.append(cont)
        cont+=1
    for position in position_list:
        result.append(list_with_texts[position+1])
    return result
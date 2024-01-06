string = input("Input a string of characters: ")

def count_and_say(input):

    char_occurences = {}

    for i in string:
        if i in char_occurences:
            char_occurences[i] += 1
        else:
            char_occurences[i] = 1

    convert = {1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine", 10: "Ten"}
    

    

    for i in char_occurences:
        for x in convert:
            if char_occurences[i] == x:
                #print(convert[x], i,"s")
                print(f'{convert[x]} {i}s')
        
        #print(i,":",char_occurences[i])

count_and_say(string)

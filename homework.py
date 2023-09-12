


def get_count(sentence):
    count = 0   #O(1)
    vowel_list = []   #O(1) 
    vowels = "aeiou"   #O(1)
    for letter in sentence:  #O(1) 
        if letter.lower() in vowels: #O(1)
            count+=1 #O(1)
    return count  #O(1)
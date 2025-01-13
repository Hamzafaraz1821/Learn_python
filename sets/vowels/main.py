def count_vowels(text):

    vowels_set = set()
    count = 0
    for c in text:
        if c in {"a", "e", "i" , "o" , "u" , "A" , "E" , "I" , "O" , "U"}:
            count += 1
            vowels_set.add(c)
    
    return count,vowels_set

            


def filter_messages(messages):
    filtered_msgs = []
    count = []

    for msg in messages:
        words = msg.split()
        non_bad_words = []
        counter = 0

        for word in words:
            if word == "dang":
                counter+=1
            else:
                non_bad_words.append(word)

        sentence = " ".join(non_bad_words)
        filtered_msgs.append(sentence)
        count.append(counter)
    
    return filtered_msgs,count

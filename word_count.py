def word_count(sentence:str)->dict:
    word_count_dict = {}
    ind_word = sentence.split()
    for i in ind_word:
        word_count_dict[i] = sentence.count(i)
    return word_count_dict
print(word_count("hello hi hello hi hello"))

def single_root_words(root_word, *other_words):
    same_words = []
    for i in other_words:
        i_low = i.lower()
        low_root_word = root_word.lower()
        if (low_root_word in i_low) or (i_low in low_root_word):
            same_words.append(i)
    return same_words
result_1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result_2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
result_3 = single_root_words('ЛеСной', 'Лес', 'поЛесНОй', 'Лесник', 'Лесно')    # на орфографию пожалуйста не смотреть :)
print(result_1)
print(result_2)
print(result_3)
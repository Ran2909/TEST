words= {}
print("Enter multiple words and their translations. e.g. hello 你好")
while True:
    user_input = input()
    # 输入空字符则跳出循环
    if user_input == "":
        break
    # 将英语单词和译文作为键值对录入字典
    word, translation = user_input.split()
    words[word] = translation

print("Enter a word to translate:")
while True:
    # 用户输入单词
    word_to_translate = input()
    if word_to_translate=='':
        break
    # 检查字典中是否有输入的单词
    if word_to_translate in words:
        # 有则翻译
        print(words[word_to_translate])
    else:
        # 没有则报错
        print("Word not found in dictionary")
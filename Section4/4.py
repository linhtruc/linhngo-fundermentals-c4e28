dic  = {
    "hello": "你好",
    "mother": "妈妈",
    "father": "爸爸"
}
while True:
    print(dic.keys())
    search = input("Enter a word: ")
    if search in dic:
        print (dic[search])
    else:
        question = input("Add new word? (y or n)").lower()
        if question == "n":
            print ("Bye")
            break
        elif question == "y":
            meaning = input("Your translation: ")
            dic[search] = meaning
    print(dic)        

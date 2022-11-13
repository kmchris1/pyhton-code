# write a code that will automatically translate an input from a user to ENGLISH.
# And if that input from user does not exixt in your ditionary, 
# simply return "input" does not exixt in the dictionary.
which_language = input("in which language do you want your sentence to be translated:")

english_to_french={
"prune" : "Plum",
"moi": "Me",
"lit": "Bed",
"soleil": "Sun",
"computer": "Ordinateur",
"africa": "Afrique"
}

if which_language=="french":
    french_word = input("Enter a word in french. The word must start with a Capital letter\n")
    french_word= french_word.lower()
    ## get value from the key received from the user input (which is the Key!!)
    translation = english_to_french.get(french_word)
    if french_word in english_to_french:
        print(translation)
    elif french_word not in  english_to_french: 
        print(f"{french_word} does not exist in the dictionary")
else:
    print("your language in not avalaible in my dictionary")



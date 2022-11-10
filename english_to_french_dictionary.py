# write a code that will automatically translate an input from a user to ENGLISH.
# And if that input from user does not exixt in your ditionary, 
# simply return "input" does not exixt in the dictionary.
which_language = input("in which language do you want your sentence to be translated:")

english_to_french={
"Prune" : "Plum",
"Moi": "Me",
"Lit": "Bed",
"Soleil": "Sun",
"Computer": "Ordinateur",
"Africa": "Afrique"
}

if which_language=="french":
    my_frenchW = input("Enter a word in french. The word must start with a Capital letter\n")
    translation = english_to_french.get (my_frenchW)
    if my_frenchW in english_to_french:
        print(translation)
    elif my_frenchW not in  english_to_french: 
        print(f"{my_frenchW} does not exist in the dictionary")
else:
    print("your language in not avalaible in my dictionary")



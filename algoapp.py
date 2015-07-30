__author__ = 'Baxter'

from tkinter import *
from re import search, sub

def evaluate(event):
    res.configure(text = inputty())#str(entry.get()))

def sorter(daInput):  # function replaces vowels and

    searcher = [r"u[\(\)][rg]", r"g+|l+|r+|s+|v+|ng|[ckmnpqtwy]", r"[aiu]"]  # goes through each item then replaces with
    replacer = [r"D", r"C", r"V"]  # D, C, or V

    for x in range(0, 3):
        daInput = sub(searcher[x], replacer[x], daInput)

    return daInput


def autofinder(gemmy):
    if search(r"[Ve][CD]VV", gemmy):  # is there gemination
        return True
    else:
        return False


def tiago(splitter):
    searches = [r"C'", r"CC", r"DC", r"(?<!\|)(?<=V|e)[DC](?!\||\Z|!)",
                r"(?<!\w)[CD]*[Ve]\|"]  # finding all open instances
    replaces = [r"C!|C", r"C|C", r"C|C", r"|C", r"Op|"]

    for y in range(0, 5):
        splitter = sub(searches[y], replaces[y], splitter)

    return splitter.split("|")

def inputty():
    word = sorter(str(entry.get()))  # takes input and sorts it
    separator = tiago(word)  # takes from sorted

    if autofinder(word):
        auto = []
        gemmies = ["CVV", "CVVC", "DVV", "DVVC"]
        for lex in range(0, len(separator)):
            for gemmy in gemmies:  # finding place of gemination
                if separator[lex] == "Op" and (separator[lex + 1] == gemmy):
                    auto.append(lex)

    for item in range(0, len(separator)):  # if it's not open or geminated, it's closed
        if "!" in separator[item]:
            separator[item] = "Gem"

        elif separator[item] != "Op" and separator[item] != "Gem":
            separator[item] = "Cl"

        if item > 0:
            if separator[item] == "Op" and separator[item - 1] == "Op":
                separator[item] = "Len"
            if separator[item] == "Op" and separator[item - 1] == "Gem":
                separator[item] = "Cl"

    if autofinder(word) and auto:
        for i in auto:
            if separator[i] == "Op":
                separator[i] = "Gem"

    separator[len(separator) - 1] = "Dwn"  # always down
    final = '|'.join(separator)
    return final


w = Tk()
Label(w, text="Type a Yup'ik word.").pack()
entry = Entry(w)
entry.bind("<Return>", evaluate)
entry.pack()
res = Label(w)
res.pack()
w.mainloop()
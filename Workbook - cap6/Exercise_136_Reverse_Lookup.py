#funzione reverseLookup

def reverseLookup(dic, t):
    k = []
    for key in dic:
        if dic[key] == t:
            k.append(key)
    return k

def main():
    Scrittori = {"J.R.R. Tolkien": "Il Signore degli Anelli", "George R.R.": "Il Trono di Spade", "J.K. Rowling": "Harry Potter", "C.S. Lewis": "Le Cronache di Narnia"}
    print("J.R.R. Tolkien ha scritto: {}".format(reverseLookup(Scrittori, "Il Signore degli Anelli")))
    print("George R.R ha scitto: {}".format(reverseLookup(Scrittori, "Il Trono di Spade")))
    print("J.K. Rowling ha scitto: {}".format(reverseLookup(Scrittori, "Harry Potter")))
    print("Arthur Conan Doyle ha scitto: {}".format(reverseLookup(Scrittori, "Sherlock Holmes")))

main()

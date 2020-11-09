def decodifica(x):
    if not text:
        return []
    else:
        caratteri = x[0]
        q = x[1]
        return [caratteri] * q + decodifica(x[2:])


def main():
    ex = ['A', 12, 'B', 4, 'A', 6, 'B', 3]
    print("La lista compressa è: {}".format(ex))
    print("L'elenco decompresso è: "
          "{}".format(decodifica(ex)))


if __name__ == "__main__":
    main()

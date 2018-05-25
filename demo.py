from ghostwriter import make_sentence, build_chain, get_words


def main():
    words = get_words('text.txt')
    print(words)
    chain = build_chain(words)
    print(chain)
    sentence = make_sentence(chain, 20)
    print(sentence)


if __name__ == '__main__':
    main()
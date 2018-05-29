from ghostwriter import Chain


def main():
    chain = Chain()
    chain.load('text.txt')
    sentence = chain.generate(wc=20)
    print(sentence)


if __name__ == '__main__':
    main()
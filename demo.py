import sys
from ghostwriter import Chain


def main():
    args = sys.argv
    chain = Chain()
    chain.load(args[1])
    sentence = chain.generate(wc=40)
    print(sentence)


if __name__ == '__main__':
    main()
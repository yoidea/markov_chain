import MeCab
import random
import re


def make_sentence(chain, wc=20):
    selected, _ = random.choice(list(chain.items()))
    sentence = selected
    for i in range(wc):
        if selected in chain:
            selected = random.choice(chain[selected])
            sentence += selected
        else :
            selected, _ = random.choice(list(chain.items()))
    return sentence


def build_chain(words):
    chain = {}
    for i in range(len(words)-1):
        if words[i] in chain:
            chain[words[i]].append(words[i+1])
        else :
            chain[words[i]] = []
            chain[words[i]].append(words[i+1])
    return chain


def get_words(fname='text.txt'):
    with open(fname, 'r') as f:
        text = f.read()
    mecab = MeCab.Tagger('-Owakati')
    words = mecab.parse(text)
    words = re.findall('\w+', words)
    return words


def main():
    words = get_words()
    print(words)
    chain = build_chain(words)
    print(chain)
    sentence = make_sentence(chain)
    print(sentence)


if __name__ == '__main__':
    main()
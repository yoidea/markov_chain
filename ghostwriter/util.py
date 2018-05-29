import MeCab
import random
import re


class Chain:
    chain = {}
    def load(self, fname='text.txt'):
        with open(fname, 'r') as f:
            text = f.read()
        mecab = MeCab.Tagger('-Owakati')
        words = mecab.parse(text)
        words = re.findall('\w+', words)
        # return words

        self.chain = {}
        for i in range(len(words)-1):
            if words[i] in self.chain:
                self.chain[words[i]].append(words[i+1])
            else :
                self.chain[words[i]] = []
                self.chain[words[i]].append(words[i+1])
        # return self.chain

    def make(self, wc=20):
        selected, _ = random.choice(list(self.chain.items()))
        sentence = selected
        for i in range(wc):
            if selected in self.chain:
                selected = random.choice(self.chain[selected])
                sentence += selected
            else :
                selected, _ = random.choice(list(self.chain.items()))
        return sentence


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
    chain = Chain()
    chain.load('../text.txt')
    sentence = chain.make(wc=20)
    print(sentence)


if __name__ == '__main__':
    main()
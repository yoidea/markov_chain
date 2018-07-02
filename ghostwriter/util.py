import MeCab
import random
import re


class Chain:
    words = []
    chain = {}
    # def __init__(self, echo):
    # print(echo)
    def load(self, fname='text.txt'):
        with open(fname, 'r') as f:
            text = f.read()
        mecab = MeCab.Tagger('-Owakati')
        self.words = mecab.parse(text)
        self.words = re.findall('\w+', self.words)
        self.chain = {}
        for i in range(len(self.words)-1):
            if self.words[i] in self.chain:
                self.chain[self.words[i]].append(self.words[i+1])
            else :
                self.chain[self.words[i]] = []
                self.chain[self.words[i]].append(self.words[i+1])


    def generate(self, wc=20):
        selected, _ = random.choice(list(self.chain.items()))
        sentence = selected
        for i in range(wc):
            if selected in self.chain:
                selected = random.choice(self.chain[selected])
                sentence += selected
            else :
                selected, _ = random.choice(list(self.chain.items()))
        return sentence


def main():
    chain = Chain()
    chain.load('../text.txt')
    sentence = chain.generate(wc=20)
    print(sentence)


if __name__ == '__main__':
    main()
# coding:utf8
'''
Run in nlp env: `source activate nlp`
'''
import sys
from gensim.models import Word2Vec

def load_model(path):
    return Word2Vec.load(path)

def vec(modelfp, word):
    return load_model(modelfp).wv[word]

def similar(modelfp, word):
    wv = load_model(modelfp).wv
    return wv.most_similar(word,topn=20)

def similar2(modelfp, positives, negtives):
    wv = load_model(modelfp).wv
    if negtives is None:
        print('no negtives.')
        result = wv.most_similar(positive=positives)
    else:
        print('has negtives.')
        result = wv.most_similar(positive=positives, negative=negtives)
    for x in result:
        print("{}: {:.4f}".format(*x))

def main():
    model_filep = sys.argv[2]
    word = sys.argv[3]
    if sys.argv[1] == 'vec':
        print('vec: {}'.format(vec(model_filep, word)))

    elif sys.argv[1] == 'simi':
        for simi in similar(model_filep, word):
            print('{}'.format(simi))

    elif sys.argv[1] == 'simi2':
        positives = word.split(" ")
        print(len(sys.argv))
        negtives = sys.argv[4].split(" ") if len(sys.argv) > 4 else None
        print('get poss: %s, negs: %s' % (positives, negtives))
        similar2(model_filep, positives, negtives)

    else:
        print('Usage: tail -n 50 evalute.py')

if __name__ == '__main__':
    main()

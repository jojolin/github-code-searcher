# coding:utf8
'''
Run in nlp env: `source activate nlp`
'''
from gensim.models import Word2Vec
import sys
import time

def load_sens(filep):
    print('load sens from: {}'.format(filep))
    sens = []
    with open(filep, 'r', encoding='utf8') as r:
        lines = r.readlines()
        for line in lines:
            sens.append(line.strip().split(' '))
    return sens

def load_model(path):
    return Word2Vec.load(path)

def train(model_path, sens, init=False):
    print('start training model: {}, len(sens): {}'.format(model_path, len(sens)))

    modelfp = model_path.split('_')[0] + '_' + time.strftime('%y%m%d%H%M')

    if init:
        model = Word2Vec(sens, size=100, window=5, min_count=1, workers=4)
        model.save(modelfp)
    else:
        model = load_model(model_path)
        model.build_vocab(sens, update=True)
        model.train(sens, total_examples=len(sens), epochs=1)
        model.save(modelfp)

    print('save model to: {}'.format(modelfp))

def main():
    try:
        if sys.argv[1] == 'train':
            data_filep = sys.argv[2]
            pre_model_filep = sys.argv[3] if len(sys.argv) > 3 else 'model/w2v.model'
            init = sys.argv[4] == 'true' if len(sys.argv) > 4 else False
            sens = load_sens(data_filep)
            train(pre_model_filep, sens, init)

    except Exception as ex:
        print(ex)
        print('tail -n 50 w2v.py')

if __name__ == '__main__':
    main()

# coding: utf8
import requests
import sys
import re
import logging
import time

URL = "https://github.com/search?p={pn}&q={q}&l={l}&s=stars&type=Repositories"
NUM_CODEBASE = 11

def downloads(lastpage, query, lan):
    codebases_fp = 'urls/q_%s_l_%s_lpg_%s_%s.txt' % (query, lan, lastpage, int(time.time()))
    with open(codebases_fp, 'w') as w:
        for x in range(lastpage, lastpage + NUM_CODEBASE):
            codebases = download(x, query, lan)
            time.sleep(3)

            for cb in codebases:
                w.write(cb + '.git\n')
                logging.info(cb + '.git')

            w.flush()

    logging.info('^----^ write codebases se to: %s' % codebases_fp)

def download(pn, query, lan):
    '''
    '''
    url = URL.format(pn=pn, q=query, l=lan)
    logging.info('get url: %s' % url)
    resp = requests.get(url)
    content = resp.text
    codebases = re.findall('(https://github.com/.*/.*)&quot;}', content)
    return codebases

def main():
    '''
    Usage: python codebase_dl.py 1 python Python
    '''
    q = sys.argv[1]
    l = sys.argv[2]
    lastpage = int(sys.argv[3])

    logging.basicConfig(level=logging.DEBUG)

    downloads(lastpage, q, l)

if __name__ == '__main__':
    main()

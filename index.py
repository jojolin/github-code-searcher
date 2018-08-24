# coding: utf8
'''
tree -afi projects | grep -F .py | python index.py > pyfile.txt
'''
import sys
import logging
import keyword
import time

TICK_PUNCS = (
        '.', '=', '+', '-', '*', '/', '>', '!', '/', '%', '&', '|', '^', '~', '>', '<', '<', '>'
        ,"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"
        , '"', "'", ':', ',', '[',']', '(', ')', '\\', '#'
        )

KEYWORDS = keyword.kwlist
KEYWORDS.extend(['self'])

def readlines(f):
    with open(f, 'r', encoding='utf8') as r:
        lines = r.readlines()
        logging.debug(lines)
    return lines

def index(files):
    handle_lines = []
    for f in files:
        logging.info('***** indexing file: %s' % f)
        try:
            lines = readlines(f.strip())
            for line in lines:
                line = line.strip()
                # remove \t, \n ...
                if line == '':
                    continue

                line2 = ''
                for c in line:
                    line2 += c if (not c in TICK_PUNCS) else ' '

                line2arr = [x for x in line2.split(' ')
                        if not (x.strip() == '' or x in KEYWORDS or len(x)==1)]
                if len(line2arr) == 0:
                    continue
                handle_lines.append(line2arr)

        except Exception as ex:
            logging.error(ex)

    sens_fp = 'pyfile2sens/sens_%s.txt' % int(time.time())
    with open(sens_fp, 'w', encoding='utf8') as w:
        for l in handle_lines:
            w.write(' '.join(l)+'\n')
        w.flush()
    logging.info('^-----^ save sens to: %s, lines: %s' % (sens_fp, len(handle_lines)))

def main():
    logging.basicConfig(level=logging.INFO)

    files = sys.stdin.readlines()
    index(files)

if __name__ == '__main__':
    main()

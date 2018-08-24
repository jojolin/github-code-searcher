# coding: utf8
import subprocess
import sys
import logging
import re
import os

def downloads(urls_fp):
    res = re.search('q_(.*)_l_(.*)_lpg_(.*)_', urls_fp)
    query = res.group(1)
    lan = res.group(2)
    projects_dir = 'projects-%s-%s' % (query, lan)
    if not os.path.exists(projects_dir):
        logging.info('make dir: %s' % projects_dir)
        os.mkdir(projects_dir)

    with open(urls_fp, 'r') as r:
        urls = r.readlines()
        for url in urls:
            try:
                cmd = 'cd %s && git clone %s' % (projects_dir, url)
                logging.info('run cmd: %s' % cmd)
                subprocess.check_output(cmd, shell=True)
                logging.info('finished: %s' % cmd)
            except subprocess.CalledProcessError as ex:
                logging.error(ex)

def main():
    '''
    Usage: python codebase_downloader.py 2 python Python
    '''
    fp = sys.argv[1]
    logging.basicConfig(level=logging.INFO)
    downloads(fp)

if __name__ == '__main__':
    main()

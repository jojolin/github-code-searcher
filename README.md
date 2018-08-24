# github code searcher
- **search the code on github**
- !! this is a working project.
- The original purpose is to index the code on github for search when you're coding.
- I train the code words with gensim word2vec in order to find something instesting :) ,
Below is some thing I have found, not much interesting! :( .
- You can download the model I've train on [baiduyun](https://pan.baidu.com/s/1pcWFe7iN8BHTVZx-U8Btww)

```
(nlp) jzlin@ubuntu1604:~/projects/github-code-searcher$ python evaluate.py simi model/w2v-crawler.model_1808240908 "music"
('displays', 0.8816262483596802)
('fan', 0.866743803024292)
('Play', 0.864991307258606)
('chosen', 0.8623303174972534)
('Music', 0.8546586036682129)
('locations', 0.8537720441818237)
('JS', 0.8529238700866699)
('TV', 0.8517374992370605)
('py`', 0.8490191102027893)
('RPM', 0.8485977649688721)
('Search', 0.8452662229537964)
('Perform', 0.8422566056251526)
('Delete', 0.8419909477233887)
('appearance', 0.8417656421661377)
('convention', 0.8415013551712036)
('configurations', 0.8412063717842102)
('player', 0.8404814004898071)
('Edit', 0.8395481705665588)
('Various', 0.838516116142273)
('assets', 0.8384709358215332)
(nlp) jzlin@ubuntu1604:~/projects/github-code-searcher$ python evaluate.py simi model/w2v-crawler.model_1808240908 "video"
('audio', 0.8401792049407959)
('Retrieve', 0.836071789264679)
('bitmap', 0.8279837369918823)
('Ocean', 0.826748251914978)
('Fetch', 0.8232293128967285)
('Dump', 0.8215538263320923)
('busybox', 0.8212484121322632)
('showing', 0.8186784982681274)
('Excessive', 0.8176584243774414)
('Download', 0.8175103068351746)
('save_icon', 0.8164739608764648)
('alpine', 0.8164356350898743)
('Reads', 0.8155316710472107)
('sound', 0.8125374913215637)
('CRC', 0.8110506534576416)
('CSV', 0.8094253540039062)
('tracks?', 0.8090611696243286)
('RPM', 0.8089923858642578)
('Copy', 0.808255136013031)
('mailcap', 0.8066860437393188)
(nlp) jzlin@ubuntu1604:~/projects/github-code-searcher$ python evaluate.py simi model/w2v-crawler.model_1808240908 "recipe"
('_path_created', 0.9407172203063965)
('tablenames', 0.9297967553138733)
('CONF_TIME_ZONE', 0.9293851852416992)
('vc_env', 0.9277179837226868)
('_aliases', 0.9248013496398926)
('renewal_config', 0.9235639572143555)
('dev_ids', 0.9209914803504944)
('ATTR_EVENT_TYPE', 0.9205851554870605)
('_is_resuming', 0.918769121170044)
('__bvar', 0.917309045791626)
('regexdisplay', 0.9162708520889282)
('__table__', 0.9157921671867371)
('build_opts', 0.9148204326629639)
('extra_cflags', 0.9146658778190613)
('__uwd', 0.9140105247497559)
('__uoc', 0.9137064218521118)
('remote_labels', 0.9132829904556274)
('__gvar', 0.9129780530929565)
('buildrecipe', 0.9128351211547852)
('preload_options', 0.9123343825340271)
```

## code usage
### search codebases
  - e.g. search `crawler` with language `Python` 
    - `python codebase_se.py crawler Python 1`

### download codebases
  - `python codebase_dl.py urls/q_xx.txt`

### find pyfiles
  - require `tree` installed on your system
  - `tree -afi projects-xx | grep -F .py > pyfile/pyfile-xx.txt`
  - `wc -l pyfile/pyfile-xx.txt`

### trans files to sens
  - (use line 1-100000? :) ) `sed -n '1,100000p' pyfile/pyfile-xx.txt > pyfile100000.txt`
  - `cat pyfile/pyfile-xx.txt | python index.py`

### train
- require packages:
  - gensim 

- init
  - `python w2v.py train pyfile2sens/sens.txt model/w2v.model true`

- continue train
  - `python w2v.py train pyfile2sens/sens.txt model/w2v.model`

- evaluate
  - `python evaluate.py simi model/w2v-crawler.model_1808240908 "music"`


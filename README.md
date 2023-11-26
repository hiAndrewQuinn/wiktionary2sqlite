# `wiktionary2sqlite`
Lil side project to generate a SQLite database I can easily look up words from based on the English Wiktionary dumps.

## Quickstart

Begin by downloading one of the Wiktionary XML dumps. For example, the one [here](https://dumps.wikimedia.org/enwiktionary/20231120/) titled `enwiktionary-20231120-pages-articles.xml.bz2` (1.1 GB). Unzip it with `bunzip2`, and then just

```bash
python main.py /wherever/enwiktionary....xml/is
```

It'll take a while, but at the end you should have a brand new `db.sqlite3` in your pwd with a 2-column table: `word` and `text_wt`.

## Help text

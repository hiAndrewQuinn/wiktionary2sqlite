# `wiktionary2sqlite`
Lil side project to generate a SQLite database I can easily look up words from based on the English Wiktionary dumps.

## Quickstart

⚠️: The CLI interface requires [Typer](https://typer.tiangolo.com/). Run `pip install typer` if you don't have it.

Begin by downloading one of the Wiktionary XML dumps. For example, the one [here](https://dumps.wikimedia.org/enwiktionary/20231120/) titled `enwiktionary-20231120-pages-articles.xml.bz2` (1.1 GB). Unzip it with `bunzip2`, and then just

```bash
python main.py /wherever/enwiktionary....xml/is
```

It'll take a while, but at the end you should have a brand new `db.sqlite3` in your pwd with a 2-column table: `word` and `text_wt`.

## Help text

![image](https://github.com/hiAndrewQuinn/wiktionary2sqlite/assets/53230903/cfa2ef45-a2dc-42a3-92f4-6d479b02df46)

## Interactive dictionary lookup with `sqlite-utils` and `fzf`

```bash
sqlite-utils enable-fts db.sqlite3 entries word --create-triggers
echo '' | fzf --preview 'sqlite-utils search db.sqlite3 entries {q} | jq ".[0].text_wt" | xargs echo -e'
```

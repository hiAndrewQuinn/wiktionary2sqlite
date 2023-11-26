import xml.etree.ElementTree as ET
import sqlite3
import typer
import logging

app = typer.Typer()


def setup_logging(debug_mode: bool):
    """Set up logging configuration."""
    if debug_mode:
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.INFO)


def process_page(cursor, title, text):
    # Add to SQLite database
    cursor.execute("INSERT INTO entries (word, text_wt) VALUES (?, ?)", (title, text))
    logging.debug(f"Added word: {title}")


@app.command()
def main(
    xml_file: str,
    db_file: str = typer.Option("db.sqlite3", help="Path to the SQLite database file"),
    debug: bool = typer.Option(False, "--debug", help="Enable debug mode"),
):
    # Set up logging
    setup_logging(debug)

    # Connect to SQLite database
    conn = sqlite3.connect(db_file)

    # Create a new table
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS entries (
            word TEXT,
            text_wt TEXT
        )
        """
    )
    conn.commit()

    c = 0
    # Parse the XML file
    for event, elem in ET.iterparse(xml_file, events=("start", "end")):
        if event == "start" and elem.tag.endswith("page"):
            title = None
            text = None
        elif event == "end":
            if elem.tag.endswith("title"):
                title = elem.text
            elif elem.tag.endswith("text"):
                text = elem.text
            elif elem.tag.endswith("page"):
                if title and text:
                    c += 1
                    process_page(cursor, title, text)
                elem.clear()  # Clear the element to free memory
        if c % 10000 == 0:
            logging.info(f"Processed {c} pages")
    conn.commit()
    conn.close()


if __name__ == "__main__":
    app()

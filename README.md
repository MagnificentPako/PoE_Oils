# PoE Oil Filter

## Installation

Clone this repo and run `pip install -r requirements.txt`.

## First-time Usage

Before running the main script you will have to populate a list of anoints by running `python scrape_mods.py`, this will create a new file, `anoints.p`. You also have to create a `.env` file, similar to the example provided, with your POESESSIONID taken from the website, your _account_ name, and the tab index (counting from the start at 0, just go down your list of tabs until you reach the desired tab). You can also change the Threshold in `main.py`; the default is Opalescent and above.

## Usage
Running `python main.py` will result in a list of jewelry with anoints that might be desireable to extract.
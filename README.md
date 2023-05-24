# Data Carver

Let's say you want to search cars.com for cars around you, and want to compile all of the data. This is the function that Data Carver fits to serve. Data Carver will scrape all of the car listings from any cars.com search URL you give it. In addition, you have the option of generating a .csv file from the given data.

NOTE: Only tested on Linux Mint, Windows version under development

## Installation

0. Ensure you have Firefox installed to the default location
1. Download and extract the .zip at <https://github.com/ElijahTyler/Data-Carver.git>
2. Open Terminal in the project directory and type `python -m pip install -r requirements.txt`

## Usage

IMPORTANT: Open `main.py` and add your personal cars.com search URLs (example is in the file), otherwise nothing will happen once you run the file.

Open Terminal in the project directory and type `python main.py`. This will open an automated Firefox window that will scrape the cars.com webpage for all car listings. Then, a CarListing object is created for each listing it finds. Lastly, `listings.json` will be created, a dictionary of all listings found.

If you want, you can use CarData.py to create a .csv file with all of your listings. To do so, open Python in your terminal with `/bin/python3` and run the following commands:

```python
from CarData import CarData
data = CarData('your_file_here.json')
data.generate_csv('your_file_here.csv')
```

This, by default, will generate a .csv file named `CarData.csv`. You can pass in whatever name you like.

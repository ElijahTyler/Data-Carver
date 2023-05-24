from bs4 import BeautifulSoup
import re
import json

class CarListings:
    def __init__(self, obj = None) -> None:
        if not obj:
            self.year = -1
            self.make = ""
            self.model = ""
            self.mileage = -1
            self.price = -1
            self.dealer = ""
        else:
            def extract_nums(string): # returns -1 if no numbers found
                temp = re.sub("[^0-9]", "", string)
                if temp:
                    return int(temp)
                else:
                    return -1
            
            soup = BeautifulSoup(obj, 'html.parser')
            # year
            year_make_model = soup.a.h2.text.strip()
            self.year = year_make_model.split(" ")[0]
            # make
            self.make = year_make_model.split(" ")[1]
            # model
            model = ""
            for i in range(2, len(year_make_model.split(" "))):
                model += year_make_model.split(" ")[i] + " "
            self.model = model.strip()
            # mileage
            self.mileage = extract_nums(soup.find(attrs={"class": "mileage"}).text.strip().split(" ")[0])
            # price
            self.price = extract_nums(soup.find("span", attrs={"class": "primary-price"}).text.strip())
            # dealer
            self.dealer = soup.find(attrs={"class": "dealer-name"}).text.strip()

    def __str__(self) -> str:
        return f'{self.year} {self.make} {self.model} - {self.mileage} miles - ${self.price} - {self.dealer}'

    def to_dict(self) -> dict:
        # make dictionary of all attributes
        return {
            "year": self.year,
            "make": self.make,
            "model": self.model,
            "mileage": self.mileage,
            "price": self.price,
            "dealer": self.dealer
        }
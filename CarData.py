import json
import csv

class CarData:
    def __init__(self, jason = None) -> None:
        # takes in a .json file generated from dictionary of CarListings
        self.years = []
        self.makes = []
        self.models = []
        self.mileages = []
        self.prices = []
        self.dealers = []
        if not jason:
            return
        with open(jason, 'r') as f:
            self.data = json.load(f)
            for c in self.data:
                car = self.data[c]
                self.years.append(car["year"])
                self.makes.append(car["make"])
                self.models.append(car["model"])
                self.mileages.append(car["mileage"])
                self.prices.append(car["price"])
                self.dealers.append(car["dealer"])

    def generate_csv(self, name = None):
        if not name:
            name = "CarData.csv"
        if not name.endswith(".csv"):
            name += ".csv"
        
        with open(name, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["Year", "Make", "Model", "Mileage", "Price", "Dealer"])
            for i in range(len(self.years)):
                writer.writerow([self.years[i], self.makes[i], self.models[i], self.mileages[i], self.prices[i], self.dealers[i]])
        
        print(f"CSV file generated: {name}")
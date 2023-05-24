from CarData import CarData

data = CarData("listings.json")
data.generate_csv("CarData.csv")
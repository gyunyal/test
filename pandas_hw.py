# Pandas Homework

import csv
import pandas as pd
import numpy as np
import csv
from sklearn.datasets import load_iris

# with open('hotels.csv', newline='') as csvfile:
#     hotelsreader = csv.reader(csvfile)
# for row in hotelsreader:
#     print(', '.join(row))

hotels=pd.read_csv("hotels.csv")
pd.read_csv("hotels.csv", sep = ';', delimiter = None, names=None)
hotels = pd.read_csv("hotels.csv", sep = ';' )
# print(hotels)

# How many rows and columns are there in your file?
print(hotels.shape)

# Print row 3-8 ( using iloc/loc).
print(f"Print row 3-8: {hotels.iloc[2:7]}")

# Filter the data score below 2
for idx in hotels.index:
    if hotels["rating"][idx] < 2:
        print(f'Score below 2: {hotels["rating"][idx]}')

# Find the mean number of all-inclusive hotels across all destinations.
mean = hotels['num_of_all-inclusive_hotels'].mean()
print(f"Number of all-inclusive hotels: {mean}")

# Find the lowest scoring destination.
min1 = hotels['rating'].min()
print(f' The lowest scoring: {hotels["Destinations"][min1]}')

# Find the highest scoring destination.
max = hotels['rating'].max()
print(f"The highest scoring destination is: {hotels['Destinations'][max]}")

# Find all the destinations where there are more than 9 all-inclusive hotels.
for des in hotels.index:
    if hotels["num_of_all-inclusive_hotels"][des] > 9:
        print(f'Destinations with more than 9 all-inclusive hotels: {hotels["the_most_visited"][des]}')


# Filter the data by score above 8.
for fil in hotels.index:
    if hotels["Feedback"][fil] > 8:
        print(f'Score above 8: {hotels["the_most_visited"][fil]}')


# data=load_iris()
# df=pd.DataFrame(data["data"], columns=data[""])
# df["rating"]=data["Destinations"]
# df.head()
# df.groupby("rating").mean().plot.bar()

# myseries = pd.Series([439, 98.54, 'Hello World', 'Sea Breeze', -342])
# mylist = [439, 98.54, 'Hello World', 'Sea Breeze', -342]
# print(myseries)
# print(mylist)

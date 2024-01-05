# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas

data = pandas.read_csv("weather_data.csv")
# print(data)
# print(type(data["temp"])) # pandas.core.series.Series

data_dict = data.to_dict()
print(data_dict)

temp_list = data["temp"].to_list()
print(temp_list)

# average = sum(temp_list) / len(temp_list)
# print(average)

average = data["temp"].mean()
print(average)

max_temp = data["temp"].max()
print(max_temp)

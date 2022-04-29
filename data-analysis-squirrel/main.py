import pandas as pa

squirrel_data = pa.read_csv("Squirrel_data.csv")

squirrel_gray_color = squirrel_data[squirrel_data["Primary Fur Color"] == 'Gray']
squirrel_black_color = squirrel_data[squirrel_data["Primary Fur Color"] == 'Black']
squirrel_cinnamon_color = squirrel_data[squirrel_data["Primary Fur Color"] == 'Cinnamon']

gray_count = len(squirrel_gray_color["Primary Fur Color"].to_list())
black_count = len(squirrel_black_color["Primary Fur Color"].to_list())
cinnamon_count = len(squirrel_cinnamon_color["Primary Fur Color"].to_list())

color_dict = {
    "Gray": [gray_count],
    "Black": [black_count],
    "Cinnamon": [cinnamon_count]
}


squirrel = pa.DataFrame.from_dict(color_dict)
print(squirrel)

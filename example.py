from K_mean import K_mean

x = [14, 48, 83, 74, 54, 37, 7, 11, 34, 56, 15, 46, 77, 37, 34, 42, 53, 99, 5, 18, 94, 8, 51, 96, 97, 72, 69, 58, 30, 62, 82, 4, 27, 64, 19, 21, 81, 18, 40, 80, 90, 77, 85, 18, 5, 25, 99, 86, 90, 46]
y = [64, 59, 10, 34, 89, 89, 97, 39, 77, 23, 3, 69, 90, 91, 55, 14, 59, 32, 53, 20, 98, 13, 98, 99, 44, 82, 46, 47, 32, 22, 83, 66, 21, 28, 24, 36, 73, 61, 46, 34, 46, 38, 42, 96, 100, 0, 29, 52, 83, 70]
z = [62, 13, 2, 19, 90, 69, 61, 36, 64, 86, 25, 29, 49, 55, 24, 32, 87, 85, 24, 29, 35, 59, 55, 13, 32, 25, 94, 77, 69, 73, 59, 40, 2, 62, 51, 71, 36, 45, 21, 23, 34, 36, 68, 97, 4, 18, 22, 8, 2, 58]

arr = list(zip(x, y, z))

# import pandas

# csv = pandas.read_csv('minute_weather.csv', low_memory=False)
# # print(csv['air_pressure'], csv['air_temp'], csv['avg_wind_direction'], csv['max_wind_direction'], csv['min_wind_direction'], csv['min_wind_speed'], csv['relative_humidity'])
# arr = list(zip(csv['air_pressure'], csv['air_temp'], csv['avg_wind_direction'], csv['max_wind_direction'], csv['min_wind_direction'], csv['min_wind_speed'], csv['relative_humidity']))

obj = K_mean(arr, 4)

obj.getClusters()
obj.plot()

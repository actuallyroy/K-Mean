from random import random
import matplotlib.pyplot as plt
import time
s = time.time()
import math



class K_mean:
  initCentroids = []
  n_clusters = 0
  data = []
  dimension = 0
  clusters = []
  centroidsProvided = False
  def __init__(self, data, k = 4, centroids = []):
    self.dimension = len(data[0])
    self.n_clusters = k
    self.data = data

    if(centroids):
      self.initCentroids = centroids
      self.n_clusters = len(centroids)
      self.centroidsProvided = True
    else:
      self.initCentroids = self.getInitCentroids(k)

  def getInitCentroids(self, k):
    self.initCentroids = []
    for i in range(k):
        randCent = arr[int(random()*len(arr))]
        if(not randCent in self.initCentroids):
          self.initCentroids.append(randCent)
        else:
          randCent = arr[int(random()*len(arr))]
          self.initCentroids.append(randCent)
    return self.initCentroids

  def calcCentroids(self, clusters):
    centroids = []
    for i in clusters:
      arr = [0] * self.dimension
      l = len(i)
      if(l > 0):
        for j in i:
          for k, v in enumerate(j):
            arr[k] += v
        centroids.append(tuple(round(m/l, 2) for m in arr))
      else:
        centroids.append(arr)
    return centroids
  
  def calcCentroid(self, cluster):
    if(len(cluster) > 0):
      arr = [0] * self.dimension
      l = len(cluster)
      for j in cluster:
        for k, v in enumerate(j):
          arr[k] += v
      return tuple(round(m/l, 2) for m in arr)

  def calcInertia(self, cluster = []):
    if(not cluster):
      cluster = self.clusters
    inertia = 0
    for i in cluster:
      for j in i:
        inertia += self.distance(j, self.calcCentroid(i))**2
    return inertia

  def distance(self, p1, p2):
    arr = [(p1[i] - p2[i])**2 for i in range(len(p1))]
    return math.sqrt(sum(arr))

  def manhattanDistance(self, p1, p2):
    arr = [abs(p1[i] - p2[i]) for i in range(len(p1))]
    return sum(arr)

  def cluster(self, data, centroids):
    arrClus = [[] for i in range(self.n_clusters)]
    for i in data:
      arrD = [] 
      for j in centroids:
        arrD.append(self.manhattanDistance(i, j))
      i_min = arrD.index(min(arrD))
      arrClus[i_min].append(i)
    return arrClus
  
  def getClusters(self, k = 0):
    if(k == 0):
      k = self.n_clusters
    else:
      self.n_clusters = k
    bestCentroids = []
    max = math.inf

    for i in range(100):
      centroids = self.getInitCentroids(k)
      clus = self.K_MeanCluster([[]], centroids)
      p = self.calcInertia(clus)
      if(max > p):
        max = p
        bestCentroids = centroids

    return self.K_MeanCluster([[]], bestCentroids)

  def K_MeanCluster(self, arrClus, centroids):
    arrClus1 = self.cluster(self.data, centroids)
    if(arrClus == arrClus1):
      self.clusters = arrClus
      return arrClus
    else:
      centroids = self.calcCentroids(arrClus1)
      return(self.K_MeanCluster(arrClus1, centroids))

  def plot(self):
    if(not self.clusters):
      self.getClusters()
    if(self.dimension > 2):
      ax = plt.axes(projection ='3d')

    for i in self.clusters:
      if(self.dimension == 1):
        plt.scatter([x[0] for x in i], [0 for x in i])
      elif(self.dimension == 2):
        plt.scatter([x[0] for x in i], [x[1] for x in i])
      else:
        ax.scatter([x[0] for x in i], [x[1] for x in i], [x[2] for x in i])
    plt.show()
  


x = [14, 48, 83, 74, 54, 37, 7, 11, 34, 56, 15, 46, 77, 37, 34, 42, 53, 99, 5, 18, 94, 8, 51, 96, 97, 72, 69, 58, 30, 62, 82, 4, 27, 64, 19, 21, 81, 18, 40, 80, 90, 77, 85, 18, 5, 25, 99, 86, 90, 46]
y = [64, 59, 10, 34, 89, 89, 97, 39, 77, 23, 3, 69, 90, 91, 55, 14, 59, 32, 53, 20, 98, 13, 98, 99, 44, 82, 46, 47, 32, 22, 83, 66, 21, 28, 24, 36, 73, 61, 46, 34, 46, 38, 42, 96, 100, 0, 29, 52, 83, 70]
z = [62, 13, 2, 19, 90, 69, 61, 36, 64, 86, 25, 29, 49, 55, 24, 32, 87, 85, 24, 29, 35, 59, 55, 13, 32, 25, 94, 77, 69, 73, 59, 40, 2, 62, 51, 71, 36, 45, 21, 23, 34, 36, 68, 97, 4, 18, 22, 8, 2, 58]

arr = list(zip(x, y, z, x))

# import pandas

# csv = pandas.read_csv('minute_weather.csv', low_memory=False)
# # print(csv['air_pressure'], csv['air_temp'], csv['avg_wind_direction'], csv['max_wind_direction'], csv['min_wind_direction'], csv['min_wind_speed'], csv['relative_humidity'])
# arr = list(zip(csv['air_pressure'], csv['air_temp'], csv['avg_wind_direction'], csv['max_wind_direction'], csv['min_wind_direction'], csv['min_wind_speed'], csv['relative_humidity']))

obj = K_mean(arr, 4)

obj.getClusters()
print(time.time() - s)
obj.plot()


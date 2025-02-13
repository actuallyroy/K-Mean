import matplotlib.pyplot as plt
import math
from random import random



class K_mean:
  initCentroids = []
  n_clusters = 0
  data = []
  dimension = 0
  clusters = []
  centroidsProvided = False
  def __init__(self, data, k = 4, centroids = [], significantPortion = None):
    self.dimension = len(data[0])
    self.n_clusters = k
    self.data = data
    self.significantPortion = significantPortion

    if(centroids):
      self.initCentroids = centroids
      self.n_clusters = len(centroids)
      self.centroidsProvided = True
    else:
      self.initCentroids = self.getInitCentroids(k)

  def getInitCentroids(self, k):
    self.initCentroids = []
    for _ in range(k):
        randCent = self.data[int(random()*len(self.data))]
        if(not randCent in self.initCentroids):
          self.initCentroids.append(randCent)
        else:
          randCent = self.data[int(random()*len(self.data))]
          self.initCentroids.append(randCent)
    return self.initCentroids

  def calcCentroids(self, clusters):
    centroids = []
    for i in clusters:
      arr = [0] * self.dimension
      l = len(i)
      if(l > 0):
        if(self.significantPortion):
          if(len(self.significantPortion) > 1):
            arr = [0] * (self.significantPortion[1] - self.significantPortion[0])
            for j in i:
              for k, v in enumerate(j[self.significantPortion[0]:self.significantPortion[1]]):
                arr[k] += v
          else:
            arr = [0] * (self.dimension - self.significantPortion[0])
            for j in i:
              for k, v in enumerate(j[self.significantPortion[1]:]):
                arr[k] += v
        else:
          for j in i:
            for k, v in enumerate(j):
              arr[k] += v
        centroids.append(tuple(round(m/l, 2) for m in arr))
      else:
        centroids.append(arr)
    return centroids
  
  def calcCentroid(self, cluster):
    l = len(cluster)
    arr = [0] * self.dimension
    if(l > 0):
      if(self.significantPortion):
        if(len(self.significantPortion) > 1):
          for j in cluster:
            for k, v in enumerate(j[self.significantPortion[0]:self.significantPortion[1]]):
              arr[k] += v
        else:
          for j in cluster:
            for k, v in enumerate(j[self.significantPortion[1]:]):
              arr[k] += v
      return (tuple(round(m/l, 2) for m in arr))
    return arr

  def calcInertia(self, cluster = [], minInertia = math.inf):
    if(not cluster):
      cluster = self.clusters
    inertia = 0
    for i in cluster:
      i_centroid = self.calcCentroid(i)
      for j in i:
        inertia += self.manhattanDistance(j, i_centroid)
        if(inertia > minInertia):
          return inertia
    return inertia

  def distance(self, p1, p2):
    arr = [(p1[i] - p2[i])**2 for i in range(len(p1))]
    return math.sqrt(sum(arr))

  def manhattanDistance(self, p1, p2):
    if(self.significantPortion):
      if(len(self.significantPortion) > 1):
        arr = [abs(p1[i] - p2[i]) for i in range(self.significantPortion[0], self.significantPortion[1])]
      else:
        arr = [abs(p1[i] - p2[i]) for i in range(self.significantPortion[0])]
    else:
      arr = [abs(p1[i] - p2[i]) for i in range(len(p1))]
    return sum(arr)

  def cluster(self, data, centroids):
    arrClus = [[] for _ in range(self.n_clusters)]
    for dataPoint in data:
      i_min = 0
      minVal = math.inf
      for i, centroid in enumerate(centroids):
        d = self.manhattanDistance(dataPoint, centroid)
        if d < minVal:
          minVal = d
          i_min = i
      arrClus[i_min].append(dataPoint)
    return arrClus
  
  def getClusters(self, k = 0):
    if(k == 0):
      k = self.n_clusters
    else:
      self.n_clusters = k
    bestCentroids = []
    max = math.inf

    for _ in range(1, 20):
      print(_)
      centroids = self.getInitCentroids(k)
      clus = self.K_MeanCluster([[]], centroids)
      p = self.calcInertia(clus, max)
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
  

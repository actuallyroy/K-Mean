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
  

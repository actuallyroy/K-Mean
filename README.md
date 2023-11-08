# K-Means Clustering Algorithm

This repository contains an implementation of the K-Means clustering algorithm in Python, which is a popular unsupervised machine learning technique used for partitioning data into groups or clusters. This implementation provides a class, `K_mean`, that allows you to perform K-Means clustering on a given dataset.

## Usage

To use this K-Means clustering implementation, follow these steps:

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/your-username/k-means-clustering.git
   cd k-means-clustering
   ```

2. **Import the `K_mean` Class:**

   Import the `K_mean` class in your Python script:

   ```python
   from k_means_clustering import K_mean
   ```

3. **Prepare Your Data:**

   Create or load your dataset and make sure it is in the appropriate format. You can use the provided example data or prepare your own data.

   Example data format:
   
   ```python
   x = [14, 48, 83, ...]  # List of data points for the first dimension
   y = [64, 59, 10, ...]  # List of data points for the second dimension
   z = [62, 13, 2, ...]   # List of data points for the third dimension
   data = list(zip(x, y, z, x))  # Combine the dimensions into a list of tuples
   ```

4. **Create a K-Means Object:**

   Create a `K_mean` object by providing your data and the number of clusters (k) you want to create. Optionally, you can provide initial centroids:

   ```python
   obj = K_mean(data, k=4, centroids=[])  # Initialize with your data, k value, and optional initial centroids
   ```

5. **Perform Clustering:**

   You can perform clustering by calling the `getClusters` method:

   ```python
   obj.getClusters()  # Perform K-Means clustering
   ```

6. **Visualize the Clusters:**

   You can visualize the clustered data using the `plot` method, which provides a 2D or 3D scatter plot of the clusters:

   ```python
   obj.plot()  # Visualize the clustered data
   ```

7. **Customization and Analysis:**

   Feel free to customize the K-Means implementation or analyze the results, such as calculating cluster centroids, cluster inertia, or other metrics.

## Example

An example of using the K-Means clustering implementation is provided in the script `example.py`. You can run this script to see how the K-Means algorithm works with sample data.

## Dependencies

This implementation relies on the following Python libraries:

- `random`: For generating random numbers.
- `matplotlib`: For data visualization.
- `math`: For mathematical calculations.

## Author

- [actuallyroy](https://github.com/actuallyroy)

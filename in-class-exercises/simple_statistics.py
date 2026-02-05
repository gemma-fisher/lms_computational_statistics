# This is some human readable content
print("Simple summary stats")
 
 # Import libraries
import numpy as np
import seaborn as sns

 # Check all was imported fine
print("All libraries imported successfully")

# Set random seed for reproducibility 
np.random.seed(123)

# Simulate 10 obs centered at 5 with std 2 from a Guassuian distribution
data = np.random.normal(size = 10, loc = 5, scale = 2)
print("\nRandom data:\n",data)

# Compute mean value manually
mean_manual = sum(data) / (len(data))

# Compute the mean
mean_np = np.mean(data)

# Check implementation 
print("Mean (manual): ",mean_manual)
print("Mean (numpy): ",mean_manual)

# Compute variance

# Compute median

# Compute std

# Plot data as histogram, box plot and violin plot



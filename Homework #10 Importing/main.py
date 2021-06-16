import statistics as st

# To find the sample arithmetic mean of data which can be a sequence or iterable.
mean = st.mean([1, 2, 3, 4, 4]) 
print("Mean of value",mean)

# To compute the arithmetic mean of floats.
fmean = st.fmean([3.5, 4.0, 5.25])
print("Mean of floating numbers",fmean)

# to find harmonic mean of data, a sequence or iterable of real-valued numbers.
hmean = st.harmonic_mean([2.5, 6, 4.6])
print("harmonic mean of data",hmean)

# To find median (middle value) of numeric data
median = st.median([1, 3, 5, 7])
print("Median of the data is",median)

# To find high median of numeric data.
high_median = st.median_high([1, 3, 5, 7])
print("High median value of the data is",high_median)

# To find high median of numeric data.
low_median = st.median_low([1, 3, 5, 7])
print("Low median value of the data is",low_median)

# To find single most common data point from discrete or nominal data.
mode = st.mode([1, 1, 2, 3, 3, 3, 3, 4])
print("Mode of the data is",mode)
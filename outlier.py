import numpy as np
import matplotlib.pyplot as plt
incomes = np.random.normal(27000, 15000, 10000)
# incomes = np.append(incomes, [1000000000])
incomes = np.append(incomes, [1000000])

print("\n ... Median based Ourlier Detection and rejection ..........\n")


plt.subplot(2, 1, 1)
plt.hist(incomes, 50)
plt.title('Plot of Data with Outlier')
plt.subplots_adjust(hspace=1)

print("Mean of Income", incomes.mean())
def reject_outliers(data):
    med1 = np.median(data)
    std1 = np.std(data)
    filtered = [el for el in data if (med1 - 2 * std1 < el < med1 + 2 * std1)]
    return filtered

filtered = reject_outliers(incomes)
plt.subplot(2, 1, 2)
plt.hist(filtered, 50)
plt.title('Plot of Data after Outlier Rejection')

plt.show()
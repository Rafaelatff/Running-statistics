import numpy as np  # To use array of numbers instead of list
import matplotlib.pyplot as plt # To plot graphics
import random # To generate random numbers
from statistics import mean # To use mean from statistics package
import math # To use log and pi methods.
from scipy.stats import norm # To show gaussian curve # pip3 install scipy   

## Generating and plotting random values with uniform distribution

values = np.random.randint(-10,10,1000) # Lower limit, Upper limit, number of values

# X = (-2logR1)^1/2 * cos(2piR2)

R1 = [random.random() for _ in range(1000)] # generate 1000 random values to list R1
R2 = [random.random() for _ in range(1000)] # generate 1000 random values to list R2
# It returns <class 'list'>

R1 = np.array(R1) # Converts <list> into <numpy.ndarray>
R2 = np.array(R2)
# It returns <class 'numpy.ndarray'>

# Calculate logarithm for each element in the array
log_R1 = [math.log(x) for x in R1]

log_R1 = np.array(log_R1)
log_R1 = log_R1 * -2 # To multiply, must be np.array instead of list
sqrtM2log_R1 = np.sqrt(log_R1) # Then I do the square root of the value (same as ^1/2)
# It returns <numpy.ndarray>

cos2piR2 = 2 * math.pi * R2
cos2piR2 = np.cos(cos2piR2)

X = sqrtM2log_R1 * cos2piR2
print(type(X))

plt.subplot(4,2,1) 
plt.plot(X) # Prepare the plot to show the randon values
plt.xlabel('Time domain') 
plt.ylabel('Amplitude') 
plt.title('X')#'Random values, normal distribution')

plt.subplot(4,2,2)
plt.hist(X, bins=20)

print('Mean: ' + str(np.float64(np.mean(X)))) # It returns a <numpy.float64> type, then is converted to string
print('Standard deviation: ' + str(np.float64(np.std(X)))) # Same as before


x = np.linspace(np.mean(X) - 4 * np.std(X), np.mean(X) + 4 * np.std(X), 100)  # Valores de x para a distribuição gaussiana
y = norm.pdf(x, np.mean(X), np.std(X))

plt.subplot(4,2,2)
plt.twinx() # To plot over the histogram, but with different scale for Y
plt.plot(x, y, color='red', linewidth=2)

# I have the random values with a normal distribution in the first plot
# Second plot is the histogram and its gaussian

# Now lets plot, in the third graphic, the standard deviation considering
# a running statiscs

# To enter with the window size
window_size = input('Enter window size (2 to 100 [1/10 of the total]) = ')
# It returns <class 'str'>
window_size_N = int(window_size) # To convert str to int
print(type(window_size_N))

if window_size_N <= 1:
    print('Window size cannont be lesser than 2')
elif window_size_N > 101: #elif = else if
    print('Window size cannont be greater than 101')
else:
    print('Running statistcs considering window size of: ', window_size_N)

    # Now lets import the IZ data, for now Rota4_42.txt
    # 3 Column, being packet number, RSSI Downlink, RSSI Uplink
    file = open("Rota4_42.txt", mode='r')
    print(file.read())

    RSSIdl = np.loadtxt("Rota4_42.txt", delimiter=';', usecols=[1])
    print(RSSIdl)     
    file.close()

    val_run = 0
    std_deviation_running = np.array(0)
    print(type(std_deviation_running))
    # Shows how many dimention the array has, not elements
    # print(std_deviation_running.ndim) 
    #std_deviation_running = np.append(std_deviation_running, 10)
    
    print(std_deviation_running)
    for val in RSSIdl:
        # val returns <class 'numpy.float64'>
        # To run over all the random values by incrementing 1
        val_run = val_run+1 
        # array_partial = initial value up to window size
        # then do it again, but initial value + 1 up to window size + 1
        array_partial = RSSIdl[val_run:window_size_N+val_run]
        # now, I need to add to an array, each value of std deviation
        #print(np.std(array_partial))
        std_deviation_running = np.append(std_deviation_running, np.std(array_partial))
        #print('Standard deviation: ' + str(np.float64(np.std(array_partial))))
        #print(array_partial)

    print(std_deviation_running)
    #plt.subplot(4,2,3)
    plt.figure(2)
    plt.plot(std_deviation_running) # Prepare the plot to show the randon values
    plt.xlabel('Time domain') 
    plt.ylabel('Standard deviation') 
    plt.title('Running statistics')#'Random values, normal distribution')

plt.show()

# X Mean: 0.003880677981061158
# X Standard deviation: 1.017240401517945





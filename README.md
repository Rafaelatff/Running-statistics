# Running-statistics
Repository to keep record of the running statistics studies for my master degree.

## Theory

This content is based on The Scientist and Engineer's Guide to Digital Signal Processing, By Steven W. Smith, Ph.D. The chapter is available [here](https://www.dspguide.com/ch2.htm). 

### Mean and Standard Deviation

In some situations, the mean describes what is being measured, while the standard deviation represents noise and other interference.

* μ = mean = average value of a signal = (x0 + x1 + x2 + ... + xN-1)/N
* N = total number of samples (samples go from 0 to N-1)

![image](https://github.com/Rafaelatff/Running-statistics/assets/58916022/f185929a-c633-4432-a029-30c0d3e8eb59)

* σ^2 = variance
* σ = standard deviation = how far the signal fluctuates from the mean = √[((x0-μ)^2 + (x1-μ)^2 + ... + (xN-1-μ)^2)/(N-1)]

![image](https://github.com/Rafaelatff/Running-statistics/assets/58916022/c7f11452-ef56-4048-8cb9-78ffcbf81faa)

### Histogram

The histogram displays the number of samples there are in the signal that have each of these possible values. The histogram can be used to efficiently calculate the mean (EQUATION 2-6) and standard deviation (EQUATION 2-7) of very large data sets. The strategy of those equation is to use these slow operations only on the few numbers in the histogram, not the many samples in the signal. If I use those calcs here during the studies I will print the equations from the book.

### Probability Mass Function and Probability Density Function

The histogram is what is formed from an acquired signal. The corresponding curve for the underlying process is called the probability mass function (pmf). A histogram is always calculated using a finite number of samples, while:

* pmf = what would be obtained with an infinite number of samples
* pmf describes the probability that a certain value will be generated

The **histogram and pmf can only be used with discrete data**, such as a digitized signal residing in a computer. A similar concept applies to continuous signals, such as voltages appearing in analog electronics. For continuous signals we have:

* pdf = probability density function, also called the probability distribution function
* pdf is represented by a continous line (while pmf isn't)
* total area under the curve is equal to one
* the integral of the pdf is used to find the probability thata signal will be within a certain range of values

![image](https://github.com/Rafaelatff/Running-statistics/assets/58916022/0dbfd8d7-9900-44ba-afb5-3d02295da5dc)

### The Normal Distribution

Signals formed from random processes usually have a bell shaped pdf. This is called a normal distribution, a Gauss distribution, or a Gaussian, after the great German mathematician, Karl Friedrich Gauss (1777-1855).

The basic shape of the curve is generated from a negative squared exponent: y(x) = e^(-x^2).

![image](https://github.com/Rafaelatff/Running-statistics/assets/58916022/902e3eba-f920-47bf-874c-35e4f15ac118)

* The mean centers the curve over a particular value
* The standard deviation controls the width of the bell shape

### Digital Noise Generation

The heart of digital noise generation is the random number generator. Each random number has a value between zero and one, with an equal probability of being anywhere between these two extremes.
The mean of the underlying process that generated this signal is 0.5, the standard deviation is 1/√12 (0.29), and the distribution is uniform between zero and one.

Algorithms need to be tested using the same kind of data they will encounter in actual operation. This creates the need to generate digital noise with a Gaussian pdf.

The **Central Limit Theorem** states that a sum of random numbers becomes normally distributed as more and more of the random numbers are added together.
The Central Limit Theorem provides the reason why normally distributed signals are seen so widely in nature. Whenever many different random forces are interacting, the resulting pdf becomes a Gaussian.

### Earlier studies

Some studies about mean, standard deviation, histogram were already performed during the [intermediate module of python DataCamp](https://github.com/Rafaelatff/DataCamp-Intermediate-Python).
The code presented in the repositorie above, shows the histogram for values with **mean (μ) near to 0** and **standard deviation (σ) of 1**. The code in this repositories shows how to generate digital noise with a Gaussian pdf by using the random number generator (that has its distribution uniform between zero and one), by using the EQUATION 2.9.

![image](https://github.com/Rafaelatff/Running-statistics/assets/58916022/a801dcd7-d314-451b-a987-bd421dfc8c1b)

My results:

![image](https://github.com/Rafaelatff/Running-statistics/assets/58916022/7ff04881-22f6-4eae-8a6f-832276acbabd)
![image](https://github.com/Rafaelatff/Running-statistics/assets/58916022/d8017e7f-c0b3-4e7c-9e08-466db3f12e6f)

I can also see more about how to import data on python [here](https://github.com/Rafaelatff/DataCamp-Importing-Data-in-Python).

Now that I know how to generate digital noise with a Gaussian pdf and also how to import data on python, I can start by putting the running statics to work. Later, on a new repositorie, I can try to generate the histogram by using data generated by the PK2, then performing running statics over the PK2, everithing considering its functionalities with the TpM.

# Running statiscs

It is often desirable to recalculate the mean and standard deviation as new samples are acquired and added to the signal. We will call this type of calculation: running statistics.
Once in my article for SBrT we use similar equations as in 2.1 and 2.2, later I will compare results with EQUATIOn 2.3. 

![image](https://github.com/Rafaelatff/Running-statistics/assets/58916022/4e6c1599-7c5f-49ec-8ebf-45a9e331340a)

I decided to leave the user to choose the window size for the running statistics by:

```py
# To enter with the window size
window_size = input('Enter window size (2 to 100 [1/10 of the total]) = ')
# It returns <class 'str'>
window_size_N = int(window_size) # To convert str to int
print(type(window_size_N))
```

Then I do the math by:

```py
if window_size_N <= 1:
    print('Window size cannont be lesser than 2')
elif window_size_N > 101: #elif = else if
    print('Window size cannont be greater than 101')
else:
    print('Running statistcs considering window size of: ', window_size_N) 
    # X is a <class 'numpy.ndarray'>
    val_run = 0
    std_deviation_running = np.array(0)
    print(type(std_deviation_running))
    # Shows how many dimention the array has, not elements
    # print(std_deviation_running.ndim) 
    #std_deviation_running = np.append(std_deviation_running, 10)
    
    print(std_deviation_running)
    for val in X:
        with np.errstate(divide='ignore', invalid='ignore'):
            # val returns <class 'numpy.float64'>
            # To run over all the random values by incrementing 1
            val_run = val_run+1 
            # array_partial = initial value up to window size
            # then do it again, but initial value + 1 up to window size + 1
            array_partial = X[val_run:window_size_N+val_run]
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
```
Now lets compare a window size of 5:

![image](https://github.com/Rafaelatff/Running-statistics/assets/58916022/d2e1f6f0-3342-4cab-849f-e23452bb0ebf)

With a window size of 50:

![image](https://github.com/Rafaelatff/Running-statistics/assets/58916022/b49ffbd3-714c-49db-8e03-6903813483f5)

Before we go to the book, let's check the IZ data collected for several projects/studies and check if the running statistics is running according to the desired. We will run a test with the data in Rota4_42.txt.

The code that collects the data from Rota4_42.txt is presented (and also added to code running-statistics-IZ.py):

```py
else:
    print('Running statistcs considering window size of: ', window_size_N)

    # Now lets import the IZ data, for now Rota4_42.txt
    # 3 Column, being packet number, RSSI Downlink, RSSI Uplink
    file = open("Rota4_42.txt", mode='r')
    print(file.read())

    RSSIdl = np.loadtxt("Rota4_42.txt", delimiter=';', usecols=[1])
    print(RSSIdl)     
    file.close()
```

Then we did a few changes on the running statistic part of the code:

```py
    print(std_deviation_running)
    for val in RSSIdl:
        val_run = val_run+1 
        array_partial = RSSIdl[val_run:window_size_N+val_run]
        #print(np.std(array_partial))
        std_deviation_running = np.append(std_deviation_running, np.std(array_partial))
```
And then we plot the data. Now, considering also a window size of 8, let`s compare the data:

![image](https://github.com/Rafaelatff/Running-statistics/assets/58916022/806c9723-3604-4feb-a1bf-e8ce194c0ffa)

It looks that the code works fine! Now let's go to the book part:

The book sugests to use the following calc:
We don't need that all of the samples be involved in each new calculation, so we will use EQUATION 2.3.

![image](https://github.com/Rafaelatff/Running-statistics/assets/58916022/fb1f644b-cc65-497a-bb73-79d79baa3967)



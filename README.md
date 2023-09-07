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

![image](https://github.com/Rafaelatff/Running-statistics/assets/58916022/06a834cd-fea3-45bc-a8c5-e68a1a62b6b8)

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


![image](https://github.com/Rafaelatff/Running-statistics/assets/58916022/fb1f644b-cc65-497a-bb73-79d79baa3967)

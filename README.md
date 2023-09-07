# Running-statistics
Repository to keep record of the running statistics studies for my master degree.

## Theory

This content is based on The Scientist and Engineer's Guide to Digital Signal Processing, By Steven W. Smith, Ph.D. The chapter is available [here](https://www.dspguide.com/ch2.htm). 

## Earlier studies

Some studies about mean, standard deviation, histogram were already performed during the [intermediate module of python DataCamp](https://github.com/Rafaelatff/DataCamp-Intermediate-Python).
The code presented in the repositorie above, shows the histogram for values with **mean (μ) near to 0** and **standard deviation (σ) of 1**. 

The histogram displays the number of samples there are in the signal that have each of these possible values. The histogram can be used to efficiently calculate the mean (EQUATION 2-6) and standard deviation (EQUATION 2-7) of very large data sets. The strategy of those equation is to use these slow operations only on the few numbers in the histogram, not the many samples in the signal. If I use those calcs here during the studies I will print the equations from the book.

The histogram is what is formed from an acquired signal. The corresponding curve for the underlying process is called the probability mass function (pmf). A histogram is always calculated using a finite number of samples, while:

* pmf = what would be obtained with an infinite number of samples
* pmf describes the probability that a certain value will be generated

The **histogram and pmf can only be used with discrete data**, such as a digitized signal residing in a computer. A similar concept applies to continuous signals, such as voltages appearing in analog electronics. For continuous signals we have:

* pdf = probability density function, also called the probability distribution function
* pdf is represented by a continous line (while pmf isn't)

![image](https://github.com/Rafaelatff/Running-statistics/assets/58916022/0dbfd8d7-9900-44ba-afb5-3d02295da5dc)

### The Normal Distribution

Signals formed from random processes usually have a bell shaped pdf. This is called a normal distribution, a Gauss distribution, or a Gaussian, after the great German mathematician, Karl Friedrich Gauss (1777-1855).

I can also see more about how to import data on python [here](https://github.com/Rafaelatff/DataCamp-Importing-Data-in-Python).

### Mean and Standard Deviation

In some situations, the mean describes what is being measured, while the standard deviation represents noise and other interference.

* μ = mean = average value of a signal = (x0 + x1 + x2 + ... + xN-1)/N
* N = total number of samples (samples go from 0 to N-1)

![image](https://github.com/Rafaelatff/Running-statistics/assets/58916022/f185929a-c633-4432-a029-30c0d3e8eb59)

* σ^2 = variance
* σ = standard deviation = how far the signal fluctuates from the mean = √[((x0-μ)^2 + (x1-μ)^2 + ... + (xN-1-μ)^2)/(N-1)]

![image](https://github.com/Rafaelatff/Running-statistics/assets/58916022/06a834cd-fea3-45bc-a8c5-e68a1a62b6b8)

### Running statiscs



![image](https://github.com/Rafaelatff/Running-statistics/assets/58916022/fb1f644b-cc65-497a-bb73-79d79baa3967)

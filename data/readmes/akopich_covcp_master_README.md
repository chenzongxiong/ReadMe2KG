# covcp
The package implements the approaches to change-point detection in covariance presented in papers 

[Avanesov, Buzun. *Change-point detection in high-dimensional covariance structure.* Electron. J. Statist. 12 (2) 3254 - 3294, 2018](https://doi.org/10.1214/18-EJS1484)

[Avanesov. *Structural break analysis in high-dimensional covariance structure.* 2018](https://arxiv.org/abs/1803.00508)

# Installation
The package can be installed via `install_github("akopich/covcp")`. `install_github` is provided by `devtools`.

# Example
First, let's sample some data and run the test from (Avanesov 2018).
```R
library(covcp) 
library(MASS) # needed for sampling from multivariate normal


library(parallel)
library(doMC)
registerDoMC(cores = 20) # set the multithreaded environment up

set.seed(42)

# Sample some data with and without a change-point
p = 50        # dimensionality  
N = 1000      # number of data points before the CP
cov0 = diag(p)# the covariance matrix before the CP

# We construct the covariance matrix after the CP,
# first constructing its inverse as a tridiagonal matrix
invCov1 = diag(p)
invCov1[row(invCov1) - col(invCov1) == 1] = 0.4
invCov1[row(invCov1) - col(invCov1) == -1] = 0.4
cov1 = solve(invCov1)


left = mvrnorm(N, rep(0, ncol(cov0)), cov0)       # now, we sample the data before...
right = mvrnorm(N, rep(0, ncol(cov1)), cov1)      # and after the CP
withCP = rbind(left, right)                       # and bind them together
noCP = mvrnorm(1.5 * N, rep(0, ncol(cov0)), cov0) # Also we sample a dataset without a CP

windows = c(20, 30, 50) # that's clear
alpha = 0.05            # nominal significance level

# The indices of the data-points that shall be used for the bootstrap. 
stableSet = 1:300 # One can set it more or less arbitrarily, but if the portion
# of the data it specifies includes the CP, the power of the test might be impeded

# finally, we are ready to run the test from (Avanesov 2018)
testResultNoCP = covTest(windows, 
                           alpha, 
                           noCP,      # here goes the data
                           noPattern, # undocumented. just keep it like that
                           infNorm,   # here we choose a matrix norm. The paper deals with l_inf
                           stableSet)

isRejected(testResultNoCP) # returns FALSE, as expected
plot.CPDResult(testResultNoCP) # also, you can plot the statistics


# Here we do the same for a dataset that actually has a CP.
testResultWithCP = covTest(windows, 
                           alpha, 
                           withCP, 
                           noPattern, 
                           infNorm, 
                           stableSet)

isRejected(testResultWithCP) # returns TRUE, unsurprisingly
plot.CPDResult(testResultWithCP)

```

Running the test from (Avanesov&Buzun 2018) takes a little more effort. 

NOTE, the methodology makes sense only if the inverse-covariance 
matrices it deals with are sparse. Yes, this is the reason why we've constructed `cov1` the way we did. 

```R
library(glasso) # we'll need that for graphical lasso implementation. 
set.seed(42)

chooseRho = function(data) sqrt(log(ncol(data)) / nrow(data)) # the graphical lasso relies on a careful choice of its penalization parameter 
myCov = function(x) t(x) %*% x / nrow(x) # no need to center, as we sampled from centered distributions
# here we just write a helper function, taking a dataset and returning a glasso estimate
GL = function(data) glasso(myCov(data), chooseRho(data), penalize.diagonal = F)$wi 

windows = c(150,220,300) 

testResultNoCP = createPrecisionMatrixTest(windows,  
                                           alpha, 
                                           noCP, 
                                           noPattern, 
                                           GL, 
                                           infNorm,
                                           stableSet,
                                           hatTheta2GaussianSigmas) # the last parameter may be replaced with cov2ZVar(cov0) if you deem the cov0 known.  

plot.CPDResult(testResultNoCP)


testResultWithCP = createPrecisionMatrixTest(windows,  
                                             alpha, 
                                             withCP,
                                             noPattern, 
                                             GL, 
                                             infNorm,
                                             stableSet,
                                             hatTheta2GaussianSigmas)
plot.CPDResult(testResultWithCP)

```



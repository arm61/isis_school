# How to leverage our prior knowledge?

In the introduction to model-dependent analysis, it was suggested that constructing a model and therefore biasing the analysis was acceptable, if the model is founded in logic. 
We can take this once step further but designing out model-dependent analysis such that we impose prior expectations about the values of parameters we are looking to probe. 
We achieve this using Bayes theorem {cite}`bayes_essay_1763`, 

$$
p(y|\theta) = \frac{\mathcal{L}(\theta|y) p(\theta)}{p(y)} \propto \mathcal{L}(\theta|y) p(\theta),
$$

where $p(y|\theta)$ is the posterior, $\mathcal{L}(\theta|y)$ is the likleihood we have already seen, $p(\theta)$ is our prior belief, and $p(y)$ is the probability associated with the measured data, which is constant for all $\theta$. 
It is Bayes theorem that enables us to integrate our prior knowledge, as a probability, into our analysis. 
If we can describe our prior understanding about our parameters $\theta$ as probabilities, we can look to maximise the posterior instead of the likelihood. 

## A uniform prior

Lets consider a simple example, where we impose a uniform prior on some of parameters, we have infact already looked at such an example. 
When, in looking at the differential evolution algorithm we imposed maximum and minimum bounds for our parameters, we were infact introducing a prior. 
In this case, the prior stated that if $\theta$ was within those bounds the probability was $1$, but if it were outside, the probability was $0$. 
Therefore, the posterior was $0$ and this could not be the maximum. 

If you would like to find out more about using Bayesian analysis in data analysis the book Data Analysis: A Bayesian tutorial by Dr Devinder Sivia is a great place to start {cite}`sivia_data_2006`. 
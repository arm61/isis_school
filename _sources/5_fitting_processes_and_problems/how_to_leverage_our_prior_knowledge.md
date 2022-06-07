# How to leverage our prior knowledge?

In the introduction to model-dependent analysis, it was suggested that constructing a model and therefore biasing the analysis was acceptable, **if the model is founded in logic**. That is, we have prior knowledge of the system which can be used to constrain the parameter space. For example, if we know that we have a sample on a silicon substrate, we can fix the substrate SLD to the known value.

We can take this one step further but designing out model-dependent analysis such that we impose prior expectations about the values of parameters we are looking to probe. 
We achieve this using Bayes theorem {cite}`bayes_essay_1763`, 

$$
p(y|\theta) = \frac{\mathcal{L}(\theta|y) p(\theta)}{p(y)} \propto \mathcal{L}(\theta|y) p(\theta),
$$

where $p(y|\theta)$ is the posterior, $\mathcal{L}(\theta|y)$ is the likelihood we have already seen, $p(\theta)$ is our prior belief, and $p(y)$ is the probability associated with the measured data, which is constant for all $\theta$. 
It is Bayes theorem that enables us to integrate our prior knowledge, as a probability, into our analysis. 
If we can describe our prior understanding of our parameters $\theta$ as probabilities, we can look to maximise the posterior instead of the likelihood. In the previous example, $p(\theta) = \delta(SLD - SLD_Si)$.

## A uniform prior

Let's consider a simple example, where we impose a uniform prior on some of the parameters, we have in fact already looked at such an example. 
When looking at the differential evolution algorithm we **imposed maximum and minimum bounds** for our parameters, we were introducing a prior. 
In this case, the prior stated that if $\theta$ was within those bounds the probability was $1$, but if it were outside, the probability was $0$. 
Therefore, the posterior was $0$ and this could not be the maximum. 

## Gaussian priors

Suppose we have information from a different technique or previous measurements in other conditions, which give us a relatively strong belief of parameters of the system (e.g. we have measured the thickness of a layer with AFM, giving $t_slab = t \pm \sigma_t$). We can use this to construct a prior for this parameter for fitting, which constrains the search space to speed up optimization.

[INSERT A DIAGRAM COMPARING UNIFORM VS GAUSSIAN PRIOR]

These are just some examples of priors, which allow us to better optimize our figure of merit and find the global best fit. 

[UPDATE THE FLOW DIAGRAM: "Propose a model" becomes "Propose a model with initial guesses and a prior", "Improve the model" becomes "Can we improve the model or our confidence in that model?"]

Optimizers can give anything from only the best fit parameters to the full posterior distribution of parameters. In general, the more information in the output, the longer it takes to converge. In practice, it is useful to start with a rapidly converging optimizer to find good initial guesses, and then feed them into a slower optimizer which can give you error bars on the final fit parameters.

If you would like to find out more about using Bayesian analysis in data analysis the book Data Analysis: A Bayesian Tutorial by Dr Devinder Sivia is a great place to start {cite}`sivia_data_2006`. 

# A case for model reparameterisation

The slab models introduced previously are a useful tool to simulate our reflectometry data. 
However, their parameterisation, in particular the concept of **scattering length density** is rather unintuative compared to how we typically think about our experimental systems. 
Therefore, it may be useful to **reparameterise** our model to translate more commonly used parameters, such as mass density or area-per-molecule, into these scattering length densities. 

```{figure} ../figures/lipid.jpg
---
height: 250px
align: center
name: lipid
---
An example of a model reparameterisation from the work of John *et al.* {cite}`john_large_2021`.
```

In addition to making our model more understandable and allowing description of our system in a language that we are more familiar with, this approach can make physical constraints on our system more straightforward to apply. 
For example, we will be able to actively constrain the density of a given material based on literature values or introduce chemical stoichiometry to our model based on the synthesis process. 
In this section, we will work through a pair of examples of reparameterising or slab model in terms of chemical and physical parameters. 
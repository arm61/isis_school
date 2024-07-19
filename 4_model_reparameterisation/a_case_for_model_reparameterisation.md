# A case for model reparameterisation

The slab models introduced previously are a useful tool to simulate our reflectometry data. 
However, their parameterisation, in particular the concept of **scattering length density** is rather unintuitive compared to how we typically think about our experimental systems. 
Therefore, it may be useful to **reparameterise** our model to translate more commonly used parameters, such as mass density or area-per-molecule, into these scattering length densities. 

```{figure} ../figures/lipid.jpg
---
height: 250px
align: center
name: lipid
---
An example of a model reparameterisation from the work of John *et al.* {cite}`john_large_2021`.
```

In addition to making our model more understandable and allowing the description of our system in a language that we are more familiar with, this approach can make physical constraints on our system more straightforward to apply. 
This process is **system-specific**, and requires that assumptions made about the data are true, to should be used with caution. 
Additionally, if measurements from complementary techniques are used to define the reparameterised system, it is important that the previous measurements **accurately describe the parameter** as it is in the neutron reflectometry measurement. 

To give a flavour of the system-specific nature of this process, in this section we will look at **two examples**. 
The first investigates a simple conversion of mass density to scattering length density, while the latter uses information about the chemical structure to reduce the number of free parameters in the fitting process. 

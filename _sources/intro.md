# A Guide to Reflectometry

The aim of these webpages are to give an introduction to neutron and X-ray reflectometry, currently the focus is on the anlaysis of reflectometry data but we how to expand this in future. 
Currently, we focus on the following subjects: 
- the **Fourier transform** and how a Born approximation approach may be used to analyse neutron and X-ray reflectometry data; 
- the logic of **model-dependent analysis**; 
- reflectometry "slab models" and their traditional parameterisation; 
- **reparameterisation** of these models to include chemical and physical insight; and 
- the process and problems associated with **fitting** in a model-dependent analysis procedure. 

## Reflectometry vs reflectivity

This is a question often asked by new users of reflectometry. What is the difference between reflectometry and reflectivity?

- *reflecto[metry](https://www.etymonline.com/word/-metry)*: the technique used to measure reflectivity
- *reflectivity*: the quantity measured by reflecto[metry](https://www.etymonline.com/word/-metry)

You might find both words being used.

## About this material

This material is gradually being developed and if you are interested in contributing content please feel free to open an [issue](https://github.com/reflectivity/learn/issues/new/choose) on the Github repository. 

This material was originally developed by [Andrew McCluskey](mailto:andrew.mccluskey@ess.eu) from the [European Spallation Source](https://europeanspallationsource.se/) and through the ISIS Neutron Reflectometry School and Open Reflectometry Standards Organisation Workshop 2022 has recieved contributions and feedback from many [reflectometry experts](https://github.com/reflectivity/learn/blob/main/contributors.md).

```{note}
In this course, we make use of the Python programming language heavily to show mathematics and plot figures. 
The aim is that the course should **not** require knowledge of Python to understand the content. 
If you are not comfortable with Python, feel free to skip the code blocks, but make sure to **pay attention** to the plots that are produced.
```

## Bibliography

Some particularly useful books and papers for reflectometry analysis, and data analysis in general include:
- Elementary Scattering Theory: For X-ray and Neutron Users by Devinder Sivia {cite}`sivia_elementary_2011`;
- *Current Opinion in Colloid & Interface Science*, **42**, 2019 covers a range of applications in soft and biological matter including {cite}`lakey_recent_2019,skoda_recent_2019,welbourn_new_2019`;
- Some interesting reviews of magnetic reflectometry analysis include {cite}`fitzsimmons_applications_2005,zabel_polarized_2007,toperberg_neutron_2015`; and
- Data Analysis: A Bayesian Tutorial by Devinder Sivia and John Skilling {cite}`sivia_data_2006`.

This list is not exhaustive and we suggest searching for and reading relevant work in your field **once you understand the basics**. 

```{bibliography}
```

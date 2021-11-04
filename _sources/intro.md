# Introduction to neutron reflectometry fitting

The aim of this course, and the companion lecture, are to give an introduction to the following subjects: 
- the **Fourier transform** and how a Born approximation approach may be used to analyse neutron reflectometry data; 
- the logic of **model-dependent analysis**; 
- neutron reflectometry "slab models" and their traditional parameterisation; 
- **reparameterisation** of these models to include chemical and physical insight; and 
- the process and problems associated with **fitting** in a model-dependent analysis procedure. 

It is **assumed** that this reader has been introduced to the technique of neutron reflectometry, such as what this technique can be used to study and the data collection methodology.

The integration with JupyterHub is powered by the [PaNOSC project](https://www.panosc.eu). 

This course was originally developed by [Andrew McCluskey](mailto:andrew.mccluskey@ess.eu) from the [European Spallation Source](https://europeanspallationsource.se/) for the [ISIS Virtual Reflectometry Training Course](https://indico.stfc.ac.uk/event/355/). 
If you have any questions about this course, please get in touch.

```{note}
In this course, we make use of the Python programming language heavily to show mathematics and plot figures. 
The aim is that the course should not require knowledge of Python to understand the content.
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
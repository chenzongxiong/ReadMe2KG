# fisher-information
## About the Project
**For the most up-to-date work using this framework, and if you are interested in applying the framework to experimental design problems of your own, see the [experimental-design](https://github.com/James-Durant/experimental-design) repository**.

This repository contains the [code](/fisher-information), [data](/fisher-information/data) and [results](/fisher-information/results) for a framework for determining the maximum information gain and optimising experimental design in neutron reflectometry experiments using the Fisher information (FI).

In neutron reflectometry experiments, the FI can be analytically calculated and used to provide sub-second predictions of parameter uncertainties. These uncertainties can influence real-time decisions about measurement angle, measurement time, contrast choice and other experimental conditions based on parameters of interest. The FI provides a lower bound on parameter estimation uncertainties and these are shown to decrease with the square root of measurement time, providing useful information for the planning and scheduling of experimental work. As the FI is computationally inexpensive to calculate, it can be computed repeatedly during the course of an experiment, saving costly beam time by signalling that sufficient data has been obtained; or saving experimental datasets by signalling that an experiment needs to continue.

### Citation
Please cite the following article if you intend on including elements of this work in your own publications:
> Durant, J. H., Wilkins, L., Butler, K. and Cooper, J. F. K. Determining the maximum information gain and optimizing experimental design in neutron reflectometry using the Fisher information. _J. Appl. Cryst_. **54**, 1100-1110 (2021).

Or with BibTeX as:
```
@article{Durant2021,
   author    = {Durant, J. H. and Wilkins, L. and Butler, K. and Cooper, J. F. K.},
   doi       = {10.1107/S160057672100563X},
   journal   = {Journal of Applied Crystallography},
   month     = {Aug},
   number    = {4},
   pages     = {1100--1110},
   publisher = {International Union of Crystallography ({IUCr})},
   title     = {{Determining the maximum information gain and optimizing experimental design in neutron reflectometry using the Fisher information}},
   url       = {https://doi.org/10.1107/S160057672100563X},
   volume    = {54},
   year      = {2021}
}
```

For the figures presented in this article, see [figures](/figures).

## Installation
1. To replicate the development environment with the [Anaconda](https://www.anaconda.com/products/individual) distribution, first create an empty conda environment by running: <br /> ```conda create --name fisher-information python=3.8.3```

2. To activate the environment, run: ```conda activate fisher-information```

3. Install pip by running: ```conda install pip```

4. Run the following to install the required packages from the [requirements.txt](/requirements.txt) file: <br />
   ```pip install -r requirements.txt```

You should now be able to run the code. Please ensure you are running a version of Python >= 3.8.0 \
If you are running an old version of Anaconda, you may need to reinstall with a newer version for this.

## Contact
Jos Cooper - jos.cooper@stfc.ac.uk \
James Durant - james.durant@warwick.ac.uk \
Lucas Wilkins - lucas@lucaswilkins.com

## Acknowledgements
This work has been partially supported by the STFC Facilities Programme Fund through the ISIS Neutron and Muon Source, and Scientific Computing Department of Rutherford Appleton Laboratory, Science and Technology Facilities Council, and by the Wave 1 of The UKRI Strategic Priorities Fund under the EPSRC Grant EP/T001569/1, particularly the "AI for Science" theme within that grant and The Alan Turing Institute. We would also like to thank Luke Clifton for his assistance and expertise in fitting the DMPC data.

## License
Distributed under the GPL-3.0 License. See [license](/LICENSE) for more information.

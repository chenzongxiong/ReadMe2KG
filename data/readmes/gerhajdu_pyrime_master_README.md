# PyRIME: Rectified I-band Metallicity Estimae of rr lyrae variables

This routine calculates the I-band photometric iron abundance of RR Lyrae variables,
based on Equation 3 of [Smolec (2005)](http://adsabs.harvard.edu/abs/2005AcA....55...59S),
but correcting for the amplitude-dependent offset in the Oosterhoff I variables, as 
described by [Hajdu et al. (2018)](https://arxiv.org/abs/1804.01456).

This routine was developed for:
 - `Python` 2.7+ or 3.6+
 - `Numpy` 1.12+

## Installation

Copy all files from the `bin` directory to the same directory in the system PATH.
If you get "ImportError: No module named builtins" error while using Python 2.7,
install the `future` package.

## Usage

The only argument the program expects is the location of a file, containing at least five columns,
where the first five columns should be:
- NAME: the name of the variable
- PERIOD: the period of the variable
- A1: the amplitude of the first Fourier harmonic in the I band
- A2: the amplitude of the second Fourier harmonic in the I band
- phi31: the epoch independent phase difference of the first and third Fourier harmonics in the I-band

Given these data, the routine estimates whether a variable belongs to the Oosterhoff II group, in which
case the original Equation 3 is used to calculate its iron abundance. In case of Oosterhoff I variables,
the amplitude dependence is rectified as described in Hajdu et al. (2018).

Finally, the program outputs the name of the variable, the abundance estimate and whether it is an
Oosterhoff I or II variable.

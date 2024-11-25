# GJ1243-Flares
This is the full catalog of 6107 flare events from 11 months of short cadence Kepler data from [Davenport et al. (2014)](http://arxiv.org/abs/1411.3723) - the largest uniform sample of flares on a single star to date.

A conference proceeding from IAUS 320 ([Davenport 2015](http://arxiv.org/abs/1510.05695)) is  available, which describes additional avenues of research with this unique dataset.

Possible uses for this flare data include:

- Studies of complex flare morphologies and rates
- Comparison of flare rates to solar flare models
- Training set for more advanced flare-detection algorithms


## Catalog Info
The repository contains both the [catalog of flares](data/gj1243_master_flares.tbl) and the corresponding 11-month [light curve](data/gj1243_master_slc.dat). These are the columns saved for every flare in the catalog:

```
# ----- Columns: -----
# index of flare start in "gj1243_master_slc.dat"
# index of flare stop in "gj1243_master_slc.dat"
# t_start
# t_stop
# t_peak
# t_rise
# t_decay
# flux peak (in fractional flux units)
# Equivalent Duration (ED) in units of per seconds
# Equiv. Duration of rise (t_start to t_peak)
# Equiv. Duration of decay (t_peak to t_stop)
# Complex flag (1=classical, 2=complex) by humans
# Number of people that identified flare event exists
# Number of people that analyzed this month
# Number of flare template components fit to event (1=classical >1=complex)
```


## The flare sample
To recreate the flare sample used to generate the median flare template (885 events), try the following in IDL:

    readcol, 'gj1243_master_flares.tbl', fstart, fstop, tstart, tstop, tpeak, $
              trise, tdecay, fpeak, ed, edrise, eddecay, cplx_flg, ppl1, ppl2
    
    dur = tstop - tstart
    remove, where(dur*24.*60. lt 20 or $ ; short flares
                  dur*24.*60. gt 75 or $ ; too long flares
                  cplx_flg gt 1.5 or $   ; complex flares
                  ppl1 lt 4 or $         ; uncertain flares
                  real(ed) le 0 or $     ; bad ED fit 
                  real(ed) gt 100),$     ; too high ED (tend to be cplx)
            dur, tstart, tstop, cplx_flg, ed

    print, '# flares in template generating sample:', n_elements(dur)



### Citation
If you use this dataset, please cite our published paper: [Davenport et al. (2014)](http://arxiv.org/abs/1411.3723)


### See Also

- [FBEYE](https://github.com/jradavenport/FBEYE) - an IDL based flare-finding suite
- [flare-fit](https://github.com/jradavenport/flare-fit) - IDL code to deconstruct complex flare events
- [appaloosa](https://github.com/jradavenport/appaloosa) - a Python-based flare Kepler flare finding project
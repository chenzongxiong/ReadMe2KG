
Geant4 Simulation of OSCAR @ OCL
=========================================================
[![DOI](https://zenodo.org/badge/44380221.svg)](https://zenodo.org/badge/latestdoi/44380221)  
(DOI for the latest release of the `code`. Earlier verions can be cited by a specific "version" DOI, if necessary)

[[Description / How to cite]](#cite) - [[Dowloading notes & usage]](#download) - [[More information]](#more)

This simulation implements OSCAR's LaBr3:Ce Scintillator detectors. The response functions for incident $\gamma$ rays up to 20 MeV are simulated with Geant4. The energy spectra are saved in a root tree. The results stored on zenodo (see below), and the extracted response matries are also available at [oslocyclotronlab/OCL_response_functions](https://github.com/oslocyclotronlab/OCL_response_functions).

<a name="cite"/></a>
# Description / How to cite
The simulations are described in following [article](https://doi.org/10.1016/j.nima.2020.164678):
```
@article{Zeiser2020,
title = "The $\gamma$-ray energy response of the Oslo Scintillator Array OSCAR",
journal = "Nuclear Instruments and Methods in Physics Research Section A: Accelerators, Spectrometers, Detectors and Associated Equipment",
volume = "985",
pages = "164678",
year = "2021",
issn = "0168-9002",
doi = "https://doi.org/10.1016/j.nima.2020.164678",
url = "http://www.sciencedirect.com/science/article/pii/S0168900220310755",
author = "Zeiser, F. and Tveten, G.M. and {Bello Garrote}, F.L. and Guttormsen, M. and Larsen, A.C. and Ingeberg, V.W. and Görgen, A. and Siem, S.",
keywords = "Geant4, Response function, Lanthanum-bromide, Gamma-ray detector array, Monte Carlo Simulation, Detector modeling",
abstract = "The new Oslo Scintillator Array (OSCAR) has been commissioned at the Oslo Cyclotron Laboratory (OCL). It consists of 30 large volume (3.5 x 8 inches) LaBr$_3$(Ce) detectors that are used for $\gamma$-ray spectroscopy. The response functions for incident $\gamma$ rays up to 20 MeV are simulated with Geant4. In addition, the resolution, and the total and full-energy peak efficiencies are extracted. The results are in very good agreement with measurements from calibration sources and experimentally obtained mono-energetic in-beam  $\gamma$-ray spectra."
}
```

- If you use/modify the simulations and or the generated response matrix, please cite the `article` mentioned above, [DOI: 10.1016/j.nima.2020.164678](https://doi.org/10.1016/j.nima.2020.164678). 
- if possible, reference also the DOI of the specific version of the response you use / the files, i.e. `zenodo` reccord via 
[DOI: 10.5281/zenodo.4018494](https://doi.org/10.5281/zenodo.4018494) for `v2.0.0.1`.
- When using `v1.0.3` *or earlier*: Cite the arXive article (v1) [arxiv/2008.06240v1](https://arxiv.org/abs/2008.06240v1) and the correct zenodo version v1.0.3 (10.5281/zenodo.1339347). We appreciate if you also cite the published article, [DOI: 10.1016/j.nima.2020.164678](https://doi.org/10.1016/j.nima.2020.164678), which very briefly discusses the challenges and changes that occurred since v1.0.3. Citing the article will also give us, the programmers, creds.

<a name="download"/></a>

## 0 - Dowloading notes & usage
- We started a [wiki](https://github.com/oslocyclotronlab/OCL_GEANT4/wiki) with a detailed how-to guide on creating your own response matrix.
- Note that the CAD geometry files (see more information below) are stored with [git lfs](https://git-lfs.github.com/). If you don't have git lfs, you will receive an [error like this](https://github.com/oslocyclotronlab/OCL_GEANT4/issues/21).

<a name="more"/></a>
## 1- GEOMETRY DEFINITION
	
   The general geometry is constructed in the DetectorConstruction class, with 
   a helper class for each element (LaBr3s, Frame, SiRi ...). The geoetry is either
   implemented as Constructed Solids Geometry (CSG), or from the CAD drawings via
   GDML files. The CSG implementation is less precise, but much faster.

   You can chose which elements should be present by following commands in the macro:

   Further seetings are available to customize the detector geometry, like
   `/OCL/det/useCADFrameOuter true` or `/OCL/det/useCADFrameOuter false` to use/exclude
   the CAD version of the "outer" frame. More commands can be found [here](https://htmlpreview.github.io/?https://github.com/oslocyclotronlab/OCL_GEANT4/blob/master/docs/_OCL_.html).

   The LaBr3 setup consists of a cylinder containing the LaBr3 crystal, and 
   outer ring with shielding, a lit in front side of the detector.
   The shielding is composed as a boolean solid to
   include the conical front. The detector os optically coupled to 
   a bialkali photocathode through a Borosilicate PMT Window.

   The dimensions and materials have been chosen as close as possible to our 
   set-up, with additional information from i.a. Sain-Gobain. 
   Where no manufacturer information was available, we used assumptions 
   based e.g. other studies. The is an arbitrary mix of materials created with 
   the NIST manager and by hand. Additionally, we defined the optical properties
   and Surfaces and boundary processes for the Scintillation process.
   (only if activated in physics list)
   
   Note that the beam line is not set to Vacuum as this would complicate the geometry definition
   at the current stage without an obvious benefits for our accurac level.
		
## 2- PHYSICS LIST
 
  We now use QGSP_BIC_HP, such that the simulation can eg be used for neutrons 
  without modifications. To get scintillation processes, you can eg use the 
  physics described in the src/PhysicsList file.
 
  If activating G4OpticalPhysics [mostly for visualisation purposes]:
  To speed-up the simulations one can either set the ScinillationYieldFactor to a low value
  (for example 0.0008) or uncomment the scintillation physics part totally.
  -- 12/10/15 One should review/set the ScintillationExcitationRatio, the ratio for the 
  fast&slow excitation ratio.
 	
## 3- AN EVENT : THE PRIMARY GENERATOR
 
  The Primary Generator is defined in the PrimaryGeneratorAction  via 
  the G4GeneralParticleSource. The type of the particle and its energy 
  (and possible biases/shape...) are via macro.
        
## 4- DETECTOR RESPONSE

   The detector response is simulated via UserSteppingAction in the 
   SteppingAction class. More precisely, the number and time of absorbed photons 
   in the PMT cathode is recorded; the broadening due to the PMT has to be
   modelled separately and is not implemented here.
  
   The total energy deposited is taken from the crystal volume. 
   Important for optical physics: Geant4 does not conserve energy for optical 
   photons! Check the results with easy configurations!
   (The main problem previously seems to have been the creation of the 
   histograms)
   
   The energy deposited is collected step by step for a selected volume
   in SteppingAction and accumulated event by event in EventAction.
   
   At end of event, the value accumulated in EventAction is added in Run
   and summed over the whole run (see EventAction::EndOfevent()).
   
   The ntuples are exported as a tree to root files to the data folder. 
   The default output file and path can be changed via the macros.
   
   
___
### The following paragraphs are common to 
### all basic examples (where this has been taken from)
### A- VISUALISATION

   The visualization manager is set via the G4VisExecutive class
   in the main() function in exampleB1.cc.    
   The initialisation of the drawing is done via a set of /vis/ commands
   in the macro vis.mac. This macro is automatically read from
   the main function when the example is used in interactive running mode.

   By default, vis.mac opens an OpenGL viewer (/vis/open OGL).
   The user can change the initial viewer by commenting out this line
   and instead uncommenting one of the other /vis/open statements, such as
   HepRepFile or DAWNFILE (which produce files that can be viewed with the
   HepRApp and DAWN viewers, respectively).  Note that one can always
   open new viewers at any time from the command line.  For example, if
   you already have a view in, say, an OpenGL window with a name
   "viewer-0", then
      /vis/open DAWNFILE
   then to get the same view
      /vis/viewer/copyView viewer-0
   or to get the same view *plus* scene-modifications
      /vis/viewer/set/all viewer-0
   then to see the result
      /vis/viewer/flush

   The DAWNFILE, HepRepFile drivers are always available
   (since they require no external libraries), but the OGL driver requires
   that the Geant4 libraries have been built with the OpenGL option.

   From Release 9.6 the vis.mac macro in example B1 has additional commands
   that demonstrate additional functionality of the vis system, such as
   displaying text, axes, scales, date, logo and shows how to change
   viewpoint and style.  Consider copying these to other examples or
   your application.  To see even more commands use help or
   ls or browse the available UI commands in the Application
   Developers Guide, Section 7.1.

   For more information on visualization, including information on how to
   install and run DAWN, OpenGL and HepRApp, see the visualization tutorials,
   for example,
   http://geant4.slac.stanford.edu/Presentations/vis/G4[VIS]Tutorial/G4[VIS]Tutorial.html
   (where [VIS] can be replaced by DAWN, OpenGL and HepRApp)

   The tracks are automatically drawn at the end of each event, accumulated
   for all events and erased at the beginning of the next run.

 ### B- USER INTERFACES
 
   The user command interface is set via the G4UIExecutive class
   in the main() function in exampleB1.cc 
   The selection of the user command interface is then done automatically 
   according to the Geant4 configuration or it can be done explicitly via 
   the third argument of the G4UIExecutive constructor (see exampleB4a.cc). 
 
### C- HOW TO RUN the simulations (outdated?)

    - Execute OCL in the 'interactive mode' with visualization:
        % ./OCL
      and type in the commands from run1.mac line by line:
      	Idle> /control/execute run1.mac
        Idle> /run/beamOn 10 
        Idle> ...
        Idle> exit
      or
        Idle> /control/execute run1.mac
        ....
        Idle> exit

    - Execute OCL  in the 'batch' mode from macro files 
      (without visualization)
        % ./OCL run1.mac
        % ./OCL OCL.in > OCL.out
   ///////////////////////////////////////////
   ///////////////////////////////////////////


### Obtaining the response functions (outdated?)
- Run the simulation for a grid of gamma-ray energies, eg with `runsims.sh`.
- Analyse the histograms in the data directory with `GetPeaks.dat`. This will create a summary file, `Peaks.dat` and spectra of the compton/rest for unfolding with mama.
- Smooth the spectra for mama, running the `RunSmooth.py` script.

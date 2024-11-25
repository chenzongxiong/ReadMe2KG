![Header image](gfx/FALCON_header.jpg "FALCON")

FALCON - Fast Analysis of LTE Control channels
==============================================

[![Release](https://img.shields.io/github/release/falkenber9/falcon)](https://github.com/falkenber9/falcon/releases)
[![AUR](https://img.shields.io/aur/version/tudo-falcon)](https://aur.archlinux.org/packages/tudo-falcon)
[![DOI](https://img.shields.io/badge/DOI-10.1109/GLOBECOM38437.2019.9014096-fcb426.svg)](https://dx.doi.org/10.1109/GLOBECOM38437.2019.9014096)
[![arXiv](https://img.shields.io/badge/arXiv-1907.10110-b31b1b.svg)](https://arxiv.org/abs/1907.10110)
[![License](https://img.shields.io/github/license/falkenber9/falcon)](LICENSE)
[![Video](https://img.shields.io/youtube/views/Va_aZYxRu3U)](http://www.youtube.com/watch?v=Va_aZYxRu3U)

**FALCON** is an open-source software collection for real-time analysis of radio resources in private or commercial LTE/LTE-A networks.

It decodes the Physical Downlink Control Channel (PDCCH) of a base station and reveals the number of currently active devices including their Radio Network Temporary Identifiers (RNTIs) and their individual resource allocations.

FALCON enables an exact determination of the current network load and the identification of bottlenecks. This information can be used to predict the achievable data rate of an additional subscriber by purely observing the current activity. Based on this criterion, congestion situations can be detected and avoidance strategies can be applied, e.g. switching to another network or postponing delay-tolerant transmissions.

Based on [srsLTE][srslte] library, the software can be run on a plain x86 general-purpose PCs with any compatible SDR.



![TU Dortmund University](gfx/tu-dortmund_small.png "TU Dortmund University")
![SFB 876](gfx/SFB876_small.png "Collaborative Research Center SFB 876")
![Communication Networks Institute](gfx/CNI_small.png "Communication Networks Institute")
![DFG](gfx/DFG_small.png "DFG")

The research around this project has been supported by *Deutsche Forschungsgemeinschaft* (DFG) within the Collaborative Research Center SFB 876
“Providing Information by Resource-Constrained Analysis”, project A4 at TU Dortmund University.

A **corresponding scientific publication** (IEEE GLOBECOM 2019) is available on [IEEE Xplore](https://dx.doi.org/10.1109/GLOBECOM38437.2019.9014096) and on [ArXiV](https://arxiv.org/abs/1907.10110).

Please see section [Acknowledgements](#acknowledgements) of how to reference this project.

## Video
[![FALCON Video Presentation](http://img.youtube.com/vi/Va_aZYxRu3U/0.jpg)](http://www.youtube.com/watch?v=Va_aZYxRu3U)

## License
FALCON is released under the [AGPLv3 license](LICENSE).


## Key Features
* Reliable real-time monitoring public LTE cells
* Monitoring up to 20 MHz bandwidth
* FDD only
* Supported DCI formats: 0/1A, 1, 1B, 1C, 2, 2A, 2B
* Suitable for short-term and long-term monitoring with non-ideal radio conditions
* Qt-based and OpenGL-accelerated GUI for visualization of allocated resource blocks, spectrogram and cell-specific performance metrics (throughput, resource utilization, user activity, etc.).
* Synchronized recorder with integrated support for network probing by an auxiliary modem

Check the [changelog](CHANGELOG.md) for recently introduced updates.

### Planned Features
* TDD
* Support for DCI with Carrier Indicator Field (CIF)
* Multithreaded DCI search
* Visualization of System Information Blocks (SIB)

## Installation

Installation has been verified on the following operating systems:

* Ubuntu 18.04.x LTS (Bionic Beaver)
* Ubuntu 20.04.x LTS (Focal Fossa)
* Archlinux [![](https://img.shields.io/aur/version/tudo-falcon)](https://aur.archlinux.org/packages/tudo-falcon) [![](https://img.shields.io/aur/maintainer/tudo-falcon)](https://aur.archlinux.org/packages/tudo-falcon)

### Installation on Ubuntu

#### 1) Required Dependencies
FALCON installation automatically downloads a patched version of srsLTE and c-mnalib as subproject during the build process. Please install the following dependencies which are required by FALCON or its included components:

For srsLTE:
```sh
sudo apt-get install build-essential git cmake libfftw3-dev libmbedtls-dev libboost-program-options-dev libconfig++-dev libsctp-dev
```
For srsGUI (only required to build the ported version of IMDEA OWL):
```sh
sudo apt-get install libboost-system-dev libboost-test-dev libboost-thread-dev libqwt-qt5-dev qtbase5-dev
git clone https://github.com/srsLTE/srsGUI.git
cd srsgui
mkdir build
cd build
cmake ../
make
sudo make install
```
For USRP support:
```sh
sudo add-apt-repository ppa:ettusresearch/uhd
sudo apt-get update
sudo apt-get install libuhd-dev uhd-host
```

For LimeSDR support:
```sh
sudo add-apt-repository -y ppa:myriadrf/drivers
sudo apt-get update
sudo apt-get install limesuite limesuite-udev limesuite-images
sudo apt-get install soapysdr soapysdr-module-lms7
```

For FALCON:
```sh
sudo apt-get install libglib2.0-dev libudev-dev libcurl4-gnutls-dev libboost-all-dev qtdeclarative5-dev libqt5charts5-dev
```

#### 2) FALCON:
```sh
git clone https://github.com/falkenber9/falcon.git
cd falcon
mkdir build
cd build
cmake -DCMAKE_INSTALL_PREFIX=/usr ../
make

# Install (optional)
sudo make install

# Uninstall (use carefully!)
sudo xargs rm < install_manifest.txt
```

**Note:** FALCON requires a [patched version][srslte-falcon-patch] of srsLTE 18.09 that is automatically downloaded and included as subproject during the build process. However if a diffferent version of srsLTE is already installed on the computer, the build system will link against that version. In case of conflicts, force the use of srsLTE as a subproject by adding ``-DFORCE_SUBPROJECT_SRSLTE=ON`` to the ``cmake`` options. In this case, take care with ``make install``, since this may overwrite your existing version of srsLTE. Example:
```
...
cmake -DFORCE_SUBPROJECT_SRSLTE=ON -DCMAKE_INSTALL_PREFIX=/usr ../
...
```


### Installation on Archlinux
On Archlinux build and install the package ``tudo-falcon`` [![](https://img.shields.io/aur/version/tudo-falcon)](https://aur.archlinux.org/packages/tudo-falcon) from the [Arch User Repository (AUR)](https://aur.archlinux.org).
The most convenient way is the use of an [AUR Helper](https://wiki.archlinux.org/index.php/AUR_helpers), e.g. [yay](https://aur.archlinux.org/packages/yay) or [pacaur](https://aur.archlinux.org/packages/pacaur). The following example shows the installation with ``yay``.

```sh
# Install
yay -Sy tudo-falcon

# Uninstall
sudo pacman -Rs tudo-falcon
```

#### Installation without AUR Helper

Without an AUR Helper, the package(s) can be built in a local directory with ``makepkg`` and installed via ``pacman``:
```sh
# Prerequisites
pacman -S --needed base-devel

# Build directory
mkdir falcon-packages
cd falcon-packages

# Dependency c-mnalib
git clone https://aur.archlinux.org/c-mnalib.git
cd c-mnalib
makepkg -si
cd ..

# Dependency srsLTE (patched)
git clone https://aur.archlinux.org/srslte-falcon-patch-git.git
cd srslte-falcon-patch-git
makepkg -si
cd ..

# FALCON
git clone https://aur.archlinux.org/tudo-falcon.git
cd tudo-falcon
makepkg -si
```

## SDR Hardware
FALCON has been tested with the following Software Defined Radios (SDRs):

* Ettus Research: USRP B210
* Ettus Research: USRP B205mini
* Lime Microsystems: LimeSDR Mini

In addition, any SDR supported by [srsLTE library][srslte] should work as well.

## Computer Hardware Requirements / Performance
Real-time decoding of LTE signals requires a mature multicore CPU, especially when monitoring busy cells and large bandwidths (i.e. 15MHz and 20MHz cells). Large sample rates, wide FFTs, and larger search spaces make heavy use of the CPU, memory and involved buses.

In case of minor/sporadic performance issues, FALCON starts skipping/dropping single subframes in favor of maintaining synchronization if the processing of previous (buffered) subframes takes too long.
Serious performance issues lead to IQ-sample overflows and degraded synchronization which causes false detections (spurious DCI) or may even cause an entire synchronization loss.

The actual computational demands depend on many internal (CPU capabilities, memory bandwidth, power-saving techniques, other processes) and external factors (interference from neighboring cells/sectors, signal strength, cell activity).
Therefore, the following *rules of thumb* may not all be required for your setup or may not be sufficient to obtain satisfactory results.

### General Recommendations
* Don't run any other fancy (GUI) application at the same time, e.g. browser or Email clients
* Use a CPU with at least 4 physical cores
* Disable Hyper-Threading
* Disable power-saving techniques such as DVFS and put the CPU into *performance* mode

### Example Systems
All systems were tested with a USRP B210 SDR, attached via USB 3.0 and simple dipole antenna (connected via 1m SMA HF cable).
#### Lenovo X250 Notebook
* Intel Core i7-5600U (Dual Core CPU + Hyper-Threading), 2.6GHz, 8GB RAM, SSD
* Arch Linux, kernel 5.3.5-arch1-1-ARCH, KDE/Plasma desktop environment
* GUI: Good results up to 10MHz bandwidth and good LTE signal.
* FalconEye: Good results up to 15MHz bandwidth and good LTE signal.
* 20 MHz bandwidth: subframe skip ratio up to 50%, eventually sync loss, many false detections

#### Lenovo T540p
* Intel Core i7-4710Q (4 Core CPU + Hyper-Threading), 2.5GHz, 8GB RAM, SSD
* Ubuntu 18.04.3 LTS (bionic), kernel 4.15.0-66-generic, GNOME or KDE/Plasma desktop environment
* GUI: Good results up to 20MHz bandwidth and good LTE signal; frame skips during window resizing
* FalconEye: Good results up to 20MHz bandwidth and good LTE signal

## Usage Instructions
This section provides brief usage instructions for FALCON. The software collection comprises the following components:

* FalconGUI: A visualization for online/offline PDCCH decoding
* FalconEye: A command-line version of the PDCCH decoder for automated/batch processing
* FalconCaptureProbe: Signal recorder with optional network probing
* FalconCaptureWarden: A command-line controller for synchronized recordings by multiple instances of FalconCaptureProbe
* imdea_cc_decoder: Port of IMDEA OWL's PDCCH decoder
* imdea_capture_sync: Port of IMDEA OWL's signal recorder

### FALCON GUI
To start the GUI version of FALCON's decoder, simply launch ``FalconGUI`` from a terminal or from your preferred window manager. Without installation, ``FalconGUI`` is located in ``<build-dir>/src/gui/FalconGUI``.
Enter the center frequency of the target LTE cell or select a recording from a file using the file chooser or drag & drop. Example files are provided in a [separate repository][examples].

Press 'Start' and the decoder immediately starts to synchronize to the cell and decodes the PDCCH.
The GUI will display waterfall plots of the spectrum and resource allocations (uplink and downlink) in real-time. The color of the displayed resource allocations is derived from the individual RNTIs of the particular subscribers.

**Note:** At any time, you can click on a waterfall plot to freeze current state. Scroll to go back and forth in time within the scrollback buffer.


![FALCON Screenshot](gfx/FalconGUI.png "Falcon GUI Screenshot")


### FALCON Eye
A command-line version of FALCON Decoder. For real-time monitoring of a cell, e.g. at 1829.4 MHz, run the following command:
```sh
FalconEye -f 1829.4e6 -D /tmp/dci.csv
```
This will print an ASCII visualization of the discovered resource allocations to the terminal and a detailed log of all captured DCI into the trace file ``/tmp/dci.csv``.
Press [CTRL]+C to exit the application and print some statistics of the run.

The output of Falcon Eye for a 15MHz (75 PRB) cell should look as follows:

![FALCON Eye Screenshot](gfx/FalconEye.png "FalconEye Screenshot")

#### DCI Tracefile Contents
The DCI tracefile is structures as CSV file, using tabs ("\t") as separator. The columns contain:
```python
COLUMNS_FALCON_DCI = [
    'timestamp',    # unix timestamp in [s] as float, 1µs resolution
    'sfn',          # system frame number
    'subframe',     # subframe index {0,1,...,9}
    'rnti',         # the addressed RNTI
    'direction',    # 0 for uplink alloc., 1 for downlink alloc.
    'mcs_idx',      # MCS index of the first transport block
    'nof_prb',      # number of allocated PRBs
    'tbs_sum',      # total Transport Block Size (TBS) in [Bit]
    'tbs_0',        # TBS of first transport block (-1 for SISO)
    'tbs_1',        # TBS of second transport block (-1 for SISO)
    'format',       # index+1 of DCI format in array flacon_ue_all_formats[], see DCISearch.cc
    'ndi',          # new data indicator for first transport block
    'ndi_1',        # new data indicator for second transport block
    'harq_idx',     # HARQ index
    'ncce',         # index of first Control Channel Element (CCE) of this DCI within PDCCH
    'L',            # aggregation level of this DCI {0..3}, occupies 2^L consecutive CCEs.
    'cfi',          # number of OFDM symbols occupied by PDCCH
    'histval',      # number of occurences of this RNTI within last 200ms
    'nof_bits',     # DCI length (without CRC)
    'hex'           # raw DCI content as hex string, see sscan_hex()/sprint_hex() in falcon_dci.c 
]
```

### FALCON Capture Probe and Capture Warden
Two command-line tools provide recording of LTE signals and optional cell probing by an auxiliary modem (supported by c-mnalib).
For synchronized recordings by multiple (distributed) instances of ``FalconCaptureProbe``, the ``FalconCaptureWarden`` provides a text-based command prompt for synchronous remote control.

Note: In order to reduce the IO-load of the capturing system, ``FalconCaptureProbe`` will store the captured samples in RAM and write them to file after the capturing has ended.
For this purpose, the application allocates all available RAM (minus 500MB as a reserve) for the internal sample buffer.
The capturing process stops if the allocated buffer size is exceeded.

#### Minimum example: capture raw data from a cell
In order to capture raw data from an LTE cell and store it on the hard disk for later (offline) analysis, launch ``FalconCaptureProbe`` as follows:

```sh
FalconCaptureProbe -f <carrier_frequency_Hz> -n <nof_subframes> -o example
```
* carrier_frequency_Hz: Center frequency in Hz of the LTE cell to capture. Exponential values are also accepted, e.g. ``1845e6``.
* nof_subframe: Number of subframes (= milliseconds) to capture. A value of ``5000`` may be a good start.

If it succeeds, the current working directory will contain the following files:

* ``example-unknownOperator-cell.csv``: General cell information in CSV format
* ``example-unknownOperator-iq.bin``: Raw IQ samples of the cell for later analysis

## Application Notes
This section contains general application notes that might be helpful for reliable and accurate control channel analysis.

### Signal Strength and Interference
FALCON has a multi-stage validation chain that reduces error detection to a minimum even under non-ideal signal conditions.
However, in order to obtain a complete view of cell activity, a location with good signal conditions should be chosen. This is because resource allocations for users with a good signal can be sent with less redundancy (lower aggregation level), but cannot be decoded correctly under poor channel conditions.

### Uncommon occupancy of PDCCH
In most cases, the eNodeB only emits a signal on actually occupied CCEs of the PDCCH, while free CCEs are left empty.
FALCON uses this circumstance for performance and skips empty CCEs.

However, some open-source eNodeBs (e.g. Open Air Interface) nevertheless send a significant signal on empty CCEs. In typical applications with normal UEs, this does not lead to any disadvantages, only to increased interference on the control channel when several cells are used.
But depending on the actual content, such CCEs can lead to false detections by FALCON's *short-cut* detector. To counteract this, the *short-cut* detector can be deactivated (option ``-L`` in ``FalconEye``). The detection of the participants then takes place exclusively via random access and with the help of histograms based on the frequency of occurrence of individual RNTIs. In the latter case, previously unseen RNTIs are only accepted and activated with a time delay after a threshold value has been reached, e.g. at least 5 resource assignments in the last 200ms.
The threshold value can be configured by the option ``-H <threshold>`` in ``FalconEye``.


## Comparison with IMDEA OWL
FALCON is an alternative to [IMDEA OWL][imdea-owl] which provides comparable functionalities for long-term monitoring of LTE cells. Other than OWL, FALCON additionally targets use cases that require short-term monitoring, mobility or increased robustness against non-ideal radio conditions.

The interface of FALCON's recorder and decoder is mostly compatible with [IMDEA OWL][imdea-owl].
FALCON inherits OWL's approach of tracking C-RNTI assignments from PRACH for any UE that joins the cell during the observation time.
However, the method to discover already active C-RNTIs from earlier assignments differs significantly.
FALCON uses RNTI histograms and shortcut decoding to validate unseen RNTIs during the blind decoding procedure.
In contrast to OWL's re-encoding approach, this method is significantly less sensitive to non-ideal radio conditions. This makes FALCON suitable for robust and reliable short-term monitoring, e.g. for mobile applications.

A direct comparison of FALCON and OWL in a controlled environment is discussed in this [video presentation][video-presentation].

### Included port of IMDEA OWL for Benchmarking
The original version of IMDEA OWL was hardcoded into a fork of srsLTE v1.3 from Sep. 2016 and was updated to srsLTE v2.0 in Jul. 2017.
In order to provide a fair comparison of FALCON and OWL and their underlying methods, we extracted and ported OWL with its custom extensions on the srsLTE library into the FALCON project as separated modules and applications.
By this, both applications benefit from future advancements of srsLTE library.

### Validation of the port against the original version

Every port requires at least slight adaptations of the code, especially if the underlying libraries evolve.
However, this may lead to unintended side effects such as deviant functionality or different handling of exceptions.

We validated the functionality of the IMDEA OWL port against its original implementation by processing the same record of a public LTE cell (IQ samples) with both programs and compared the outputs.

This required the following precautions:

- **Switch Viterbi decoder to 8 bit**: srsLTE uses a 16-bit Viterbi decoder if AVX2 is available, whereas the version underlying IMDEA OWL uses 8-bit Viterbi decoder. This circumvents direct comparison since spurious (false) DCI are decoded to different sequences of bits. Therefore, ``#undef VITERBI_16`` in file ``dci.c`` of srsLTE library even if ``LV_HAVE_AVX2`` is defined to achieve the same behavior.

With these precautions, both versions decoded and processed exactly the same set of DCI candidates (whether true or spurious). All candidates were classified identically.
However, we noticed the following (minor) differences:

- **DCI scrambled with RA/P/SI-RNTI**: MCS is correctly provided by the ported version. In such cases the original version always reports MCS=0.
- **Swapping**: In case the *Transport Block to Codeword Swap Flag* is set, the related values appear in swapped order.
- **Invalid RB allocation**: If the library detects an illegal RB allocation (i.e. spurious DCI carrying an illegal resource block group assignment), a nulled line is printed. The original version prints arbitrary values.



## Related Publications
- B. Sliwa, R. Falkenberg, C. Wietfeld, [**Towards Cooperative Data Rate Prediction for Future Mobile and Vehicular 6G Networks**](https://arxiv.org/abs/2001.09452), In *2nd 6G Wireless Summit (6G SUMMIT)*, 2020.
- R. Falkenberg, C. Wietfeld, [**FALCON: An Accurate Real-time Monitor for Client-based Mobile Network Data Analytics**](https://arxiv.org/abs/1907.10110), In *GLOBECOM 2019 - 2019 IEEE Global Communications Conference*, 2019.
- R. Falkenberg, K. Heimann, C. Wietfeld, [**Discover Your Competition in LTE: Client-Based Passive Data Rate Prediction by Machine Learning**](https://arxiv.org/abs/1711.06820), In *GLOBECOM 2017 - 2017 IEEE Global Communications Conference*, 2017.
- R. Falkenberg, C. Ide, C. Wietfeld, [**Client-Based Control Channel Analysis for Connectivity Estimation in LTE Networks**](https://arxiv.org/abs/1701.03304), In *IEEE Vehicular Technology Conference (VTC-Fall)*, 2016.



## Acknowledgements

To acknowledge us in your publication(s) please refer to the following publication:

```tex
@InProceedings{Falkenberg2019a,
	Author = {Robert Falkenberg and Christian Wietfeld},
	Title = {{FALCON}: An Accurate Real-time Monitor for Client-based Mobile Network Data Analytics},
	Booktitle = {2019 IEEE Global Communications Conference (GLOBECOM)},
	Year = {2019},
	Address = {Waikoloa, Hawaii, USA},
	Month = dec,
	Publisher = {IEEE},
	Doi = {10.1109/GLOBECOM38437.2019.9014096},
	Eprint = {1907.10110},
	Eprinttype = {arxiv},
	Url = {https://arxiv.org/abs/1907.10110}
}
```


<!-- Identifiers, in alphabetical order -->

[imdea-owl]: https://git.networks.imdea.org/nicola_bui/imdeaowl
[examples]: https://github.com/falkenber9/falcon-examples
[srslte]: https://github.com/srsLTE/srsLTE
[srslte-falcon-patch]: https://github.com/falkenber9/srsLTE
[video-presentation]: https://www.youtube.com/watch?v=Va_aZYxRu3U


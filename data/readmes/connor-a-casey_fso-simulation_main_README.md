<div align="center">
    <h1>
        <img src="assets/header.jpg">
    </h1>
</div>

# IAC 2024 Space Communications and Quantum Symposium

This repository contains resources related to the **75th International Astronautical Congress (IAC) 2024** symposium focused on Space Communications and Quantum Technologies.

## Presentation Information
**Title:** Advancing Free-Space Optical Communication System Architecture: Performance Analysis of Diverse Optical Ground Station Network Configurations

**Authors:** 
- Mr. Eugene Rotherham: University College London (UCL), United Kingdom
- Mr. Connor Casey: University of Massachusetts Amherst, United States
- Ms. Eva Fernandez Rodriguez: Netherlands Organisation for Applied Scientific Research (TNO), The Netherlands
- Ms. Karen Wendy Vidaurre Torrez: Space Generation Advisory Council (SGAC), Bolivia
- Mr. Maren Mashor: Space Generation Advisory Council (SGAC), Nigeria
- Mr. Isaac Pike: University College London (UCL), United Kingdom

**About the Presentation:**
This presentation explores the frontier of space-based optical and quantum communications. It provides an in-depth analysis of various configurations of optical ground station networks to enhance communication systems in space.

## Repository Structure

The repository is organized into two main folders:

1. `src`: Contains the source code for each component of the model.
2. `data`: Stores input data and output results.

### Source Code (`src`)

The `src` folder contains subfolders for each component of the model:

1. satellite_passes
2. turbulence
3. cloud_cover
4. data_integrator
5. dynamic_analysis

Each subfolder contains the scripts necessary for that particular component of the model.

### Data (`data`)

The `data` folder is divided into two subfolders:

1. `input`: Contains the `satelliteParameters.txt` file with essential parameters for the model.
2. `output`: Stores the results from each component of the model in separate subfolders:
   - satellite_passes
   - turbulence
   - cloud_cover
   - data_integrator
   - dynamic_analysis

## Data Flow and Execution Order

The model components are executed in the following order:

1. satellite_passes
2. turbulence
3. cloud_cover
4. data_integrator
5. dynamic_analysis

### Key Points:

- Each component in the `src` folder reads data from the `satelliteParameters.txt` file in the `data/input` folder.
- The `satellite_passes` component also uses a `.tle` (Two-Line Element) file for satellite orbit data.
- The `cloud_cover` component interacts with an API gateway for retrieving cloud cover data.
- The `data_integrator` component pulls data from the `satellite_passes`, `turbulence`, and `cloud_cover` components.
- The `dynamic_analysis` component uses data from both the `satelliteParameters.txt` file and the `data_integrator` component.

## Software Architecture
<div align="center">
    <h1>
        <img src="assets/software_architecture_vF.svg">
    </h1>
</div>

This diagram illustrates the repository structure, execution order, and data flow between components.

## Usage

To run the model:

1. Ensure all required data is present in the `data/input` folder.
2. Add your TLE file (e.g., `terra.tle`) into the same folder as the `satellite_passes` folder.
3. Create a `.env` file in the project root directory and add your EUMET API key as follows:
   ```
   EUMET_API_KEY=your_api_key_here
   ```
4. Fill in all necessary parameters in the `satelliteParameters.txt` file located in the `data/input` folder.
5. Execute the scripts in the `src` folder in the order specified above.
6. Check the `data/output` folder for results from each component.

## Dependencies

- Satellite TLE data file (`.tle`)
- API gateway access for cloud cover data
- Python (version X.X or higher)
- [List any other dependencies or libraries required]


## Repository Contents:
- **Paper:** [Link to published paper](https://arxiv.org/abs/2410.23470)
- **Datasets:** [Link to datasets](https://www.dropbox.com/scl/fo/k7yug64a3rukr89p8xlmq/AH92crjcwRxoaDdJj1JSdmM?rlkey=i7putlvrf36inva68dfwipo6y&st=e0bcoyof&dl=0)
- **Data Analysis:** [Link to Notebook](https://www.dropbox.com/scl/fo/b1rnfzf3o8bz4iplv2ql4/AL59S5MLe3bO77BnmGWxis0?rlkey=fm22cwnophj40uggofkulb1x7&st=ienm03r6&dl=0)

## Contact Information:
For inquiries or collaborations related to this presentation, please reach out to the authors directly via the provided email addresses in AUTHORS.txt

We appreciate your interest in our work!

## License

[Specify the license under which this project is released]

# RAAC Hospital Interactive Maps

**Author:** Dr Lixu Liu  
**Position:** Research Fellow  
**Contact:**

- Academic:
  - l.liu.9@bham.ac.uk
  - l.liu2@lboro.ac.uk
- Personal: lixu@verdemetrix.com

**Affiliations:**

- Department of Civil Engineering, University of Birmingham
- School of Architecture, Building and Civil Engineering, Loughborough University
- Centre for Postdoctoral Development in Infrastructure, Cities and Energy (C-DICE)
- RAAC Research Team, Loughborough University

## Overview

This project provides an interactive map visualizing hospitals in England that have confirmed presence of Reinforced Autoclaved Aerated Concrete (RAAC). It combines data processing scripts, mapping tools, and a pre-generated web-based visualization.

The downloadable ZIP archive includes:

- Python source code for geocoding and map generation
- Hospital dataset with RAAC information
- A fully generated HTML file (`index.html`) showing the interactive map

The **source code is maintained on GitHub**, and the latest interactive map is **publicly accessible via GitHub Pages**.

### This tool helps users:

- Identify and locate hospitals with confirmed RAAC structures
- Visualize the geographic distribution of RAAC-affected facilities
- Access hospital information interactively using a map interface

It is particularly useful for:

- **Healthcare facility managers** monitoring RAAC risk
- **Structural engineers** assessing infrastructure safety
- **Public health officials** and emergency response planners
- **Researchers** studying hospital building materials and conditions

## Data Source

The hospital data used in this project is sourced from the UK Government's official publication:
[Reinforced autoclaved aerated concrete (RAAC) in hospitals: management information](https://www.gov.uk/government/publications/reinforced-autoclaved-aerated-concrete-raac-in-hospitals-management-information)

This data is part of NHS England's ongoing national RAAC programme, which has been allocated £954 million since the 2021 to 2022 financial year for remediation and failsafe measures. The data includes:

- Site location
- NHS trust information
- RAAC status
- Latest updates on RAAC presence and remediation

## Current Project Structure

```
raac-hospital-interactive-maps/
├── src/                    # Source code directory
│   ├── step1_get_coordinates.py    # Script to get coordinates from addresses
│   └── step2_create_map.py         # Script to generate the interactive map
├── data/                   # Data files directory
│   ├── hospital-sites-with-confirmed-raac-in-england-3-october-2024.csv  # Original data
│   ├── coordinates.xlsx            # Generated coordinates file
│   └── NGL15- Hospital_sites_with_confirmed_RAAC_list.xlsx  # Enhanced input data
├── index.html              # Generated interactive map
├── requirements.txt        # Python dependencies
└── README.md              # Project documentation
```

## Step-by-Step Guide

### Step 1: Prepare Your Data

1. Download the CSV file from the UK Government website:

   - File name: `hospital-sites-with-confirmed-raac-in-england-3-october-2024.csv`
   - Contains basic hospital information including Region, Trust, Site Notes, and RAAC Status

2. Convert and enhance the data:

   - Convert the CSV file to Excel format
   - Create a new file named `NGL15- Hospital_sites_with_confirmed_RAAC_list.xlsx`
   - Add the following columns:
     - Required Columns:
       - `Hospital Name`: Use the Site Notes from the CSV
       - `Address`: Complete address including street, city, and county (add manually)
       - `Postcode`: UK postcode (e.g., AB12 3CD) (add manually)
     - Optional Columns:
       - `RAAC Status`: Copy from the CSV
       - `Building Name`: Can be extracted from Site Notes
       - `Notes`: Any additional information

3. Example of how your data should look:
   ```
   Hospital Name | Address                    | Postcode  | RAAC Status | Building Name | Notes
   -------------|----------------------------|-----------|-------------|---------------|-------
   Hospital A   | 123 Main Street, City      | AB12 3CD  | Confirmed   | Main Block    | ...
   Hospital B   | 456 High Road, Town        | EF45 6GH  | Suspected   | East Wing     | ...
   ```

### Step 2: Set Up the Project

1. Download or clone the project files
2. Ensure you have the following structure:

   ```
   raac-hospital-interactive-maps/
   ├── src/
   │   ├── step1_get_coordinates.py
   │   └── step2_create_map.py
   ├── data/
   ├── requirements.txt
   └── README.md
   ```

3. Place your Excel file in the `data` folder:
   ```
   raac-hospital-interactive-maps/data/NGL15- Hospital_sites_with_confirmed_RAAC_list.xlsx
   ```

### Step 3: Install Required Software

1. Install Python (version 3.8 or higher) if not already installed
2. Open a terminal/command prompt
3. Navigate to the project directory
4. Install required Python packages:
   ```bash
   pip install -r requirements.txt
   ```
   This will install:
   - pandas (for data manipulation)
   - folium (for map creation)
   - openpyxl (for Excel file handling)
   - geopy (for geocoding)

### Step 4: Generate the Map

1. Run the first script to get coordinates:

   ```bash
   python src/step1_get_coordinates.py
   ```

   - This will create `coordinates.xlsx` in the data folder
   - The script will:
     - Read the hospital data from your Excel file
     - Convert addresses to coordinates using geocoding
     - Save the results in `coordinates.xlsx`

2. Run the second script to create the interactive map:
   ```bash
   python src/step2_create_map.py
   ```
   - This will generate `index.html` in the main directory
   - The script will:
     - Read the coordinates from `coordinates.xlsx`
     - Create an interactive map using Folium
     - Add markers for each hospital
     - Save the map as `index.html`

### Step 5: View and Use the Map

1. Open `index.html` in a web browser
2. The interactive map will show:
   - All hospitals as markers on the map
   - Click on any marker to see hospital details
   - Use the zoom controls to explore different areas
   - Use the search function to find specific hospitals

### Troubleshooting

1. If coordinates are not generated:

   - Check that your Excel file has the correct column names
   - Verify that addresses and postcodes are in the correct format
   - Ensure you have an internet connection (needed for geocoding)
   - Check the console output for any error messages

2. If the map doesn't show all hospitals:

   - Check `coordinates.xlsx` for any failed geocoding attempts
   - Verify that all required columns are present in your input file
   - Look for any error messages in the console output

3. If the map doesn't open:
   - Ensure `index.html` was generated successfully
   - Try opening it in a different web browser
   - Check if the file size is reasonable (should be around 50KB)

## Technical Details

- Python for data processing
- HTML/CSS/JavaScript for web interface
- Folium for map visualization
- Pandas for data manipulation
- Excel data formats

## License

This project is licensed under the [Creative Commons Attribution 4.0 International License (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/).  
You may use this work — even commercially — as long as you give proper credit to the author.

## Acknowledgements

This work has been made possible through the support of:

- Centre for Postdoctoral Development in Infrastructure, Cities and Energy (C-DICE)
- IMFUNA LTD
- University of Birmingham
- Loughborough University

## Version Information

- Current Version: 1.0.0
- Last Updated: May 2025
- DOI: [To be assigned by the repository]

## Citation

If you use this work in your research, please cite it as:

```
Liu, L. (2025). RAAC Hospital Interactive Maps [Computer software]. University of Birmingham. https://doi.org/[DOI to be assigned]
```

## Funding

This research was supported by:

- Centre for Postdoctoral Development in Infrastructure, Cities and Energy (C-DICE)
- IMFUNA LTD

## Keywords

- RAAC (Reinforced Autoclaved Aerated Concrete)
- Hospital Infrastructure
- Interactive Mapping
- Healthcare Facilities
- Structural Monitoring
- Geographic Information Systems (GIS)
- Public Health Infrastructure
- Building Safety

## Related Publications

[To be added when available]

## Repository Information

- **Repository Type:** Research Software
- **Primary Language:** Python
- **Development Status:** Active
- **Intended Audience:** Researchers, Healthcare Facility Managers, Structural Engineers
- **Operating System:** Platform Independent
- **Programming Language:** Python 3.8+
- **Topic:** Healthcare Infrastructure, Building Safety, Geographic Information Systems

## How to Cite This Software

When citing this software in academic work, please use the following format:

```
@software{liu2025raacmaps,
  author = {Liu, Lixu},
  title = {RAAC Hospital Interactive Maps},
  year = {2025},
  publisher = {University of Birmingham},
  url = {https://doi.org/[DOI to be assigned]},
  version = {1.0.0}
}
```

# Home Battery and Solar System Simulation

This project provides a simulation model to analyze the financial viability and effectiveness of using home batteries and solar panels in Finland. The model takes into account various parameters such as electricity prices, solar production, household energy consumption, and battery usage strategies to determine potential savings and payback periods for different configurations.

## Table of Contents

- [Introduction](#introduction)
- [Simulation Assumptions](#simulation-assumptions)
- [Files in the Repository](#files-in-the-repository)
- [How to Run the Simulation](#how-to-run-the-simulation)
- [Dependencies](#dependencies)
- [Results](#results)
- [License](#license)

## Introduction

The simulation aims to evaluate the economic benefits of installing solar panels and battery storage systems in a residential setting in Finland. The model considers several factors, including:
- Seasonal variations in solar energy production.
- Fluctuating electricity prices depending on the time of day and season.
- Household energy consumption patterns.
- Costs associated with installing and maintaining solar panels and batteries.
- Potential revenue from selling excess energy back to the grid.

The output includes total savings, net savings, and payback periods for different configurations of solar panels and batteries.

## Simulation Assumptions

The following assumptions are made in the simulation:

1. **Electricity Prices by Quarter (€/kWh):**
   - Winter (Q1): 0.20 €/kWh
   - Spring (Q2): 0.10 €/kWh
   - Summer (Q3): 0.08 €/kWh
   - Autumn (Q4): 0.15 €/kWh

2. **Daily Price Variations:**
   - Winter: Daytime is cheaper by 0.05 €/kWh; Nighttime is more expensive by 0.05 €/kWh.
   - Spring: Daytime is cheaper by 0.03 €/kWh; Nighttime is more expensive by 0.03 €/kWh.
   - Summer: Daytime is cheaper by 0.02 €/kWh; Nighttime is more expensive by 0.02 €/kWh.
   - Autumn: Daytime is cheaper by 0.04 €/kWh; Nighttime is more expensive by 0.04 €/kWh.

3. **Solar Production Share by Season (average hours/day):**
   - Winter: 2 hours/day
   - Spring: 5 hours/day
   - Summer: 8 hours/day
   - Autumn: 4 hours/day

4. **Consumption Share by Season (% of total annual consumption):**
   - Winter: 40%
   - Spring: 20%
   - Summer: 15%
   - Autumn: 25%

5. **Annual Household Consumption:** 10,000 kWh, 15,000 kWh, 20,000 kWh, 30,000 kWh

6. **Battery Sizes (kWh):** 5 kWh, 20 kWh, 100 kWh

7. **Battery Efficiency:** 90% (round-trip efficiency)

8. **Battery Degradation Rate:** 2% per year

9. **Electricity Transmission Cost:** 0.0871 €/kWh

10. **Selling Price to Grid:** 0.10 €/kWh

11. **Solar Panel System Cost:** 1000 €/kW

12. **Battery Cost per kWh:**
   - 5 kWh: 500 €/kWh
   - 20 kWh: 400 €/kWh
   - 100 kWh: 350 €/kWh

13. **Simulation Period:** 5 years

## Files in the Repository

- `home_battery_simulation.py`: The main Python script that runs the simulation.
- `README.md`: This readme file.
- `requirements.txt`: List of dependencies required to run the script.
- `Home_Battery_Simulation_Results_Finland.xlsx`: Example output file generated by the script containing simulation results.

## How to Run the Simulation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/home-battery-simulation.git
   cd home-battery-simulation
   
Install dependencies:

Install the required Python packages using pip:

bash
Kopioi koodi
pip install -r requirements.txt
Run the simulation:

Execute the Python script to run the simulation:

bash
Kopioi koodi
python home_battery_simulation.py
View the results:

The script will generate an Excel file Home_Battery_Simulation_Results_Finland.xlsx containing the results of the simulation. Open the file to view the detailed results for different configurations of solar panel and battery sizes.

Dependencies
The simulation script requires the following Python libraries:

pandas
numpy
xlsxwriter
You can install these dependencies using the requirements.txt file provided.

Results
The simulation outputs include:

Total Savings (€): The total amount saved over the simulation period by using solar panels and batteries.
Net Savings (€): Total savings minus the initial investment cost.
Payback Period (Years): The time required to recover the initial investment through savings.
The results are provided for different combinations of battery sizes, solar panel sizes, and household consumption levels.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgements
The simulation model was developed to evaluate the economic feasibility of home battery and solar systems in Finland, considering various dynamic factors such as electricity prices, solar production, and consumption patterns.

vbnet








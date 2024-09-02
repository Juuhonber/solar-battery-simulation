import pandas as pd
import numpy as np

# Constants and assumptions for the simulation
battery_sizes = [5, 20, 100]  # kWh
solar_panel_sizes = [5, 7, 10]  # kW solar systems
household_consumptions = [10000, 15000, 20000, 30000]  # kWh
battery_efficiency = 0.90  # 90% round-trip efficiency
battery_degradation_rate = 0.02  # 2% degradation per year
hours_per_year = 8760  # Total hours in a year (365 * 24)
transmission_cost_per_kwh = 0.0871  # €/kWh for electricity transmission cost saved when using battery energy
selling_price_per_kwh = 0.10  # €/kWh for selling excess electricity back to the grid

# Investment costs
solar_panel_cost_per_kw = 1000  # €/kW for solar panel system
battery_costs = {
    5: 500 * 5,  # Cost for 5 kWh battery
    20: 400 * 20,  # Cost for 20 kWh battery
    100: 350 * 100  # Cost for 100 kWh battery
}
years = 5  # Operating period for calculating payback

# Assumptions for simulation
base_prices = {
    'winter': 0.20,  # Q1
    'spring': 0.10,  # Q2
    'summer': 0.08,  # Q3
    'autumn': 0.15   # Q4
}

# Function to generate hourly electricity prices
def generate_hourly_prices():
    prices = []
    seasons = ['winter', 'spring', 'summer', 'autumn']
    season_hours = [2159, 2184, 2184, 2233]  # Adjusted for exactly 8760 total hours
    daily_variations = [0.05, 0.03, 0.02, 0.04]

    for season, hours, daily_variation in zip(seasons, season_hours, daily_variations):
        base_price = base_prices[season]
        for hour in range(hours):
            hour_of_day = hour % 24
            if 6 <= hour_of_day < 18:  # Daytime (cheaper)
                price = base_price - daily_variation
            else:  # Nighttime (slightly more expensive)
                price = base_price + daily_variation
            prices.append(price)
    
    return np.array(prices[:hours_per_year])  # Ensure total length is 8760

# Function to generate hourly solar output
def generate_hourly_solar_output(solar_capacity):
    production = []
    seasons = ['winter', 'spring', 'summer', 'autumn']
    season_hours = [2159, 2184, 2184, 2233]  # Adjusted for exactly 8760 total hours
    avg_hours_by_season = [2, 5, 8, 4]
    variability_by_season = [0.1, 0.2, 0.3, 0.15]

    for season, hours, avg_hours, variability in zip(seasons, season_hours, avg_hours_by_season, variability_by_season):
        for hour in range(hours):
            hour_of_day = hour % 24
            if 6 <= hour_of_day < 18:  # Only during daylight hours
                daily_solar_output = solar_capacity * avg_hours / 12  # Average kWh production per hour of sunlight
                production.append(daily_solar_output * (1 + np.random.uniform(-variability, variability)))
            else:
                production.append(0)  # No production at night
    
    return np.array(production[:hours_per_year])  # Ensure total length is 8760

# Function to generate hourly consumption profile
def generate_hourly_consumption(annual_consumption):
    consumption = []
    seasons = ['winter', 'spring', 'summer', 'autumn']
    season_hours = [2159, 2184, 2184, 2233]  # Adjusted for exactly 8760 total hours
    season_share = [0.40, 0.20, 0.15, 0.25]
    daily_consumption_pattern = [0.5, 0.3, 0.2]  # Higher usage in morning, evening, low at night

    for season, hours, share in zip(seasons, season_hours, season_share):
        total_season_consumption = annual_consumption * share
        avg_hourly_consumption = total_season_consumption / hours  # Corrected hourly average
        
        for day in range(hours // 24):
            for hour in range(24):
                if 6 <= hour < 10:  # Morning peak
                    hourly_use = avg_hourly_consumption * daily_consumption_pattern[0]
                elif 18 <= hour < 22:  # Evening peak
                    hourly_use = avg_hourly_consumption * daily_consumption_pattern[1]
                else:  # Off-peak
                    hourly_use = avg_hourly_consumption * daily_consumption_pattern[2]
                consumption.append(hourly_use)
    
    if len(consumption) < hours_per_year:
        remaining_hours = hours_per_year - len(consumption)
        consumption.extend([avg_hourly_consumption] * remaining_hours)
    
    return np.array(consumption[:hours_per_year])  # Ensure total length is 8760

# Generate hourly prices for the simulation
hourly_prices = generate_hourly_prices()

# Function to simulate battery operation with solar panels
def simulate_battery_operation_with_solar(battery_capacity, hourly_data):
    battery_charge = 0  # Initial battery charge in kWh
    total_savings = 0  # Total savings including electricity cost and transmission cost savings
    electricity_cost_savings = 0
    transmission_cost_savings = 0
    selling_revenue = 0

    for index, row in hourly_data.iterrows():
        solar_production = row['Solar Production (kWh)']
        consumption = row['Consumption (kWh)']
        electricity_price = row['Electricity Price (€/kWh)']

        # Calculate excess solar energy (solar production minus consumption)
        solar_excess = max(0, solar_production - consumption)
        grid_demand = max(0, consumption - solar_production)

        # Step 1: Use solar production to meet immediate consumption
        if solar_production >= consumption:
            # All consumption is covered by solar; excess goes to battery
            if solar_excess > 0:
                charge_amount = min(battery_capacity - battery_charge, solar_excess)
                battery_charge += charge_amount
                solar_excess -= charge_amount
                # Savings on transmission cost by storing solar energy
                transmission_cost_savings += charge_amount * transmission_cost_per_kwh

            # Sell any remaining solar excess back to the grid
            if solar_excess > 0:
                selling_revenue += solar_excess * selling_price_per_kwh

        else:
            # Step 2: If solar is not enough, use battery to cover remaining consumption
            discharge_amount = min(battery_charge, grid_demand)
            battery_charge -= discharge_amount
            grid_demand -= discharge_amount
            # Savings on electricity cost by using battery instead of grid
            electricity_cost_savings += discharge_amount * electricity_price

            # Step 3: If there is still grid demand after using solar and battery, draw from the grid
            if grid_demand > 0:
                cost_with_battery = grid_demand * electricity_price
                cost_without_battery = consumption * electricity_price
                savings = cost_without_battery - cost_with_battery
                total_savings +=

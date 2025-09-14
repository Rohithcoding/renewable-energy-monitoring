import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

class RenewableEnergyDataGenerator:
    def __init__(self):
        self.energy_sources = ['Solar', 'Wind', 'Hydro', 'Biomass']
        
    def generate_historical_data(self, days=30):
        """Generate historical renewable energy data for the past n days"""
        end_date = datetime.now()
        start_date = end_date - timedelta(days=days)
        
        # Generate hourly data
        date_range = pd.date_range(start=start_date, end=end_date, freq='H')
        
        data = []
        for timestamp in date_range:
            hour = timestamp.hour
            
            # Simulate realistic patterns
            solar_base = max(0, 100 * np.sin((hour - 6) * np.pi / 12)) if 6 <= hour <= 18 else 0
            wind_base = 50 + 30 * np.sin(hour * np.pi / 12)
            hydro_base = 80 + 10 * np.sin(hour * np.pi / 24)
            biomass_base = 40 + 5 * np.sin(hour * np.pi / 6)
            
            # Add some randomness
            solar = max(0, solar_base + random.uniform(-20, 20))
            wind = max(0, wind_base + random.uniform(-15, 15))
            hydro = max(0, hydro_base + random.uniform(-10, 10))
            biomass = max(0, biomass_base + random.uniform(-5, 5))
            
            data.append({
                'timestamp': timestamp,
                'solar_kwh': round(solar, 2),
                'wind_kwh': round(wind, 2),
                'hydro_kwh': round(hydro, 2),
                'biomass_kwh': round(biomass, 2),
                'total_kwh': round(solar + wind + hydro + biomass, 2)
            })
        
        return pd.DataFrame(data)
    
    def generate_current_status(self):
        """Generate current status data for real-time monitoring"""
        current_time = datetime.now()
        hour = current_time.hour
        
        # Simulate current production
        solar_current = max(0, 100 * np.sin((hour - 6) * np.pi / 12)) if 6 <= hour <= 18 else 0
        solar_current += random.uniform(-10, 10)
        
        wind_current = 50 + 30 * np.sin(hour * np.pi / 12) + random.uniform(-10, 10)
        hydro_current = 80 + 10 * np.sin(hour * np.pi / 24) + random.uniform(-5, 5)
        biomass_current = 40 + 5 * np.sin(hour * np.pi / 6) + random.uniform(-3, 3)
        
        return {
            'timestamp': current_time,
            'solar': {'current_kwh': max(0, round(solar_current, 2)), 'efficiency': round(random.uniform(85, 95), 1)},
            'wind': {'current_kwh': max(0, round(wind_current, 2)), 'efficiency': round(random.uniform(80, 92), 1)},
            'hydro': {'current_kwh': max(0, round(hydro_current, 2)), 'efficiency': round(random.uniform(88, 96), 1)},
            'biomass': {'current_kwh': max(0, round(biomass_current, 2)), 'efficiency': round(random.uniform(75, 88), 1)},
            'total_current_kwh': round(max(0, solar_current) + max(0, wind_current) + max(0, hydro_current) + max(0, biomass_current), 2)
        }
    
    def generate_environmental_impact(self, total_kwh):
        """Calculate environmental impact metrics"""
        # Approximate CO2 emissions avoided (kg CO2 per kWh from fossil fuels)
        co2_avoided = round(total_kwh * 0.5, 2)  # 0.5 kg CO2 per kWh average
        
        # Equivalent homes powered (average home uses ~30 kWh/day)
        homes_powered = round(total_kwh / 30, 0)
        
        # Trees equivalent (1 tree absorbs ~22 kg CO2/year)
        trees_equivalent = round(co2_avoided / 22 * 365, 0)
        
        return {
            'co2_avoided_kg': co2_avoided,
            'homes_powered': int(homes_powered),
            'trees_equivalent': int(trees_equivalent)
        }
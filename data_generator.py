import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

class SolarEnergyDataGenerator:
    def __init__(self):
        self.energy_source = 'Solar'
        # Solar panel specifications
        self.panel_capacity_kw = 100  # Total solar panel capacity in kW
        self.num_panels = 400  # Number of solar panels
        self.panel_efficiency = 0.20  # Panel efficiency (20%)
        
    def generate_historical_data(self, days=30):
        """Generate historical solar energy data for the past n days"""
        end_date = datetime.now()
        start_date = end_date - timedelta(days=days)
        
        # Generate hourly data
        date_range = pd.date_range(start=start_date, end=end_date, freq='H')
        
        data = []
        for timestamp in date_range:
            hour = timestamp.hour
            month = timestamp.month
            day_of_year = timestamp.timetuple().tm_yday
            
            # Simulate realistic solar patterns
            # Base solar irradiance follows sun cycle
            if 6 <= hour <= 18:
                # Peak solar hours with bell curve
                solar_base = 100 * np.sin((hour - 6) * np.pi / 12)
                
                # Seasonal variation (higher in summer, lower in winter)
                seasonal_factor = 0.8 + 0.4 * np.sin((day_of_year - 80) * 2 * np.pi / 365)
                
                # Weather variation (clouds, rain, etc.)
                weather_factor = random.uniform(0.3, 1.0)
                
                # Panel temperature effect (efficiency drops at high temps)
                temp_factor = random.uniform(0.85, 1.0)
                
                solar_kwh = solar_base * seasonal_factor * weather_factor * temp_factor
                
                # Efficiency and panel degradation
                efficiency = self.panel_efficiency * random.uniform(0.95, 1.0)
                solar_kwh *= efficiency
                
            else:
                solar_kwh = 0  # No solar production at night
            
            # Additional solar metrics
            irradiance = max(0, solar_kwh * 10 + random.uniform(-50, 50))  # W/m²
            panel_temp = random.uniform(15, 75) if solar_kwh > 0 else random.uniform(5, 25)  # °C
            ambient_temp = random.uniform(10, 35)  # °C
            cloud_cover = max(0, min(100, 100 - (solar_kwh / 100) * 100 + random.uniform(-20, 20)))  # %
            
            data.append({
                'timestamp': timestamp,
                'solar_kwh': round(max(0, solar_kwh), 2),
                'irradiance_wm2': round(irradiance, 1),
                'panel_temp_c': round(panel_temp, 1),
                'ambient_temp_c': round(ambient_temp, 1),
                'cloud_cover_pct': round(cloud_cover, 1),
                'efficiency_pct': round(efficiency * 100, 2),
                'panels_active': random.randint(380, 400) if solar_kwh > 0 else 0
            })
        
        return pd.DataFrame(data)
    
    def generate_current_status(self):
        """Generate current solar status data for real-time monitoring"""
        current_time = datetime.now()
        hour = current_time.hour
        day_of_year = current_time.timetuple().tm_yday
        
        # Simulate current solar production
        if 6 <= hour <= 18:
            # Base solar production
            solar_base = 100 * np.sin((hour - 6) * np.pi / 12)
            
            # Seasonal variation
            seasonal_factor = 0.8 + 0.4 * np.sin((day_of_year - 80) * 2 * np.pi / 365)
            
            # Current weather conditions
            weather_factor = random.uniform(0.4, 1.0)
            temp_factor = random.uniform(0.85, 1.0)
            
            solar_current = solar_base * seasonal_factor * weather_factor * temp_factor
            efficiency = self.panel_efficiency * random.uniform(0.95, 1.0)
            solar_current *= efficiency
            
            # Current environmental conditions
            current_irradiance = max(0, solar_current * 10 + random.uniform(-50, 50))
            current_panel_temp = random.uniform(25, 75)
            current_ambient_temp = random.uniform(15, 35)
            current_cloud_cover = max(0, min(100, 100 - (solar_current / 100) * 100 + random.uniform(-20, 20)))
            panels_active = random.randint(385, 400)
            
        else:
            solar_current = 0
            current_irradiance = 0
            current_panel_temp = random.uniform(5, 20)
            current_ambient_temp = random.uniform(5, 20)
            current_cloud_cover = random.uniform(0, 100)
            panels_active = 0
            efficiency = 0
        
        return {
            'timestamp': current_time,
            'current_kwh': round(max(0, solar_current), 2),
            'efficiency_pct': round(efficiency * 100, 2) if efficiency > 0 else 0,
            'irradiance_wm2': round(current_irradiance, 1),
            'panel_temp_c': round(current_panel_temp, 1),
            'ambient_temp_c': round(current_ambient_temp, 1),
            'cloud_cover_pct': round(current_cloud_cover, 1),
            'panels_active': panels_active,
            'total_panels': self.num_panels,
            'system_capacity_kw': self.panel_capacity_kw
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
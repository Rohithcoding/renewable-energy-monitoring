# ☀️ Solar Energy Monitoring Dashboard

A comprehensive real-time dashboard for monitoring solar energy production and performance. Built with Python, Streamlit, and Plotly for interactive data visualization and detailed solar analytics.

## 🌟 Features

- **Real-time Solar Monitoring**: Live status of solar panel system performance
- **Historical Solar Analysis**: Interactive charts showing solar production trends
- **Environmental Impact**: Calculate CO₂ avoided from solar energy production
- **Solar Performance Analytics**: Track panel efficiency, irradiance, and temperature effects
- **Weather Correlation**: Analyze how weather conditions affect solar output
- **System Health Monitoring**: Track active panels and system capacity
- **Interactive Visualizations**: Time series, scatter plots, bar charts, and real-time metrics
- **Responsive Design**: Works on desktop and mobile devices

## 📊 Dashboard Sections

1. **Live Solar Status**: Real-time solar production, irradiance, temperature, and system health
2. **Historical Solar Trends**: Time series analysis of solar energy production over time
3. **Solar Analytics**: Hourly production patterns and daily solar output trends
4. **Weather Correlation**: Solar production vs irradiance and temperature vs efficiency charts
5. **Environmental Impact**: CO₂ reduction and environmental benefits from solar energy
6. **Performance Analytics**: Solar system efficiency, peak production, and irradiance metrics

## 🚀 Quick Start

### Local Development

1. **Clone the repository**
   ```bash
   git clone https://github.com/Rohithcoding/renewable-energy-monitoring.git
   cd renewable-energy-monitoring
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   streamlit run app.py
   ```

4. **Open your browser**
   Navigate to `http://localhost:8501` to view the dashboard

## 🌐 Deployment Options

### Option 1: Streamlit Community Cloud (Recommended)

1. **Fork this repository** to your GitHub account
2. **Visit** [share.streamlit.io](https://share.streamlit.io)
3. **Connect your GitHub account**
4. **Deploy** by selecting your repository
5. **Your app will be live** at `https://your-app-name.streamlit.app`

### Option 2: Heroku

1. **Install Heroku CLI** and login
   ```bash
   heroku login
   ```

2. **Create a new Heroku app**
   ```bash
   heroku create your-app-name
   ```

3. **Deploy to Heroku**
   ```bash
   git add .
   git commit -m "Deploy renewable energy dashboard"
   git push heroku main
   ```

### Option 3: Railway

1. **Connect your GitHub repository** to Railway
2. **Deploy directly** from the Railway dashboard
3. **Your app will be automatically deployed** with a custom URL

## 📱 Demo

### Live Demo Features:
- **Real-time data simulation** with realistic energy production patterns
- **Interactive controls** to adjust historical data timeframe
- **Environmental impact calculations** showing real-world benefits
- **Responsive design** that works on all devices

### Sample Data:
- **Solar Production**: Peak production during daylight hours (6 AM - 6 PM) with realistic sun cycle patterns
- **Weather Conditions**: Simulated cloud cover, temperature variations, and seasonal effects
- **Panel Performance**: Efficiency variations based on temperature and irradiance levels
- **System Health**: Active panel counts and system capacity monitoring
- **Environmental Factors**: Ambient temperature, panel temperature, and solar irradiance data

## 🛠️ Technical Stack

- **Frontend**: Streamlit
- **Data Processing**: Pandas, NumPy
- **Visualizations**: Plotly
- **Backend**: Python 3.8+
- **Deployment**: Streamlit Cloud, Heroku, Railway

## 📋 Requirements

```
streamlit==1.28.1
pandas==2.1.1
numpy==1.24.3
plotly==5.17.0
python-dateutil==2.8.2
```

## 🔧 Configuration

### Environment Variables
- No environment variables required for basic operation
- All data is generated using realistic simulation algorithms

### Customization
- Modify `data_generator.py` to connect to real energy monitoring APIs
- Adjust time ranges and refresh intervals in `app.py`
- Customize themes in `.streamlit/config.toml`

## 📈 Data Sources

Currently uses simulated data that mimics real solar energy patterns:
- **Solar Production**: Follows realistic sun cycle with seasonal variations
- **Weather Data**: Simulated irradiance, cloud cover, and temperature effects
- **Panel Performance**: Efficiency variations based on temperature and environmental conditions
- **System Status**: Panel health monitoring and capacity tracking

### Connecting Real Data
To connect real solar data sources, modify the `SolarEnergyDataGenerator` class:
```python
# Replace simulation with real solar API calls
def get_real_solar_data():
    # Connect to solar inverter APIs or weather services
    # Examples: SolarEdge API, Enphase API, OpenWeatherMap
    pass
```

## 🌍 Environmental Impact Calculations

- **CO₂ Avoided**: Based on 0.5 kg CO₂ per kWh from fossil fuels
- **Homes Powered**: Average home consumption of 30 kWh per day
- **Tree Equivalent**: 22 kg CO₂ absorption per tree per year

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👤 Author

**Rohith Kumar**
- GitHub: [@Rohithcoding](https://github.com/Rohithcoding)
- Project: Solar Energy Monitoring Dashboard

## 🙏 Acknowledgments

- Streamlit community for the amazing framework
- Plotly for interactive visualizations
- Renewable energy community for inspiration

## 📞 Support

If you have any questions or need help with deployment, please:
1. Check the [Issues](https://github.com/Rohithcoding/renewable-energy-monitoring/issues) page
2. Create a new issue with your question
3. Include your deployment platform and error details

---

**☀️ Monitor and optimize your solar energy production with this dashboard! 🌍**

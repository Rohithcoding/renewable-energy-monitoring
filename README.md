# 🌱 Renewable Energy Monitoring Dashboard

A comprehensive real-time dashboard for monitoring renewable energy production from multiple sources including Solar, Wind, Hydro, and Biomass. Built with Python, Streamlit, and Plotly for interactive data visualization.

## 🌟 Features

- **Real-time Monitoring**: Live status of all renewable energy sources
- **Historical Analysis**: Interactive charts showing energy production trends
- **Environmental Impact**: Calculate CO₂ avoided, homes powered, and tree equivalents
- **Performance Analytics**: Track efficiency, peak production, and daily averages
- **Interactive Visualizations**: Time series, pie charts, bar charts, and metrics
- **Responsive Design**: Works on desktop and mobile devices

## 📊 Dashboard Sections

1. **Live Status**: Current production and efficiency for each energy source
2. **Historical Trends**: Time series analysis of energy production
3. **Energy Mix**: Pie chart breakdown of energy sources
4. **Daily Production**: Stacked bar chart of the last 7 days
5. **Environmental Impact**: CO₂ reduction and environmental benefits
6. **Performance Analytics**: System efficiency and production statistics

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
- **Solar**: Peak production during daylight hours (6 AM - 6 PM)
- **Wind**: Variable production with realistic wind patterns
- **Hydro**: Consistent baseline production with minor variations
- **Biomass**: Steady production with scheduled maintenance periods

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

Currently uses simulated data that mimics real renewable energy patterns:
- **Solar**: Follows sun cycle with weather variations
- **Wind**: Variable production with seasonal patterns
- **Hydro**: Consistent flow with reservoir management
- **Biomass**: Steady production with maintenance schedules

### Connecting Real Data
To connect real data sources, modify the `RenewableEnergyDataGenerator` class:
```python
# Replace simulation with API calls
def get_real_solar_data():
    # Your API integration here
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
- Project: Renewable Energy Monitoring Dashboard

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

**🌱 Help monitor and promote renewable energy adoption with this dashboard! 🌍**
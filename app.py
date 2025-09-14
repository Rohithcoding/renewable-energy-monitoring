import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
from data_generator import SolarEnergyDataGenerator

# Page configuration
st.set_page_config(
    page_title="Solar Energy Monitoring Dashboard",
    page_icon="☀️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize data generator
@st.cache_data
def load_data(days=30):
    generator = SolarEnergyDataGenerator()
    return generator.generate_historical_data(days)

def get_current_status():
    generator = SolarEnergyDataGenerator()
    return generator.generate_current_status()

def calculate_environmental_impact(total_kwh):
    generator = SolarEnergyDataGenerator()
    return generator.generate_environmental_impact(total_kwh)

# Main app
def main():
    st.title("☀️ Solar Energy Monitoring Dashboard")
    st.markdown("Real-time monitoring and analysis of solar energy production")
    
    # Sidebar
    st.sidebar.header("Dashboard Controls")
    days_to_show = st.sidebar.slider("Historical Data (days)", 7, 90, 30)
    auto_refresh = st.sidebar.checkbox("Auto Refresh", value=True)
    
    if auto_refresh:
        st.sidebar.info("Dashboard refreshes every 30 seconds")
        # Auto refresh every 30 seconds
        import time
        time.sleep(0.1)  # Small delay for demo purposes
    
    # Load data
    df = load_data(days_to_show)
    current_status = get_current_status()
    
    # Current Status Section
    st.header("☀️ Live Solar Status")
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        st.metric(
            "⚡ Power Output",
            f"{current_status['current_kwh']} kWh",
            "Current Production"
        )
    
    with col2:
        st.metric(
            "🔆 Solar Irradiance",
            f"{current_status['irradiance_wm2']} W/m²",
            "Current Sunlight"
        )
    
    with col3:
        st.metric(
            "🌡️ Panel Temperature",
            f"{current_status['panel_temp_c']}°C",
            f"Ambient: {current_status['ambient_temp_c']}°C"
        )
    
    with col4:
        st.metric(
            "☁️ Cloud Cover",
            f"{current_status['cloud_cover_pct']}%",
            "Weather Conditions"
        )
    
    with col5:
        st.metric(
            "🔋 System Status",
            f"{current_status['panels_active']}/{current_status['total_panels']}",
            "Panels Active"
        )
    
    # Historical Trends
    st.header("📊 Historical Solar Production")
    
    # Time series chart for solar production
    fig_timeline = go.Figure()
    
    fig_timeline.add_trace(go.Scatter(
        x=df['timestamp'], y=df['solar_kwh'],
        mode='lines', name='Solar Production', line=dict(color='#FFA500', width=3),
        fill='tonexty', fillcolor='rgba(255, 165, 0, 0.1)'
    ))
    
    fig_timeline.update_layout(
        title="Solar Energy Production Over Time",
        xaxis_title="Time",
        yaxis_title="Solar Production (kWh)",
        hovermode='x',
        showlegend=False,
        height=400
    )
    
    st.plotly_chart(fig_timeline, use_container_width=True)
    
    # Solar conditions correlation charts
    col1, col2 = st.columns(2)
    
    with col1:
        # Solar irradiance vs production
        fig_irradiance = px.scatter(
            df, x='irradiance_wm2', y='solar_kwh',
            title='Solar Production vs Irradiance',
            labels={'irradiance_wm2': 'Solar Irradiance (W/m²)', 'solar_kwh': 'Solar Production (kWh)'},
            color='solar_kwh', color_continuous_scale='Oranges'
        )
        st.plotly_chart(fig_irradiance, use_container_width=True)
    
    with col2:
        # Temperature vs efficiency
        fig_temp = px.scatter(
            df, x='panel_temp_c', y='efficiency_pct',
            title='Panel Efficiency vs Temperature',
            labels={'panel_temp_c': 'Panel Temperature (°C)', 'efficiency_pct': 'Efficiency (%)'},
            color='efficiency_pct', color_continuous_scale='RdYlBu_r'
        )
        st.plotly_chart(fig_temp, use_container_width=True)
    
    # Solar analytics breakdown
    st.header("🔍 Solar System Analytics")
    col1, col2 = st.columns(2)
    
    with col1:
        # Hourly production pattern
        df['hour'] = df['timestamp'].dt.hour
        hourly_avg = df.groupby('hour')['solar_kwh'].mean().reset_index()
        
        fig_hourly = px.bar(
            hourly_avg, x='hour', y='solar_kwh',
            title="Average Solar Production by Hour",
            labels={'hour': 'Hour of Day', 'solar_kwh': 'Average Production (kWh)'},
            color='solar_kwh', color_continuous_scale='Oranges'
        )
        fig_hourly.update_layout(showlegend=False)
        st.plotly_chart(fig_hourly, use_container_width=True)
    
    with col2:
        # Daily totals bar chart
        df['date'] = df['timestamp'].dt.date
        daily_totals = df.groupby('date')['solar_kwh'].sum().reset_index()
        daily_totals = daily_totals.tail(7)  # Last 7 days
        
        fig_daily = px.bar(
            daily_totals, x='date', y='solar_kwh',
            title='Daily Solar Production (Last 7 Days)',
            labels={'date': 'Date', 'solar_kwh': 'Solar Production (kWh)'},
            color='solar_kwh', color_continuous_scale='Oranges'
        )
        fig_daily.update_layout(showlegend=False)
        st.plotly_chart(fig_daily, use_container_width=True)
    
    # Environmental Impact
    st.header("🌍 Environmental Impact")
    total_solar_energy = df['solar_kwh'].sum()
    impact = calculate_environmental_impact(total_solar_energy)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric(
            "🌳 CO₂ Avoided",
            f"{impact['co2_avoided_kg']:,} kg",
            "From solar energy"
        )
    
    with col2:
        st.metric(
            "🏠 Homes Powered",
            f"{impact['homes_powered']:,}",
            "Daily equivalent"
        )
    
    with col3:
        st.metric(
            "🌲 Trees Equivalent",
            f"{impact['trees_equivalent']:,}",
            "Annual CO₂ absorption"
        )
    
    # Performance Analytics
    st.header("📈 Solar Performance Analytics")
    
    # Calculate solar-specific metrics
    avg_daily_production = df.groupby(df['timestamp'].dt.date)['solar_kwh'].sum().mean()
    peak_production = df['solar_kwh'].max()
    peak_time = df.loc[df['solar_kwh'].idxmax(), 'timestamp']
    avg_efficiency = df['efficiency_pct'].mean()
    avg_irradiance = df[df['solar_kwh'] > 0]['irradiance_wm2'].mean()
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(
            "📊 Avg Daily Production",
            f"{avg_daily_production:.1f} kWh",
            "Solar energy per day"
        )
    
    with col2:
        st.metric(
            "🎯 Peak Production",
            f"{peak_production:.1f} kWh",
            f"at {peak_time.strftime('%H:%M')}"
        )
    
    with col3:
        st.metric(
            "⚡ System Efficiency",
            f"{avg_efficiency:.1f}%",
            "Average panel efficiency"
        )
    
    with col4:
        st.metric(
            "🔆 Avg Irradiance",
            f"{avg_irradiance:.0f} W/m²",
            "During daylight hours"
        )
    
    # Data table
    with st.expander("📋 Solar Data (Latest 100 records)"):
        # Display relevant solar columns
        display_df = df[['timestamp', 'solar_kwh', 'irradiance_wm2', 'panel_temp_c', 
                        'ambient_temp_c', 'cloud_cover_pct', 'efficiency_pct', 'panels_active']].tail(100)
        st.dataframe(display_df, use_container_width=True)
    
    # Footer
    st.markdown("---")
    st.markdown("*Dashboard last updated: {}*".format(datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

if __name__ == "__main__":
    main()
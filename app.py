import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
from data_generator import RenewableEnergyDataGenerator

# Page configuration
st.set_page_config(
    page_title="Renewable Energy Monitoring Dashboard",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize data generator
@st.cache_data
def load_data(days=30):
    generator = RenewableEnergyDataGenerator()
    return generator.generate_historical_data(days)

def get_current_status():
    generator = RenewableEnergyDataGenerator()
    return generator.generate_current_status()

def calculate_environmental_impact(total_kwh):
    generator = RenewableEnergyDataGenerator()
    return generator.generate_environmental_impact(total_kwh)

# Main app
def main():
    st.title("🌱 Renewable Energy Monitoring Dashboard")
    st.markdown("Real-time monitoring and analysis of renewable energy production")
    
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
    st.header("🔴 Live Status")
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        st.metric(
            "☀️ Solar",
            f"{current_status['solar']['current_kwh']} kWh",
            f"{current_status['solar']['efficiency']}% efficiency"
        )
    
    with col2:
        st.metric(
            "💨 Wind",
            f"{current_status['wind']['current_kwh']} kWh",
            f"{current_status['wind']['efficiency']}% efficiency"
        )
    
    with col3:
        st.metric(
            "💧 Hydro",
            f"{current_status['hydro']['current_kwh']} kWh",
            f"{current_status['hydro']['efficiency']}% efficiency"
        )
    
    with col4:
        st.metric(
            "🌾 Biomass",
            f"{current_status['biomass']['current_kwh']} kWh",
            f"{current_status['biomass']['efficiency']}% efficiency"
        )
    
    with col5:
        st.metric(
            "⚡ Total Current",
            f"{current_status['total_current_kwh']} kWh",
            "Live Production"
        )
    
    # Historical Trends
    st.header("📊 Historical Energy Production")
    
    # Time series chart
    fig_timeline = go.Figure()
    
    fig_timeline.add_trace(go.Scatter(
        x=df['timestamp'], y=df['solar_kwh'],
        mode='lines', name='Solar', line=dict(color='#FFA500', width=2)
    ))
    fig_timeline.add_trace(go.Scatter(
        x=df['timestamp'], y=df['wind_kwh'],
        mode='lines', name='Wind', line=dict(color='#87CEEB', width=2)
    ))
    fig_timeline.add_trace(go.Scatter(
        x=df['timestamp'], y=df['hydro_kwh'],
        mode='lines', name='Hydro', line=dict(color='#4682B4', width=2)
    ))
    fig_timeline.add_trace(go.Scatter(
        x=df['timestamp'], y=df['biomass_kwh'],
        mode='lines', name='Biomass', line=dict(color='#8FBC8F', width=2)
    ))
    
    fig_timeline.update_layout(
        title="Energy Production Over Time",
        xaxis_title="Time",
        yaxis_title="Energy Production (kWh)",
        hovermode='x unified',
        showlegend=True,
        height=400
    )
    
    st.plotly_chart(fig_timeline, use_container_width=True)
    
    # Energy source breakdown
    col1, col2 = st.columns(2)
    
    with col1:
        # Pie chart for energy mix
        recent_data = df.tail(24)  # Last 24 hours
        energy_totals = {
            'Solar': recent_data['solar_kwh'].sum(),
            'Wind': recent_data['wind_kwh'].sum(),
            'Hydro': recent_data['hydro_kwh'].sum(),
            'Biomass': recent_data['biomass_kwh'].sum()
        }
        
        fig_pie = px.pie(
            values=list(energy_totals.values()),
            names=list(energy_totals.keys()),
            title="Energy Mix (Last 24 Hours)",
            color_discrete_sequence=['#FFA500', '#87CEEB', '#4682B4', '#8FBC8F']
        )
        st.plotly_chart(fig_pie, use_container_width=True)
    
    with col2:
        # Daily totals bar chart
        df['date'] = df['timestamp'].dt.date
        daily_totals = df.groupby('date')[['solar_kwh', 'wind_kwh', 'hydro_kwh', 'biomass_kwh']].sum().reset_index()
        daily_totals = daily_totals.tail(7)  # Last 7 days
        
        fig_bar = go.Figure()
        fig_bar.add_trace(go.Bar(name='Solar', x=daily_totals['date'], y=daily_totals['solar_kwh'], marker_color='#FFA500'))
        fig_bar.add_trace(go.Bar(name='Wind', x=daily_totals['date'], y=daily_totals['wind_kwh'], marker_color='#87CEEB'))
        fig_bar.add_trace(go.Bar(name='Hydro', x=daily_totals['date'], y=daily_totals['hydro_kwh'], marker_color='#4682B4'))
        fig_bar.add_trace(go.Bar(name='Biomass', x=daily_totals['date'], y=daily_totals['biomass_kwh'], marker_color='#8FBC8F'))
        
        fig_bar.update_layout(
            title='Daily Energy Production (Last 7 Days)',
            xaxis_title='Date',
            yaxis_title='Energy Production (kWh)',
            barmode='stack'
        )
        st.plotly_chart(fig_bar, use_container_width=True)
    
    # Environmental Impact
    st.header("🌍 Environmental Impact")
    total_energy = df['total_kwh'].sum()
    impact = calculate_environmental_impact(total_energy)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric(
            "🌳 CO₂ Avoided",
            f"{impact['co2_avoided_kg']:,} kg",
            "Carbon footprint reduction"
        )
    
    with col2:
        st.metric(
            "🏠 Homes Powered",
            f"{impact['homes_powered']:,}",
            "Equivalent homes per day"
        )
    
    with col3:
        st.metric(
            "🌲 Trees Equivalent",
            f"{impact['trees_equivalent']:,}",
            "Annual CO₂ absorption"
        )
    
    # Performance Analytics
    st.header("📈 Performance Analytics")
    
    # Calculate averages and trends
    avg_daily_production = df.groupby(df['timestamp'].dt.date)['total_kwh'].sum().mean()
    peak_production = df['total_kwh'].max()
    peak_time = df.loc[df['total_kwh'].idxmax(), 'timestamp']
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric(
            "📊 Avg Daily Production",
            f"{avg_daily_production:.1f} kWh",
            "Per day average"
        )
    
    with col2:
        st.metric(
            "🎯 Peak Production",
            f"{peak_production:.1f} kWh",
            f"at {peak_time.strftime('%H:%M on %m/%d')}"
        )
    
    with col3:
        efficiency_avg = (
            current_status['solar']['efficiency'] +
            current_status['wind']['efficiency'] +
            current_status['hydro']['efficiency'] +
            current_status['biomass']['efficiency']
        ) / 4
        st.metric(
            "⚡ System Efficiency",
            f"{efficiency_avg:.1f}%",
            "Overall system performance"
        )
    
    # Data table
    with st.expander("📋 Raw Data (Latest 100 records)"):
        st.dataframe(df.tail(100), use_container_width=True)
    
    # Footer
    st.markdown("---")
    st.markdown("*Dashboard last updated: {}*".format(datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

if __name__ == "__main__":
    main()
import streamlit as st
import pandas as pd
import plotly.express as px

# Define data URL
DATA_URL = 'https://raw.githubusercontent.com/randalnabout/streamlit/main/2019.csv'

# Load the data from the URL
data = pd.read_csv(DATA_URL)

def main():
    st.title("World Happiness Report")

    st.header("Introduction")
    st.write("Welcome to the World Happiness Report app. This app visualizes data from the 2019 World Happiness Report.")
    st.write("You can explore the happiness scores, GDP per capita, and more by placing the mouse on the country of interest.")

    st.subheader("Data Exploration")

    # Filter by region
    selected_region = st.selectbox("Select a Region", data["Region"].unique())

    # Filter by happiness score range
    min_score = st.slider("Minimum Happiness Score", min_value=data["Score"].min(), max_value=data["Score"].max())
    max_score = st.slider("Maximum Happiness Score", min_value=min_score, max_value=data["Score"].max())

    # Filter by GDP per capita range
    min_gdp = st.slider("Minimum GDP per Capita", min_value=data["GDP per capita"].min(), max_value=data["GDP per capita"].max())
    max_gdp = st.slider("Maximum GDP per Capita", min_value=min_gdp, max_value=data["GDP per capita"].max())

    # Apply the selected filters to the data
    filtered_data = data[(data["Region"] == selected_region) &
                        (data["Score"] >= min_score) & (data["Score"] <= max_score) &
                        (data["GDP per capita"] >= min_gdp) & (data["GDP per capita"] <= max_gdp)]

    st.write("Filtered Data:")
    st.dataframe(filtered_data)

    st.subheader("Visualization 1: World Happiness Map")
    st.write("This map shows the happiness scores of different countries on the world map. Hover over countries to see details.")

    fig5 = px.scatter_geo(filtered_data,
                         locations="Country or region",
                         locationmode="country names",
                         color="Score",
                         hover_name="Country or region",
                         size="GDP per capita",
                         projection="natural earth",
                         title="World Happiness Report",
                         hover_data={"Country or region": True, "Score": ":.2f", "GDP per capita": ":.2f"})

    fig5.update_geos(showcoastlines=True, coastlinecolor="Black", showland=True, landcolor="white", showocean=True, oceancolor="lightblue")

    fig5.update_layout(geo=dict(showframe=False, showcoastlines=False))

    st.plotly_chart(fig5)

    # Visualization Customization
    st.subheader("Visualization Customization")
    st.write("Customize the chart:")
    
    chart_type = st.selectbox("Select Chart Type", ["Scatter Plot", "Bar Chart", "Line Chart"])
   
    if chart_type == "Scatter Plot":
        # Display the scatter plot
        fig = px.scatter(filtered_data, x="GDP per capita", y="Score", title="Scatter Plot")
    elif chart_type == "Bar Chart":
        # Display the bar chart
        fig = px.bar(filtered_data, x="Country or region", y="Score", title="Bar Chart")
    else:
        # Display the line chart
        fig = px.line(filtered_data, x="Country or region", y="GDP per capita", title="Line Chart")

    st.plotly_chart(fig)

if __name__ == "__main__":
    main()


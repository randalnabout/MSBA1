import streamlit as st
import pandas as pd
import plotly.express as px

# Define data URL
DATA_URL = 'https://raw.githubusercontent.com/randalnabout/streamlit/main/2019.csv'

# Load the data from the URL
data = pd.read_csv(DATA_URL)

def main():
    st.title("World Happiness Report")

    st.header("Assignment MSBA 325 - Data Visualization")
    st.write("Welcome to the World Happiness Report app. Explore the 2019 World Happiness data by filtering and visualizing it.")
    st.write("Hover over countries to view happiness scores and GDP per capita.")

    # Filter by Happiness Score
    st.subheader("Filter by Happiness Score")
    min_score = st.slider("Minimum Happiness Score:", min_value=0.0, max_value=10.0, step=0.1, value=0.0)
    max_score = st.slider("Maximum Happiness Score:", min_value=0.0, max_value=10.0, step=0.1, value=10.0)

    filtered_data = data[(data['Score'] >= min_score) & (data['Score'] <= max_score)

    # World Happiness Map
    st.write("This map displays happiness scores and GDP per capita by country.")
    
    fig5 = px.scatter_geo(filtered_data,
                         locations="Country or region",
                         locationmode="country names",
                         color="Score",
                         hover_name="Country or region",
                         hover_data=["Score", "GDP per capita"],
                         size="GDP per capita",
                         projection="natural earth",
                         title="World Happiness Report",
                         color_continuous_scale=px.colors.sequential.Plasma,
                         range_color=(0, 10))

    fig5.update_geos(showcoastlines=True, coastlinecolor="Black", showland=True, landcolor="white", showocean=True, oceancolor="lightblue")
    fig5.update_layout(geo=dict(showframe=False, showcoastlines=False))

    st.plotly_chart(fig5)

    # Happiness Score vs. GDP per Capita
    st.subheader("Visualization 2: Happiness Score vs. GDP per Capita")
    st.write("This scatter plot visualizes the relationship between happiness score and GDP per capita.")
    
    fig6 = px.scatter(data_frame=filtered_data, x="GDP per capita", y="Score", animation_frame="Overall rank",
                     size="Score", color="Country or region", hover_name="Country or region",
                     title="Happiness Score vs. GDP per Capita (Filtered Countries)")

    fig6.update_layout(xaxis=dict(range=[1.2, 1.6]), yaxis=dict(range=[2, 8]))

    st.plotly_chart(fig6)

    # Find a Matching Country
    st.subheader("Quote of the Day: 'WHAT IS COMING IS BETTER THAN WHAT IS GONE!'")
    st.subheader("Find a Country Matching Your Happiness Score")
    user_happiness_score = st.number_input("Enter your happiness score (0-10):", min_value=0.0, max_value=10.0, step=0.1)

    if st.button("Find Matching Country"):
        closest_country = filtered_data.iloc[(filtered_data['Score'] - user_happiness_score).abs().argsort()[:1]]
        st.write(f"The closest matching country to your happiness score of {user_happiness_score} is: {closest_country['Country or region'].values[0]}")

if __name__ == "__main__":
    main()

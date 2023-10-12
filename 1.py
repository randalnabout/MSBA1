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

    st.sidebar.title("Control Panel")
    
    st.sidebar.subheader("Your Happiness Percentage")
    user_happiness = st.sidebar.slider("On a scale from 1 to 100, how happy are you?", min_value=1, max_value=100)
    
    st.subheader("Visualization 1: World Happiness Map")
    st.write("This map shows the happiness scores of different countries on the world map.")
    
    fig5 = px.scatter_geo(data,
                         locations="Country or region",
                         locationmode="country names",
                         color="Score",
                         hover_name="Country or region",
                         size="GDP per capita",
                         projection="natural earth",
                         title="World Happiness Report")

    fig5.update_geos(showcoastlines=True, coastlinecolor="Black", showland=True, landcolor="white", showocean=True, oceancolor="lightblue")
    fig5.update_layout(geo=dict(showframe=False, showcoastlines=False))
    st.plotly_chart(fig5)

    st.subheader("Find Country by Rank")
    st.write("Enter a rank to find the corresponding country:")
    rank = st.number_input("Enter a Rank", min_value=1, max_value=data["Overall rank"].max())

    if st.button("Find Country"):
        selected_data = data[data["Overall rank"] == rank]
        if not selected_data.empty:
            country = selected_data.iloc[0]["Country or region"]
            st.write(f"Country at Rank {rank}: {country}")
        else:
            st.write(f"No country found at Rank {rank}.")

    st.sidebar.subheader("Find Similar Happiness Country")
    st.write("See which country in the World Happiness Report is most similar to your happiness percentage.")
    
    # Calculate the absolute difference between user's happiness and each country's happiness
    data["Difference"] = abs(data["Score"] - (user_happiness / 100))
    
    # Find the country with the smallest difference
    similar_country = data.loc[data["Difference"].idxmin()]["Country or region"]
    
    st.sidebar.write(f"You are similar in happiness to the population of {similar_country} in the World Happiness Report.")

if __name__ == "__main__":
    main()

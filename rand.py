import streamlit as st
import pandas as pd
import plotly.express as px

# Define data URL
DATA_URL = 'https://raw.githubusercontent.com/randalnabout/streamlit/main/2019.csv'

# Load the data from the URL
data = pd.read_csv(DATA_URL)

def main():
    st.title("World Happiness Report")

    st.header("Hello! This page is part of an assignment for MSBA 325. Data visualization.")
    st.write("Welcome to the World Happiness Report app. This app visualizes data from the 2019 World Happiness Report.")
    st.write("You can explore the happiness scores, GDP per capita, and more by placing the mouse on the country of interest.")

    st.sidebar.title("Map Layers")  # Moved the sidebar title here

    st.sidebar.subheader("Visualization 1: World Happiness Map")
    st.sidebar.write("This map shows the happiness scores of different countries on the world map.")
    
    # Create a sidebar for the control panel
    with st.sidebar:
        # Interactive widget to select the column for color coding
        color_column = st.selectbox("Select a Column for Color Coding", data.columns[2:])

    fig5 = px.scatter_geo(data,
                         locations="Country or region",
                         locationmode="country names",
                         color=color_column,  # Color based on user selection
                         hover_name="Country or region",
                         size="GDP per capita",
                         projection="natural earth",
                         title="World Happiness Report")

    fig5.update_geos(showcoastlines=True, coastlinecolor="Black", showland=True, landcolor="white", showocean=True, oceancolor="lightblue")

    fig5.update_layout(geo=dict(showframe=False, showcoastlines=False))

    # Customize the hover effect to highlight the country
    fig5.update_traces(marker=dict(line=dict(width=2, color='DarkSlateGrey')),
                      selector=dict(mode='markers+text'))

    st.plotly_chart(fig5)

    fig6 = px.scatter(data_frame=data, x="GDP per capita", y="Score", animation_frame="Overall rank",
                     size="Score", color="Country or region", hover_name="Country or region",
                     title="Happiness Score vs. GDP per Capita (All Countries)")

    fig6.update_layout(xaxis=dict(range=[1.2, 1.6]), yaxis=dict(range=[2, 8]))

    st.plotly_chart(fig6)

    st.sidebar.subheader("Find Country by Rank")
    st.sidebar.write("Enter a rank to find the corresponding country:")
    rank = st.sidebar.number_input("Enter a Rank", min_value=1, max_value=data["Overall rank"].max())
    
    if st.sidebar.button("Find Country"):
        selected_data = data[data["Overall rank"] == rank]
        if not selected_data.empty:
            country = selected_data.iloc[0]["Country or region"]
            st.sidebar.write(f"Country at Rank {rank}: {country}")
        else:
            st.sidebar.write(f"No country found at Rank {rank}")

    st.header("Your Happiness Rank")
    st.write("Please enter your happiness rank on a scale of 1-10:")
    user_rank = st.number_input("Enter Your Rank", min_value=1, max_value=10)
    
    if st.button("See Your Rank Compared to World Happiness"):
        st.subheader("Your Happiness Rank Compared to World Happiness Report")
        st.write(f"Your happiness rank: {user_rank}")
        st.write(f"World Happiness Report rank: {rank}")
        if user_rank > rank:
            st.write("You are happier than the country at this rank.")
        elif user_rank < rank:
            st.write("You are less happy than the country at this rank.")
        else:
            st.write("You are equally happy as the country at this rank.")


if __name__ == "__main__":
    main()

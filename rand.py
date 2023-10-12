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

    # Modify Figure 5
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

# ...

fig6 = px.scatter(data_frame=filtered_data, x="GDP per capita", y="Score", animation_frame="Overall rank",
                 size="Score", color="Country or region", hover_name="Country or region",
                 title="Happiness Score vs. GDP per Capita (All Countries)")

fig6.update_layout(xaxis=dict(range=[1.2, 1.6]), yaxis=dict(range=[2, 8]))

st.plotly_chart(fig6)

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

if __name__ == "__main__":
    main()


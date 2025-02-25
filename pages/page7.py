import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Sample Data: Best Picture winners from 2010 to 2023 (Replace with actual data if needed)
data = {
    "Year": list(range(2010, 2024)),
    "Movie": [
        "The Hurt Locker", "The King's Speech", "The Artist", "Argo", "12 Years a Slave", "Birdman",
        "Spotlight", "Moonlight", "The Shape of Water", "Green Book", "Parasite", "Nomadland",
        "CODA", "Everything Everywhere All at Once"
    ]
}

# Convert data into DataFrame
df = pd.DataFrame(data)

# Streamlit App
st.title("Oscar's Best Picture Winners Over the Years")

# Plotting
fig, ax = plt.subplots()
ax.plot(df["Year"], range(len(df)), marker='o', linestyle='-', color='b')
ax.set_xticks(df["Year"])
ax.set_yticks(range(len(df)))
ax.set_yticklabels(df["Movie"], fontsize=8)
ax.set_xlabel("Year")
ax.set_ylabel("Best Picture Winner")
ax.set_title("Oscar Best Picture Winners Timeline")
plt.xticks(rotation=45)
plt.grid()

# Show plot
st.pyplot(fig)

import streamlit as st
import plotly.graph_objects as go
import numpy as np

# Given Data
temperature = np.array([25, 26, 27, 28, 29, 30, 31])
dc_power = np.array([213.9, 210.9, 202.1, 206.7, 209.9, 194.69, 200.27])

st.title("DC Power vs Temperature Simulation")

# Interactive temperature slider
temp_input = st.slider("Select Temperature (°C)", min_value=25, max_value=31, value=28)
selected_power = np.interp(temp_input, temperature, dc_power)

# Display Output
st.write(f"Predicted DC Power at {temp_input}°C: **{selected_power:.2f} W**")

# Create interactive plot
fig = go.Figure()
fig.add_trace(go.Scatter(x=temperature, y=dc_power, mode='markers+lines', name='DC Power'))
fig.add_trace(go.Scatter(x=[temp_input], y=[selected_power], mode='markers', name="Selected Point", marker=dict(color='red', size=10)))

fig.update_layout(title="DC Power vs Temperature Simulation",
                  xaxis_title="Temperature (°C)",
                  yaxis_title="DC Power (W)",
                  template="plotly_dark")

st.plotly_chart(fig)

import matplotlib.pyplot as plt

# Define the alpha values and corresponding average deflection values for blue line
alpha_values_1 = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
average_deflection_values_1 = [
    23.36,
    21.72,
    19.80,
    16.84,
    14.64,
    11.76,
    9.72,
    8.72,
    7.32,
    4.92,
    0.56,
]

# Define the alpha values and corresponding average deflection values for red line
alpha_values_2 = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.9557522123893806, 1]
average_deflection_values_2 = [
    53.03,
    48.81,
    43.12,
    38.05,
    30.50,
    24.23,
    19.61,
    15.96,
    12.12,
    8.48,
    4.80,
    1.08,
]

alpha_values_3 = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.9777777777777777, 1]
average_deflection_values_3 = [
    104.30,
    92.61,
    76.28,
    61.70,
    50.53,
    43.04,
    36.76,
    30.69,
    23.95,
    15.75,
    5.11,
    2.27,
]

average_deflection_values_1 = [value / 45 for value in average_deflection_values_1]
average_deflection_values_2 = [value / 108 for value in average_deflection_values_2]
average_deflection_values_3 = [value / 220 for value in average_deflection_values_3]

# Create the plot
plt.figure(figsize=(10, 6))

# Plot the blue line with labels for legend
plt.plot(
    alpha_values_1,
    average_deflection_values_1,
    marker="o",
    linestyle="-",
    color="b",
    label="108N-5000E",
)

# Plot the red line with labels for legend
plt.plot(
    alpha_values_2,
    average_deflection_values_2,
    marker="o",
    linestyle="-",
    color="r",
    label="45N-2000E",
)
plt.plot(
    alpha_values_3,
    average_deflection_values_3,
    marker="o",
    linestyle="-",
    color="g",
    label="220N-10000E",
)

# Add labels and title
plt.xlabel("Alpha")
plt.ylabel("Average Deflection / Nodes")
plt.title("(Average Deflection / Nodes) vs. Alpha")

# Show grid
plt.grid(True)

# Add legend with labels specified
plt.legend()

# Show the plot
plt.show()

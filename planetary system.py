import matplotlib.pyplot as plt
import numpy as np

# Use interactive mode
plt.ion()

# Star at origin
star_x, star_y = 0, 0

# Planets parameters: radius and angular speed
planets = [
    {"radius": 3, "theta": 0, "dtheta": 0.1, "color": "b", "size": 8},   # Planet 1
    {"radius": 5, "theta": 0, "dtheta": 0.05, "color": "g", "size": 10},  # Planet 2
    {"radius": 7, "theta": 0, "dtheta": 0.03, "color": "r", "size": 12}   # Planet 3
]

# Figure setup
fig, ax = plt.subplots()
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.set_aspect('equal')

# Draw star
ax.plot(star_x, star_y, 'yo', markersize=15)  # Yellow star

# Draw orbit circles
for p in planets:
    circle = plt.Circle((0, 0), p["radius"], color='gray', fill=False, linestyle='--')
    ax.add_patch(circle)

# Initialize planet plots
planet_plots = [ax.plot([], [], 'o', color=p["color"], markersize=p["size"])[0] for p in planets]

# Simulation loop
for _ in range(500):
    for i, p in enumerate(planets):
        x = [p["radius"] * np.cos(p["theta"])]
        y = [p["radius"] * np.sin(p["theta"])]
        planet_plots[i].set_data(x, y)
        p["theta"] += p["dtheta"]
    plt.pause(0.05)

# Keep the final plot open
plt.ioff()
plt.show()
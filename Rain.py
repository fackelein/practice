import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# A very simple rain effect can be obtained by having small growing rings
# randomly positioned over a figure. Of course, they won’t grow forever
# since ripples are supposed to damp with time. To simulate this phenomenon,
# we can use an increasingly transparent color as the ring is growing, up to
# the point where it is no more visible. At this point, we remove the ring
# and create a new one. First step is to create a blank figure.
fig = plt.figure(figsize=(6, 6), facecolor='white', dpi=50)

ax = fig.add_axes([0, 0, 1, 1], frameon=False, aspect=1)
ax.set_xlim(0, 1), ax.set_xticks([])
ax.set_ylim(0, 1), ax.set_yticks([])

# Then we create an empty scatter plot but we take care of settings linewidth
# (0.5) and facecolors ("None") that will apply to any new data.
scatter = ax.scatter([], [], s=[], lw=0.5,
                     edgecolors=[], facecolors="None")

# Next, we need to create several rings. For this, we can use the scatter plot
# object that is generally used to visualize points cloud, but we can also use
# it to draw rings by specifying we don’t have a facecolor. We also have to
# take care of initial size and color for each ring such that we have all sizes
# between a minimum and a maximum size. In addition, we need to make
# sure the largest ring is almost transparent.
n = 50
R = np.zeros(n, dtype=[("position", float, (2,)),
                       ("size", float, (1,)),
                       ("color", float, (4,))])
R["position"] = np.random.uniform(0, 1, (n, 2))
R["size"] = np.linspace(0, 1, n).reshape(n, 1)
R["color"][:, 3] = np.linspace(0, 1, n)


# Now, we need to write the update function for our animation. We know
# that at each time step each ring should grow and become more transpar‐
# ent while the largest ring should be totally transparent and thus removed.
# Of course, we won’t actually remove the largest ring but re‐use it to set a
# new ring at a new random position, with nominal size and color. Hence,
# we keep the number of rings constant.
def rain_update(frame):
    global R, scatter
    # Transparency of each ring is increased
    R["color"][:, 3] = np.maximum(0, R["color"][:, 3] - 1 / len(R))

    # Size of each rings is increased
    R["size"] += 1 / len(R)

    # Reset last ring
    i = frame % len(R)
    R["position"][i] = np.random.uniform(0, 1, 2)
    R["size"][i] = 0
    R["color"][i, 3] = 1

    # Update scatter object accordingly
    scatter.set_edgecolors(R["color"])
    scatter.set_sizes(1000 * R["size"].ravel())
    scatter.set_offsets(R["position"])


# Last step is to tell matplotlib to use this function as an update function for
# the animation and display the result (or save it as a movie):
animation = animation.FuncAnimation(fig, rain_update,
                                    interval=10, frames=200)
plt.show()

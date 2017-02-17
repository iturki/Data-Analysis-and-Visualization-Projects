import matplotlib.pyplot as plt

'''
An example to create a dumbbell chart in Python.
This is an stripped down example used in this post: http://turki.ws/?p=176
For a more customized example, see dembbell_plot.py

'''


labels = ['A', 'B', 'C']
a_values = [5, 6, 10]
b_values = [12, 10, 7]

# Create the figure
fig = plt.figure()
ax = fig.add_subplot(111)

for i in list(range(len(labels))):
    # Plot the line between dumbbells
    ax.plot([a_values[i], b_values[i]], [i, i], color='black')
    # Plot the dumbbells.
    ax.plot(a_values[i], i, color='red', marker='o', markersize=15)
    ax.plot(b_values[i], i, color='blue', marker='o', markersize=15)
    # Add data label on top of dumbbells
    ax.text(a_values[i], i, a_values[i], horizontalalignment='center', verticalalignment='center', color='white')
    ax.text(b_values[i], i, b_values[i], horizontalalignment='center', verticalalignment='center', color='white')
    # Add the axis label
    ax.text(3, i, labels[i], horizontalalignment='right', verticalalignment='center', fontsize=12)

# Adjust and show the plot
fig.subplots_adjust(left=0.3)
ax.set_axis_off()
plt.show()
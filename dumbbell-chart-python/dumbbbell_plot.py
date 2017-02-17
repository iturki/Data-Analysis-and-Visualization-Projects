import matplotlib.pyplot as plt

'''
This is an example to create a dumbbell chart in Python.

If not modified, this code will produce a chart like this:
If you would like to provide your data and customize the graph, modify the variables in the section below.
Please be aware that you need matplotlib installed in order for this to work.
'''

########## Modify Below ##########
# how many categories you have?
N = 13
# labels for categories (must have N labels)
axis_labels = ['Eastern', 'Riyadh', 'Makkah', 'Baha', 'Madinah', 'Qassim', 'Assir', 'Tabouk', 'Najran',
               'Northern Borders', 'Jazan', 'Hail', 'AlJouf']
# First dumbbell values (must have N values)
a = [71, 69, 70, 68, 69, 68, 67, 66, 64, 64, 63, 63, 63]
# Second dumbbell values (must have N values)
b = [68, 66, 65, 66, 64, 65, 65, 61, 62, 62, 62, 61, 60]
A_COLOR = '#EA2BA2'  # Color to plot a values
B_COLOR = '#006666'  # Color to plot b values
LINE_COLOR = '#000000'  # Color to plot the line between dumbbells
REVERSED_ORDER = True  # Order of plotting (False: bottom to top. True: top to bottom)
########## Modify Above ##########

# Styles to be used when plotting the different elements of the graph.
dumbbell_style_a = dict(color=A_COLOR, marker='o', markersize=15)
dumbbell_style_b = dict(color=B_COLOR, marker='o', markersize=15)
line_style = dict(color=LINE_COLOR, linestyle='-')
axis_label_style = dict(horizontalalignment='right', verticalalignment='center', fontsize=12,
                        fontdict={'family': 'monospace'})
data_label_style = dict(horizontalalignment='center', verticalalignment='center', color='white', weight='bold',
                        fontsize=8, fontdict={'family': 'monospace'})

# By default, data will be plotted bottom to top. If True, this will reverse the order (top to bottom)
if (REVERSED_ORDER):
    a.reverse()
    b.reverse()
    axis_labels.reverse()

# Create the figure
fig = plt.figure()
ax = fig.add_subplot(111)

# Get min and max values (for plotting purposes)
min = min([min(a), min(b)]) - 1
max = max([max(a), max(b)]) + 1

index = list(range(N))
# Loop N times
for i in index:
    # Plot the line between dumbbells
    ax.plot([a[i], b[i]], [i, i], **line_style)
    # Plot the dumbbells.
    ax.plot(a[i], i, **dumbbell_style_a)
    ax.plot(b[i], i, **dumbbell_style_b)
    # Add data label on top of dumbbells
    ax.text(a[i], i, a[i], **data_label_style)
    ax.text(b[i], i, b[i], **data_label_style)
    # Add the axis label
    ax.text(min, i, axis_labels[i], **axis_label_style)

# Adjust and save the figure
fig.subplots_adjust(left=0.3) # Depending on your data, you might not need this adjustment.
ax.set_axis_off()
plt.xlim(min, max)
plt.ylim(-1, N)
plt.savefig('dumbbell.png', dpi=300)
plt.show()

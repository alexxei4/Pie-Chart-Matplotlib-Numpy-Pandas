import pandas as pd
import collections
import matplotlib.pyplot as plt

# Read the dataset
dataset = pd.read_csv("tech.csv")

# Count how many times each technology appears in the dataset
technology_count = collections.Counter(dataset['FALL 2021 Co-op Technologies'])

# Sum up the number of technologies that appear less than 2 times
other_count = sum(v for v in technology_count.values() if v < 2)

# Add the "Other" category to the dictionary
technology_count["Other"] = other_count

# Remove any technologies that appear less than 2 times
to_delete = [k for k, v in technology_count.items() if v < 2]
[technology_count.pop(key) for key in to_delete]

# Sort the dictionary by value
sorted_technology_count = {k: v for k, v in sorted(technology_count.items(), key=lambda item: item[1])}

# This is for the "Explode" effect
explode = [0] * (len(sorted_technology_count) - 1)
explode.insert(23, 0.1) # Insert a value for the "Other" category slice

# This sets the colors for the pie chart
colors = ["forestgreen", "lightseagreen", "mediumaquamarine", "darkblue", "crimson", "orange", "purple", "navajowhite", "lightsalmon", "cornflowerblue", "lightpink","firebrick","indianred","lightskyblue"]

# Plot the pie chart
plt.figure(figsize=(8, 6), dpi=100)
plt.pie(sorted_technology_count.values(),
        labels=sorted_technology_count.keys(),
        explode=explode,
        colors=colors,
        startangle=150,
        counterclock=True,
        autopct='%2d %%',
        textprops={'fontsize': 10},
        rotatelabels=False,
        pctdistance=0.9)
plt.title('Technologies Used by COOPs in Fall 2021', fontsize=14)
plt.show()
# Right On , less then 45 Executable Lines :)

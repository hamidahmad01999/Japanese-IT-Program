# Random Color-Based Password Generator in Python
import random

colors =  ["red", "blue", "green", "yellow", "orange", "purple"]

selected_color = colors[random.randint(0, len(colors)-1)]

password = selected_color[::-1]
print(f"Selected Color: {selected_color}")
print(f"Generated password: {password}")
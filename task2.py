import re

file_path = 'task2.html'
with open(file_path, 'r') as file:
    html_content = file.read()

color_pattern = r'\b(?:color|background-color)\s*:\s*([^;]+);?'

colors = re.findall(color_pattern, html_content)

print("Colors found:", colors)
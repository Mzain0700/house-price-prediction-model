from PIL import Image, ImageDraw, ImageFont
import os

# Create directories if they don't exist
os.makedirs('static/images', exist_ok=True)

# Create a new image with a white background
width, height = 200, 200
image = Image.new('RGBA', (width, height), (255, 255, 255, 0))
draw = ImageDraw.Draw(image)

# Draw a house shape
house_color = (46, 125, 50)  # Green color
roof_points = [(40, 100), (100, 40), (160, 100)]
draw.polygon(roof_points, fill=house_color)
draw.rectangle([60, 100, 140, 160], fill=house_color)

# Draw a door
door_color = (255, 143, 0)  # Orange color
draw.rectangle([90, 130, 110, 160], fill=door_color)

# Draw a window
window_color = (3, 169, 244)  # Blue color
draw.rectangle([70, 110, 85, 125], fill=window_color)
draw.rectangle([115, 110, 130, 125], fill=window_color)

# Draw a graph line to represent price prediction
graph_color = (255, 143, 0)  # Orange color
graph_points = [(40, 180), (60, 170), (80, 175), (100, 165), (120, 155), (140, 145), (160, 130)]
draw.line(graph_points, fill=graph_color, width=3)

# Save the image
image.save('static/images/logo.png')
print("Logo generated and saved to static/images/logo.png")
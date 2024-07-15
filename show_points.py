import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

# Get directories from user
images_dir = "/datasets/co-tracker"
txts_dir = "/datasets/co-tracker/"

# Get list of .txt files and sort them
txt_files = sorted([f for f in os.listdir(txts_dir) if f.endswith('.txt')])

# Initialize index
index = 0

# Function to update the image
def update_image(index):
    txt_file = txt_files[index]
    txt_path = os.path.join(txts_dir, txt_file)
    image_path = os.path.join(images_dir, txt_file.split('.')[0] + '.jpg')

    # Read the image
    img = plt.imread(image_path)

    # Read the points from the .txt file
    points = np.loadtxt(txt_path)
    x = points[:, 0]
    y = points[:, 1]
    id = points[:, 2]

    # Get the height and width of the image
    height, width = img.shape[:2]

    # Clear the current plot
    axImage.clear()

    # Display the image
    axImage.imshow(img)

    # Plot the points on the image
    for i in range(len(x)):
        # Check if the point is within the image boundaries
        if 0 <= x[i] < width and 0 <= y[i] < height:
            # Use a colormap to get a color for each point based on its index
            color = cm.rainbow(i / len(x))
            if id[i] == 1:
                axImage.plot(x[i], y[i], 'o', color=color, markersize=2)
            else:
                axImage.plot(x[i], y[i], 'o', color=color, markerfacecolor='none', markersize=2)

    # Set the title of the plot to the filename
    axImage.set_title(txt_file)

    # Draw the plot
    fig.canvas.draw_idle()

# Function for the 'Next' key press event
def next_image(event):
    global index
    if event.key == 'right':
        index = (index + 1) % len(txt_files)
        update_image(index)

# Function for the 'Previous' key press event
def pre_image(event):
    global index
    if event.key == 'left':
        index = (index - 1) % len(txt_files)
        update_image(index)

# Create the figure and the image subplot
fig, axImage = plt.subplots(1)
update_image(index)

# Connect the 'next_image' function to the 'right' key press event
fig.canvas.mpl_connect('key_press_event', next_image)

# Connect the 'pre_image' function to the 'left' key press event
fig.canvas.mpl_connect('key_press_event', pre_image)

plt.show()

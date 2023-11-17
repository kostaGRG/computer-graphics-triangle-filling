import numpy as np
from triangle_filling import *
import matplotlib.pyplot as plt 

# Load data from "hw1.npy" file
data = np.load("hw1.npy",allow_pickle=True).item()
verts2d = data['verts2d']
vcolors = data['vcolors']
faces = data['faces']
depth = data['depth']

# Choose shade type
shade_type = 'flat'

# Get the image calling "render" function
image = render(verts2d,faces,vcolors,depth,shade_type)

plt.xticks([])
plt.yticks([])

# Save and print the image
plt.imshow(image)
plt.savefig((shade_type+'.png'))
plt.show()
from PIL import Image
import numpy as np

a = np.full((512, 256, 3), 255, dtype=np.uint8)
image = Image.fromarray(a, "RGB")
image.save("white.png", "PNG")

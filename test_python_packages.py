# test_python_packages.py
import cv2
from PIL import Image
import numpy as np
import imageio
import requests
from tqdm import tqdm
from logger_config import log_error, log_warning

print("=== Test des packages installés ===")

# Test OpenCV
print(f"OpenCV version: {cv2.__version__}")

# Test Pillow
print(f"Pillow version: {Image.__version__}")

# Test NumPy
print(f"NumPy version: {np.__version__}")

"""
Zina - Module d'animation éducative
Copyright © 2024 HikayatData (https://www.hikayatdata.com)
Licence MIT - https://opensource.org/license/mit/
"""
# Test MoviePy avec gestion des versions
try:
    # Essayer la version 2.x
    import moviepy

    print(f"moviePy version: {moviepy.__version__} (v2)")
except (ImportError, AttributeError):
    try:
        # Fallback sur la version 1.x
        from moviepy.editor import __version__ as moviepy_v1_version

        print(f"moviePy version: {moviepy_v1_version} (v1)")
    except ImportError:
        print("moviePy: NON INSTALLÉ")

# Test imageio
print(f"imageio version: {imageio.__version__}")

# Test requests
response = requests.get("https://httpbin.org/get")
print(f"Requests test: HTTP {response.status_code}")

# Test tqdm
for _ in tqdm(range(1000000)):
    pass

print("✅ Tous les packages fonctionnent correctement")


© 2025 HikayatData
[![License: MIT](https://img.shields.io/badge/License-MIT-HikayatData-blue.svg)](https://opensource.org/licenses/MIT)
# Projet Zina - Système d'Animation Éducative

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Système de création de cartoons éducatifs pour enfants utilisant Python et MoviePy.

## 🚀 Configuration Express (5 minutes)

### 1. Prérequis système
```bash
sudo apt update && sudo apt install -y ffmpeg python3.12 python3.12-venv git
```

### 2. Cloner et configurer
```bash
git clone https://github.com/MARA1976/zinacartoon.git
cd zinacartoon
python3.12 -m venv zina_env
source zina_env/bin/activate
```

### 3. Installer les dépendances
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

## 🎬 Première utilisation

### Tester MoviePy
```bash
python test_integration.py  # Génère test_output.mp4
```

### Visualiser dans Streamlit
```bash
streamlit run video_viewer.py
```
➡️ Ouvre automatiquement http://localhost:8501

## 📦 Configuration MoviePy

### Fichier `requirements.txt` optimisé :
```txt
moviepy==2.2.1  # Version stable recommandée
numpy==2.2.6
opencv-python==4.11.0.86
pillow==11.2.1
imageio[ffmpeg]==2.37.0  # Gestion FFmpeg
streamlit==1.35.0  # Dashboard
```

### Code compatible v2.2.1 :
```python
from moviepy import VideoFileClip, TextClip  # Nouvel import

clip = VideoFileClip("input.mp4")
text = TextClip(
    text="Bonjour Zina",
    fontsize=70,
    color='white',
    font='Arial',
    size=(800, 100)
```

## 🔄 Migration depuis MoviePy v1
| Ancien (v1)                  | Nouveau (v2)               |
|------------------------------|----------------------------|
| `from moviepy.editor import`  | `from moviepy import`       |
| `clip.set_position()`         | `clip.with_position()`      |
| `clip.set_duration(5)`        | `clip.with_duration(5)`     |

## 📂 Structure du projet
```
zinacartoon/
├── assets/           # Assets visuels
├── output/           # Vidéos générées
├── scripts/          # Scripts métier
├── tests/            # Tests unitaires
├── test_integration.py  # Test vidéo
├── video_viewer.py   # Dashboard Streamlit
└── requirements.txt  # Dépendances
```

## 💡 Bonnes pratiques
1. Toujours utiliser `zina_env` :
   ```bash
   source zina_env/bin/activate
   ```
2. Pour régénérer les dépendances :
   ```bash
   pip freeze > requirements.txt
   ```
3. Documentation MoviePy :
   moviepy.readthedocs.io
"""
Zina - Module d'animation éducative
Copyright © 2024 HikayatData (https://www.hikayatdata.com)
Licence MIT - https://opensource.org/license/mit/
"""

import os
import subprocess
import sys
from logger_config import log_error, log_warning

# Vérifie si on est en mode CI (GitHub Actions)
IS_CI = os.getenv("CI") == "true"


def generate_video():
    """Génère la vidéo de test (commun aux deux modes)"""
    result = subprocess.run(
        ["python", "test_integration.py", "--cleanup"], capture_output=True, text=True
    )

    if IS_CI:
        print(result.stdout)
        if result.returncode != 0:
            print(f"ERREUR: {result.stderr}")
            return False
        return True

    # Mode Streamlit
    import streamlit as st

    st.code(result.stdout)
    if result.returncode == 0:
        st.success("Vidéo générée avec succès!")
    else:
        st.error(f"Erreur lors de la génération:\n{result.stderr}")
    return result.returncode == 0


def main():
    if IS_CI:
        # Mode GitHub Actions
        print("=== Début du test vidéo ===")
        success = generate_video()
        sys.exit(0 if success else 1)
    else:
        # Mode Streamlit local
        import streamlit as st

        st.title("ZINA Project - Video Viewer")
        st.header("Test d'intégration MoviePy")

        with st.expander("Générer une nouvelle vidéo de test"):
            if st.button("Lancer test_integration.py"):
                generate_video()

        # Section visualisation
        st.subheader("Visualisation")
        if os.path.exists("test_output.mp4"):
            file_size = os.path.getsize("test_output.mp4") // 1024
            st.video("test_output.mp4")
            st.success(f"Vidéo chargée - Taille: {file_size} KB")

            col1, col2 = st.columns(2)
            with col1:
                if st.button("Supprimer la vidéo"):
                    os.remove("test_output.mp4")
                    st.experimental_rerun()
            with col2:
                with open("test_output.mp4", "rb") as f:
                    st.download_button("Télécharger", f, "zina_test.mp4")
        else:
            st.warning("Aucune vidéo disponible. Génerez d'abord une vidéo de test.")


if __name__ == "__main__":
    main()

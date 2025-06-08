
"""
Zina - Module d'animation éducative
Copyright © 2024 HikayatData (https://www.hikayatdata.com)
Licence MIT - https://opensource.org/license/mit/
"""

import streamlit as st
import os
import subprocess
from logger_config import log_error, log_warning



def main():
    st.title( "ZINA Project - Video Viewer" )
    st.header( "Test d'intégration MoviePy" )

    # Section de génération vidéo
    with st.expander( "Générer une nouvelle vidéo de test" ):
        if st.button( "Lancer test_integration.py" ):
            result = subprocess.run( ["python", "test_integration.py"], capture_output=True, text=True )
            st.code( result.stdout )
            if result.returncode == 0:
                st.success( "Vidéo générée avec succès!" )
            else:
                st.error( f"Erreur lors de la génération:\n{result.stderr}" )

    # Section de visualisation
    st.subheader( "Visualisation" )
    if os.path.exists( "test_output.mp4" ):
        file_size = os.path.getsize( "test_output.mp4" ) // 1024
        st.video( "test_output.mp4" )
        st.success( f"Vidéo chargée - Taille: {file_size} KB" )

        # Options supplémentaires
        col1, col2 = st.columns( 2 )
        with col1:
            if st.button( "Supprimer la vidéo" ):
                os.remove( "test_output.mp4" )
                st.experimental_rerun()
        with col2:
            with open( "test_output.mp4", "rb" ) as f:
                st.download_button( "Télécharger", f, "zina_test.mp4" )
    else:
        st.warning( "Aucune vidéo disponible. Génerez d'abord une vidéo de test." )


if __name__ == "__main__":
    main()
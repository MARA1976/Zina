"""
Zina - Module d'animation éducative
Copyright © 2024 HikayatData (https://www.hikayatdata.com)
Licence MIT - https://opensource.org/license/mit/
"""

#test_integration.py
import os
import time
from moviepy import CompositeVideoClip
from moviepy.video.VideoClip import TextClip, ColorClip


def create_test_video(output_path="test_output.mp4"):
    """Crée une vidéo de test avec MoviePy v2.1.2"""
    print( "Création du clip de couleur..." )
    clip = ColorClip( size=(640, 480), color=(0, 120, 255), duration=3 )

    print( "Création du texte..." )
    text = TextClip( text="Test Réussi!", color='white', size=(640, 100), duration=3 )

    # Positionnement du texte - syntaxe spécifique à v2.1.2
    print( "Positionnement du texte..." )
    text = text.with_position( ('center', 190) )  # Utilisation de with_position

    print( "Combinaison des clips..." )
    final = CompositeVideoClip( [clip, text] )

    print( "Exportation de la vidéo..." )
    start_time = time.time()
    final.write_videofile( output_path, fps=24, logger=None )
    export_time = time.time() - start_time

    print( f"Exportation terminée en {export_time:.2f} secondes" )
    return output_path


if __name__ == "__main__":
    print( "=== Début du test d'intégration MoviePy ===" )
    try:
        output_file = create_test_video()

        if os.path.exists( output_file ):
            size_kb = os.path.getsize( output_file ) // 1024
            print( f"\n✅ Vidéo générée avec succès: {output_file}" )
            print( f"Taille: {size_kb} KB" )

            # Optionnel: demander si on veut supprimer
            delete = input( "Supprimer le fichier temporaire? (o/n) " ).lower()
            if delete == 'o':
                os.remove( output_file )
                print( "Fichier temporaire nettoyé" )
            else:
                print( "Fichier conservé: " + output_file )
        else:
            print( "\n❌ Échec: le fichier vidéo n'a pas été créé" )
    except Exception as e:
        print( f"\n❌ Erreur pendant l'exécution: {str( e )}" )
    print( "=== Fin du test ===" )

"""
Zina - Module d'animation éducative
Copyright © 2024 HikayatData (https://www.hikayatdata.com)
Licence MIT - https://opensource.org/license/mit/
"""

# check_modules.py
def verify_moviepy():
    try:
        # Version v2
        import moviepy
        return f"✅ MoviePy v2 installée: {moviepy.__version__}"
    except (ImportError, AttributeError):
        try:
            # Fallback v1
            from moviepy.editor import __version__ as v
            return f"⚠️ MoviePy v1 installée: {v} (obsolète)"
        except ImportError:
            return "❌ MoviePy non installée"


# Test de tous les modules
if __name__ == "__main__":
    print( "=== Vérification des modules ===" )
    print( verify_moviepy() )

    # Ajoutez ici d'autres vérifications si nécessaire
    import sys

    print( f"Version Python: {sys.version.split()[0]}" )
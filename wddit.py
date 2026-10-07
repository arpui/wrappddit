import praw
from prawcore.exceptions import ResponseException

def llegir_dades_reddit(client_id="", client_secret="", user_agent="", subreddit_nom="Python", limit=5):
    """
    Connecta a Reddit i llegeix els últims posts d'un subreddit.
    Inclou gestió de valors nuls i captura d'errors de xarxa.
    """
    # Validació prèvia per evitar errors d'execució
    if not client_id or not client_secret or not user_agent:
        print("Error: Falten les credencials d'autenticació.")
        return []

    try:
        # Inicialització del wrapper de Reddit
        reddit = praw.Reddit(
            client_id=client_id,
            client_secret=client_secret,
            user_agent=user_agent
        )
        
        # Extracció de dades (només lectura)
        subreddit = reddit.subreddit(subreddit_nom)
        resultats = []
        
        for post in subreddit.new(limit=limit):
            resultats.append({
                "títol": post.title,
                "autor": str(post.author) if post.author else "Desconegut",
                "puntuació": post.score,
                "url": post.url
            })
            
        return resultats

    except ResponseException as e:
        print(f"Error d'autenticació o de l'API: {e}")
        return []
    except Exception as e:
        print(f"S'ha produït un error de connexió inesperat: {e}")
        return []

if __name__ == "__main__":
    # Substitueix aquestes variables quan tinguis les credencials finals
    CLIENT_ID = ""
    SECRET = ""
    AGENT = "script:Lector_Dades:v1.0 (by /u/el_teu_usuari)"
    
    dades_obtingudes = llegir_dades_reddit(
        client_id=CLIENT_ID,
        client_secret=SECRET,
        user_agent=AGENT
    )
    
    if dades_obtingudes:
        for item in dades_obtingudes:
            print(f"[{item['puntuació']}] {item['títol']}")
from .en import Lang as LBase

class Lang(LBase):
    """ Thanks @danogentili """
    lang = "it"
    format_unsupported = "Formato audio non supportato."
    start_message = "Questo bot può amplificare i bassi di file audio mandati ad esso. Mandami una canzone."
    help_message = start_message + "\n\nQuesto bot fa parte del network di bot @luckydonaldsbots.\n\nQUESTO BOT FA SCHIFO\nEHI!!! BELLOH!!! PERCHÈ LO STAI ANCORA USANDO?!?"
    caption = "@{bot} ha appena amplificato i tuoi bassi!"
    progress1 = "caricamento audio"
    progress2 = "lettura traccia"
    progress3 = "calcolo dell'amplificazione media necessaria"
    progress4 = "calcolo dell'amplificazione necessaria"
    progress5 = "calcolo dell'amplificazione potenziata necessaria"
    progress6 = "estrazione delle regioni da amplificare"
    progress7 = "applicazione dei bassi potenziati alla traccia originale"
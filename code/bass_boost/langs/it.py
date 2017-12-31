from .en import Lang as LBase

class Lang(LBase):
    """ Thanks @danogentili """
    lang = "it"
    format_unsupported = "Formato audio non supportato."
    start_message = "Questo bot può potenziare i bassi di file audio mandati ad esso. Mandami una canzone."
    help_message = start_message + "\n\nQuesto bot fa parte del network di bot @luckydonaldsbots.\n\nQUESTO BOT FA SCHIFO\nEHI!!! BELLOH!!! PERCHÈ LO STAI ANCORA USANDO?!?"
    caption = "@{bot} ha appena potenziato i tuoi bassi!"
    progress1 = "caricamento audio"
    progress2 = "lettura traccia audio"
    progress3 = "calcolo del potenziamento medio necessario"
    progress4 = "calcolo del potenziamento necessario"
    progress5 = "calcolo del potenziamento potenziato necessario"
    progress6 = "estrazione delle regioni da potenziare"
    progress7 = "applicazione dei bassi potenziati alla traccia originale"
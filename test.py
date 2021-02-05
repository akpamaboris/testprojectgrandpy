from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


newmessage = input('this is a new message')

# Je specifie que les stopwords sont en français
stopWords = set(stopwords.words("french"))

        # je tokenize la phrase, c'est à dire que je sépare une phrase
        # en de plus petits éléments
wordTokens = word_tokenize(newmessage)

        # je crée une liste vide pour pouvoir stocker la phrase une fois que les stop words
        # auront étés enlevés de celle ci
phrase_avec_filtre = []

        # Je crée une boucle avec la variable w pour repérer les éléments qu'il y  a dans
        # ma requête tokénisée qui ne sont pas dans les stop words en français
        # ce procédé permet de filtrer tous les stop words afin de recueuillir une requête
        # filtrée sous forme de liste

for w in wordTokens:
    if w not in stopWords:
        phrase_avec_filtre.append(w)

        # je convertis cette liste alors tous juste créée en un élément string
full_str = " ".join([str(elem) for elem in phrase_avec_filtre])

        # je commence à préparer mon opération de cherchage
searchRequest = str(full_str)

print(searchRequest)
from owlready2 import *

onto_path = "C:/Users/zyran/OneDrive/Documents/Cours/EMA/Web Semantique/App/Ontologie/ProjetPlante.owl"
onto = get_ontology(onto_path).load()

print(onto.Attribut)
print(list(onto.classes()))

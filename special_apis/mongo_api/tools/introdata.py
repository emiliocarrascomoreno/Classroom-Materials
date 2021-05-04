from config.configuration import db, collection


def intro_frase(frase,personaje, secuencia):
    return collection.insertOne({ "scene":secuencia , "character_name": personaje, "dialogue":frese})
    
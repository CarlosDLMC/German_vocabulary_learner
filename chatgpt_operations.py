## pip install -U g4f
# en github es gpt4free

import g4f


# g4f.debug.logging = True  # Enable debug logging
# g4f.debug.version_check = False  # Disable automatic version checking
# print(g4f.Provider.Bing.params)  # Print supported args for Bing


def get_translation(word):
    first_message = """
    Te voy a escribir palabras en alemán, en el formato palabra + nivel "por ejemplo, das Gehirn A2", y necesito que me des la siguiente salida para cada palabra que escriba:
    -la palabra traducida al español, al ruso y al inglés (la palabra en ruso no necesita transcripción).
    -tres frases en alemán usando esta palabra, de tal forma que se entienda su significado. En el caso de que la palabra sea un verbo, una frase debe estar en presente, la otra usando el Präteritum y la tercera usando el Perfekt

    No me añadas ninguna información extra que no te he pedido. No me escribas "Aquí está la informacín de la palabra "palabra ":,
    escribe simplemente "das Gehirn, A2"
    Español: cerebro
    Русский: мозг
    English: brain
    Y luego los ejemplos
    Todo entendido?
    """

    first_answer = """
    Sí, todo entendido. Estoy listo para ayudarte con las palabras en alemán que me escribas. Por favor, escribe una palabra por mensaje.
    """
    response = g4f.ChatCompletion.create(
        model=g4f.models.default,
        provider=g4f.Provider.Bing,
        messages=[{"role": "user", "content": first_message},
                  {"role": "assistant", "content": first_answer},
                  {"role": "user", "content": word}],
    )
    return response


# print(get_translation("der Eimer, - B1"))

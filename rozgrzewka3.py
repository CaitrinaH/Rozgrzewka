#napisz funkcję, która zanonimizuje podany string poprzez zamianę wszystkich liter poza pierwszą i ostatnią na gwiazdki


def anonymize_text(text):
    text = text.replace(text[1:-1], "*" * len(text[1:-1]))
    return text

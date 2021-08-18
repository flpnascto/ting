def exists_word(word, instance):
    word_lines = []
    for index in range(0, len(instance)):
        item = instance.search(index)
        occurrence = []
        is_word_found = False
        for line in item["linhas_do_arquivo"]:
            if word.lower() in line.lower():
                occurrence.append(
                    {"linha": item["linhas_do_arquivo"].index(line) + 1}
                )
                is_word_found = True
        if is_word_found:
            word_lines.append(
                {
                    "palavra": word,
                    "arquivo": item["nome_do_arquivo"],
                    "ocorrencias": occurrence,
                }
            )
    return word_lines


def search_by_word(word, instance):
    """Aqui irá sua implementação"""

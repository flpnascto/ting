import sys


def txt_importer(path_file):
    lines = []
    try:
        if not path_file.endswith(".txt"):
            sys.stderr.write("Formato inválido\n")
        else:
            with open(path_file, "rt", newline="\n") as txt_content:
                for line in txt_content:
                    lines.append(line.strip())
                return lines
    except FileNotFoundError:
        sys.stderr.write(f"Arquivo {path_file} não encontrado\n")

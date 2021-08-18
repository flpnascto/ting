from ting_file_management.file_management import txt_importer
import sys

# from ting_file_management.queue import Queue


def process(path_file, instance):
    lines = txt_importer(path_file)
    data_info = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(lines),
        "linhas_do_arquivo": lines,
    }
    if len(instance) > 0:
        file_is_queued = False
        for index in range(0, len(instance)):
            item = instance.search(index)
            if item["nome_do_arquivo"] == data_info["nome_do_arquivo"]:
                file_is_queued = True
                # como "parar" o for
        if not file_is_queued:
            instance.enqueue(data_info)
    else:
        instance.enqueue(data_info)

    sys.stdout.write(str(data_info))


def remove(instance):
    if len(instance) < 1:
        sys.stdout.write("Não há elementos\n")
    else:
        item = instance.search(len(instance) - 1)
        path_file = item["nome_do_arquivo"]
        instance.dequeue()
        sys.stdout.write(f"Arquivo {path_file} removido com sucesso\n")


def file_metadata(instance, position):
    try:
        item = instance.search(position)
        sys.stdout.write(str(item))
    except IndexError:
        sys.stderr.write("Posição inválida")

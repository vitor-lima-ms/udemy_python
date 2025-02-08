from contextlib import contextmanager
from pathlib import Path

FILE_PATH = Path(__file__).parent / '31_file.txt'


@contextmanager
def my_open(file_path, mode):
    try:
        file = open(file_path, mode)
        yield file #Por isso e um generator, pois tem yield
        file.close()
    except Exception as error: #Nem precisamos do except
        print('Ocorreu um erro', error)
    finally:
        file.close()

with my_open(FILE_PATH, 'w') as file:
    file.write('Linha1\n')
    file.write('Linha2\n', 'Erro proposital.')
    file.write('Linha3\n')
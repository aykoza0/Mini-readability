import os


# Парсить ли ссылки, принимает 2 значения 0 -выкл 1 - вкл
LINK = 1

# Позиционирование ссылки. После текста ссылки или до. Может принимать значения 'after' или 'before'
LINK_PARSER = 'after'

# Ширина строки для переноса по словам. Принимает возможное количество символов в строке.
LINE_BREAK_WIDTH = 80

# Домашняя директория для сохранения файла.
CUR_DIR = os.getcwd()

# Отступ у параграфа, принимает 2 значения 0 -выкл 1 - вкл
IDENT = 0

import hashlib


def get_hash(path):
    with open(path) as file:
        for line in file:
            yield hashlib.md5(line.encode()).hexdigest()


path = str(input('Введите путь к файлу: '))
for str_hash in get_hash(path):
    print(str_hash)

    # countries_links.txt
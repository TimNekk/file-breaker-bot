from secrets import randbelow


def corrupt_file(file: str):
    with open(file, 'w') as f:
        for _ in range(2500):
            f.write(chr(randbelow(127)))


def main():
    corrupt_file(input('Введите название файла: '))


if __name__ == '__main__':
    main()
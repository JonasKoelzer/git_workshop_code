from pathlib import Path

if __name__ == '__main__':
    p = Path('.')
    for txt_file in p.glob('./[0-9]*.txt'):
        with txt_file.open() as f:
            print(f.readline())



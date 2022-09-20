import sqlite3
import sys
import getpass


def main():
    file_list = []
    username = getpass.getuser()
    db = sqlite3.connect("./History")

    for row in db.execute('SELECT target_path, total_bytes FROM downloads'):
        file_list = row[0].split('\\')
        print(file_list[-1])


if __name__ == "__main__":
    main()
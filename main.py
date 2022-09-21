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

    for row in db.execute('SELECT target_path, total_bytes FROM downloads'):
        file_list = row
        if file_list[-1] / 1048576 >= 1:
            print(round(file_list[-1]/1048576),"MB")
        elif file_list[-1] / 1024 >= 1:
            print(round(file_list[-1] / 1024),"KB")
        else:
            print(round(file_list[-1]),"Bytes")


if __name__ == "__main__":
    main()
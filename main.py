import sqlite3
import sys
import getpass


def main():
    file_info = []
    file_list = []
    size = []
    ref = []

    username = getpass.getuser()
    db = sqlite3.connect("./History")

    for row in db.execute('SELECT target_path, total_bytes FROM downloads'):
        file_list = row[0].split('\\')
        print(file_list[-1])

    for row in db.execute('SELECT total_bytes FROM downloads'):
        size = row
        if size[-1] / 1048576 >= 1:
            print(round(size[-1]/1048576),"MB")
        elif size[-1] / 1024 >= 1:
            print(round(size[-1] / 1024),"KB")
        else:
            print(round(size[-1]),"Bytes")

    for referrer in db.execute('SELECT referrer FROM downloads'):
        ref = referrer
        print(ref[-1])

    file_info = file_list
    file_info = size
    file_info = ref
    print(file_info)


if __name__ == "__main__":
    main()
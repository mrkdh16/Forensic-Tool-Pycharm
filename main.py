import sqlite3
import sys
import getpass


def main():
    name_list = []
    size_list = []
    ref_list = []
    file_info = []

    username = getpass.getuser()
    db = sqlite3.connect("./History")                       

    for row in db.execute('SELECT target_path FROM downloads'):
        name_list.append(row[0].split('\\')[-1])

    for row in db.execute('SELECT total_bytes FROM downloads'):
        if row[-1] / 1048576 >= 1:
            size_list += ((round(row[-1]/1048576),"MB"),)
        elif row[-1] / 1024 >= 1:
            size_list += ((round(row[-1] / 1024),"KB"),)
        else:
            size_list += ((round(row[-1]),"Bytes"),)

    for referrer in db.execute('SELECT referrer FROM downloads'):
        file_info += ()
        ref_list.append(referrer[-1])

    print(file_info)

if __name__ == "__main__":
    main()
import os


def get_db(file_name):
    with open(file=file_name, mode='r', encoding="utf-8") as my_bd:
        data = []
        col_name = my_bd.readline()[:-1].split(",")
        for line in my_bd.readlines():
            list_line = line[:-1].split(",")
            row = {}
            for index in range(len(col_name)):
                row[col_name[index]] = list_line[index]
            data.append(row)
        my_bd.close()
    return data


def add_data_db(file: str, data: dict):
    check_file = os.path.exists(file)  # True
    if check_file:
        with open(file=file, mode='r+', encoding="utf-8") as my_db:
            col_name = my_db.readline()[:-1].split(',')
            if col_name == list(data.keys()):
                my_db.write(",".join(list(data.values())))
                my_db.write("\n")
            else:
                print("Error не найдено таких стольбцов!")
    else:
        with open(file=file, mode='w+', encoding="utf-8") as my_db:
            col_names = ','.join(list(data.keys()))
            col_names += '\n'+ ",".join(list(data.values())) +'\n'
            my_db.write(col_names)


def del_data_db(file, col_name:str, val:str):
    check_file = os.path.exists(file)  # True
    if check_file:
        temp = ''
        with open(file=file, mode='r+', encoding="utf-8") as my_db:
            temp = my_db.readline()
            col_names_db = temp[:-1].split(',')
            if col_name in col_names_db:
                row_index = col_names_db.index(col_name)
                for _line in my_db.readlines():
                    if val != _line[:-1].split(',')[row_index]:
                        temp += _line
            else:
                print("Error не найдено таких стольбцов!")
                return False
        with open(file=file, mode='w+', encoding="utf-8") as my_db:
            my_db.write(temp)
            return True
    else:
        print("Error не найден файл")
        return False


if __name__ == "__main__":
    print(get_db("phon.txt"))
    add_data_db('phon.txt', data={'Фамилия': 'Иванов', 'Имя': 'Иван', 'Номер': ' 111', 'доп': 'описание Иванова'})
    print(get_db("phon.txt"))
    del_data_db('phon.txt', 'Фамилия', 'Иванов')

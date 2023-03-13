

if __name__ == "__main__":
    users = ['user1', 'user2', 'user3', 'user4', 'user5']
    ids = [4, 5, 9, 14, 7]
    salary = [111, 222, 333]
    print(list(zip(users, ids, salary)))
    print(list(zip(*zip(users, ids, salary))))
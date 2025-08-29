import time
class UserManager:
    def __init__(self):
        self.users = []  

    def add_user(self, user_id, name):
        self.users.append({"id": user_id, "name": name})

    def find_user(self, user_id):
        user = None
        for u in self.users:
            if u["id"] == user_id:
                user = u
        return user  

    def delete_user(self, user_id):
        for u in self.users:
            if u["id"] == user_id:
                self.users.remove(u)
                break  

    def get_all_names(self):
        return [u["id"] for u in self.users]

    def average_user_id(self):
        return sum([u["id"] for u in self.users]) / len(self.users)


if __name__ == "__main__":
    user_manager = UserManager()

    for i in range (1000):
        user_manager.add_user(i,f"Yo soy el num: {i}")

    #print(user_manager.find_user(2))

    ''''
    user_manager.delete_user(3)
    print(user_manager.find_user(3))
    '''

    #RF4
    #print(user_manager.get_all_names())

    #RF5
    #print(user_manager.average_user_id())

    #RF6
    '''
    start = time.time()
    print(user_manager.find_user(500))
    end = time.time()
    print(f"Tardó {end - start} segundos")
    '''

    #RF7
    print(user_manager.delete_user(1001))
    print("end")



class HashTable:
    ## WRITE HT CONSTRUCTOR HERE ##
    #                             #
    #                             #
    ###############################

    def __hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash

    def __init__(self):
        self.data_map = [None] * 7

    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i, ": ", val)

    def set_item(self, key, value):
        index = self.__hash(key)

        if self.data_map[index] is None:
            self.data_map[index] = []

        self.data_map[index].append([key, value])

    def get_item(self, key):
        index = self.__hash(key)

        if (index_list := self.data_map[index]) is None:
            return None

        for data in index_list:
            if data[0] == key:
                return data[1]

        return None

    def keys(self):
        keys = []

        for data in self.data_map:
            if data is None:
                continue

            for key, _ in data:
                keys.append(key)

        return keys


my_hash_table = HashTable()

my_hash_table.print_table()


"""
    EXPECTED OUTPUT:
    ----------------
    0 :  None
    1 :  None
    2 :  None
    3 :  None
    4 :  None
    5 :  None
    6 :  None

"""

print("===" * 5)

my_hash_table = HashTable()

my_hash_table.set_item("bolts", 1400)
my_hash_table.set_item("washers", 50)
my_hash_table.set_item("lumber", 70)

my_hash_table.print_table()


"""
    EXPECTED OUTPUT:
    ----------------
    0 :  None
    1 :  None
    2 :  None
    3 :  None
    4 :  [['bolts', 1400], ['washers', 50]]
    5 :  None
    6 :  [['lumber', 70]]

"""

print("===" * 5)

my_hash_table = HashTable()

my_hash_table.set_item("bolts", 1400)
my_hash_table.set_item("washers", 50)

print("Bolts:", my_hash_table.get_item("bolts"))
print("Washers:", my_hash_table.get_item("washers"))
print("Lumber:", my_hash_table.get_item("lumber"))


"""
    EXPECTED OUTPUT:
    ----------------
    Bolts: 1400
    Washers: 50
    Lumber: None

"""

print("===" * 5)

my_hash_table = HashTable()

my_hash_table.set_item("bolts", 1400)
my_hash_table.set_item("washers", 50)
my_hash_table.set_item("lumber", 70)

print(my_hash_table.keys())


"""
    EXPECTED OUTPUT:
    ----------------
    ['bolts', 'washers', 'lumber']

"""

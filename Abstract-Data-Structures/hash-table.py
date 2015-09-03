
class HashTable(object):
    """
    Implementation of a Hash Table that maps
    string keys to values.
    """

    max_size = 101
    prime = 101

    def __init__(self):
        self.table = [None] * self.max_size

    def insert(self, key, value):
        index = self._hash(key) % self.max_size

        if self.table[index] is None:
            self.table[index] = [(key,value)]
        else:
            self.table[index].append((key,value))

    def delete(self, key):
        index = self._hash(key) % self.max_size

        if self.table[index] is None:
            raise KeyError(('Key %s not found in the dict.') % key)
        for i, item in enumerate(list(self.table[index])):
            if item[0] == key:
                del self.table[index][i]
                break

        raise KeyError(('Key %s not found in the dict.') % key)

    def search(self, key):
        index = self._hash(key) % self.max_size

        if self.table[index] is None:
            return None
        for item in self.table[index]:
            if item[0] == key:
                return item[1]
        return None

    def _hash(self, key):
        hash_value = 0
        for item in key:
            hash_value = (self.prime * hash_value) + ord(item)
        return hash_value


if __name__ == '__main__':
    h = HashTable()
    h.insert('Name', 'ankesh')
    h.insert('Sur', 'anand')
    print h.search('Name')
    print h.search('Sur')
    h.delete('Sur')
    print h.search('Sur')

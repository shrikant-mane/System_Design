import hashlib

class BloomFilter:
    def __init__(self, size=100, hash_count=3):
        self.size = size
        self.hash_count = hash_count
        self.bit_array = bytearray(size)

    def _hashes(self, item):
        item = str(item).encode("utf-8")

        for i in range(self.hash_count):
            data = i.to_bytes(4, "big") + item
            digest = hashlib.sha256(data).digest()
            yield int.from_bytes(digest, "big") % self.size

    def add(self, item):
        for index in self._hashes(item):
            self.bit_array[index] = 1

    def contains(self, item):
        return all(
            self.bit_array[index] == 1
            for index in self._hashes(item)
        )


bloom = BloomFilter()

bloom.add("apple")
bloom.add("banana")
bloom.add("mango")

print(bloom.contains("apple"))
print(bloom.contains("banana"))
print(bloom.contains("grape"))

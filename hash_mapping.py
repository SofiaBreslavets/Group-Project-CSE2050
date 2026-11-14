
class Entry:
    """Stores one key-value pair"""

    def __init__(self, key, value):
        """Initialize the key and value"""
        self.key = key
        self.value = value



class HashMapping:
    """A mapping using a hashing"""

    def __init__(self, size=2):
        """Initializes an empty HashMapping."""
        self._n_buckets = size
        self._len = 0
        self._L = [[] for i in range(self._n_buckets)]

    def __len__(self):
        """Returns the number of key-value pairs"""
        return self._len

    def _find_bucket(self, key):
        """Returns the index of the bucket for the key"""
        return hash(key) % self._n_buckets

    def __contains__(self, key):
        """Checks if a key exists in the mapping"""

        idx = self._find_bucket(key)
        bucket = self._L[idx]

        for e in bucket:
            if e.key == key:
                return True

        return False

    def put(self, key, value):
        """Adds or updates a key-value pair"""
        
        idx = self._find_bucket(key)
        bucket = self._L[idx]

        for e in bucket:
            if e.key == key:
                e.value = value
                return

        bucket.append(Entry(key, value))
        
        self._len += 1

        if self._len > self._n_buckets:
            self.rehash()

    def get(self, key):
        """Returns the value associated with a key"""

        idx = self._find_bucket(key)
        bucket = self._L[idx]

        for e in bucket:
            if e.key == key:
                return e.value
        raise KeyError(key)

    def rehash(self):
        """Creates a larger bucket table and reinserts all entries"""

        old_L = self._L
        self._n_buckets *= 2
        self._L = [[] for i in range(self._n_buckets)]

        for bucket in old_L:
            for e in bucket:
                idx = self._find_bucket(e.key)
                self._L[idx].append(e)

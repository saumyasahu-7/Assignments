# LRUCache Usage Instructions

This guide demonstrates the working of `LRUCache` class.

## Explanation for LRUCache Class

### Putting in Cache

- **If key is already present in cache**: Update the value and give it first priority.
- **If key is not already present in cache**: Create a key-value pair in the cache.
    - If the cache is not full: Give first priority to the incoming key.
    - If the cache is full: Remove the least recently used key and give first priority to the incoming key.

### Getting from Cache

- **If key is present in cache**: Give the key first priority and return its value.
- **If key is not present in cache**: Return `-1`.

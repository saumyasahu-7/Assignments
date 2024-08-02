# Explanation for LRUCache class
<br>
**putting in cache**
<br>
-If key is already present in cache=> updating the value and giving it first priority
<br>
-If key is not already present in cache=>reating key, value pair in cache
<br>
    -if cache is is not full=> give first priority to incoming key
<br>
    -if cache is is full=> remove least recently used key and give first priority to incoming key
<br>
**getting from cache**
<br>
-If key is present in cache=> give the key first priority and return its value
<br>
-If key is present in cache=> return -1
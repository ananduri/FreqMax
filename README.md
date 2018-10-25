# FreqMax

Data structure used to track most frequently occuring keys in a list of keys.

Supports reading a list of length N in O(N) time, and returning the k most frequently occurring elements in O(k) time.

This data structure offers superior time complexity to the more standard solution of using a max-heap to track the most commonly occurring elements, by getting rid of the log N factor.

## Usage

```python
freqmax = FreqMax()
data = ['b', 'c', 'd', 'a', 'b', 'c', 'd', 'd', 'b', 'd', 'd', 'a']

for d in data:
    freqmax.add(d)

g = freqmax.getmax(3)

list(g)
>> ['d', 'b', 'c']
```

## How it works

A doubly linked list is used to keep track of the keys. Each node in the list contains the key as well as the number of times that key has occurred so far. The nodes are ordered by the keys' frequencies.

This means that returning the k most frequently occuring keys is easy. Simply read k nodes from the head of the linked list, which takes O(k) time. However, updating the list as the frequencies of the keys increase is where the complexity gets pushed to.

When a key is seen, and its frequency needs to be incremented by 1, a hash table is first used to find the node holding that key. This node can then be spliced out of the linked list and spliced back in at a location where the ordering of the list is restored.

One way to do this would be to traverse the list upwards from the updated node, until we find a node whose key has a frequency greater that or equal to the updated node's frequency. Then, we can make the found node the parent of the updated node, and splice it back in.

The problem with this approach is that the search for the new parent could degenerate into a linear scan of the entire list, if there were long runs of keys each occuring with the same frequency. To surmount this, we maintain another hash table. This 'gaps' hash table maps from frequencies to the last node in the linked list that has a key with that frequency. Using this, after updating the frequency of a node, we can look up, in constant time, the new parent of this node. After splicing the node in, we update the gaps hash table to point to the spliced in node, as it is now the last node in the linked list with that frequency. 

As a result, the frequency of a key can be updated in O(1) time.

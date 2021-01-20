# Hash Tables

Two techniques to solve the collision

- chaining(simpliest)
  - hash to the same slot into the same linked list
  - CHAINED-HASH-INSERT(T, x)
    - insert x at the head of list T[h(x.key)]
  - CHAINED-HASH-SEARCH(T, k)
    - search for an element with key k in list T[h(k)]
  - CHAINED-HASH-DELETE(T, x)
    - delete x from thelist T[h(x.key)]
  - worst-case behavior of hashing with chaining: all n keys hash to the same slot.
- open addressing

### hash function

- good hash function: each key is equally likely to hash to any of the m slots, independently od where any other key has hashed to.
- the division method
  - h(k) = k mod m
- the multiplication method
  - two steps.first, we multiply the key k by a contant A in the range 0 < A < < 1 and exect the fractional part of kA. Then, we multiply this value by m and take the floor of the result.
  - h(k) = floor[ m(kA mod 1)]
- universal hashing

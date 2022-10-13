# Redis

Redis is an open source (BSD licensed), in-memory data structure store used as a database, cache, message broker, and streaming engine.

**Note**
    Redis actually is not a simple key-value store, it's more a datastructure server supporting differnent kind of values.

## Basics

- Commands

> set <KEY_VALUE> <STR_VALUE> - ADD or REPLACE existing key in the store.
> get <KEY_NAME>
> INCR <KEY_NAME> - Increments key value by 1
> DECR <KEY_NAME> - Decrements key value by 1
> INCRBY <KEY_NAME> <N> - Increments key value by n
> DECRBY <KEY_NAME> <N> - Decrements key value by n
> GESET <KEY_NAME> <DS_VALUE> - Set key to value, and returns original/old value of the key
> MSET <KEY_1> <VALUE_1> <KEY_2> <VALUE_2> ... - Set multiple keys - values
> MGET <KEY_1> <KEY_2> <KEY_3> - Returns values of a list of keys

**Note**
    Incrementation and decrementation operations will attempt to convert string values to integer before performing the operation.
    INCR|DECR|INCRBY|DECRBY are atomic, meaning that even multiple clients issuing INCR against the same key will never enter into a race condition.

### Supported Data Types

-- `Binary safe strings`
-- `List` (Linked List) : Collection of string elements sorted according to the order of insertion.
-- `Sets`: Collection of unique unsorted string elements
-- `Sorted Set`: Similar to `Sets` but where every string element is assoc with a floating number number called score. Element are sorted based on their score.
-- `Hashes` Dictionary<string, string>
-- Bit array (Bitmaps) - Redis provides through special command to manipulate string as bit array.
-- HyperLogLogs : Probabilistic data structure which is used in order to estimate the cardinality of a set.
-- `Streams`: append-only collections of map-like entries that provide an abstract log data type.

#### Redis Keys

**Note**
    The maximum allowed key size is 512 MB.

Redis keys are binary safe, this means that you can use any binary sequence as a key, from a string like "foo" to the content of a JPEG file. The empty string is also a valid key.

Rules:

- Very long keys are not a good idea. For instance a key of 1024 bytes is a bad idea not only memory-wise, but also because the lookup of the key in the dataset may require several costly key-comparisons

- Very short keys are often not a good idea. There is little point in writing "u1000flw" as a key if you can instead write "user:1000:followers". The latter is more readable and the added space is minor compared to the space used by the key object itself and the value object. While short keys will obviously consume a bit less memory, your job is to find the right balance.

#### Altering and querying Key space

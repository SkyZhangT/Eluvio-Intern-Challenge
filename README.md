# Eluvio-Intern-Challenge-Applications

## Task:

Look up information about items using their item ID in large batches.

<ul>
<li>Many repeating items</li>
<li>max 5 simultaneous requests</li>
</ul>

## Sample API request:

GET https://eluv.io/items/:id

Required headers:

<ul>
<li>Authorization: Base64(:id)</li>
</ul>

## Implementation

Since the task is mainly concentrating on the algorithm, I choose python as the implementation language. So that I can put all my effort on the task itself.

The runtime optimization is materialized from two different perspectives: 1. multi-threading the requests, 2. discard the repeating items.

1. I configured a multithreading environment that accepts at most 5 simultaneous works at the same time. So it should not get any 429 status codes. The result of each thread is awaited and returned to the main thread.

2. Since the items are coming in large batches, and there might be many repeating items, we need a way to memorize the visited item IDs. A simple set can do the job but I need to always consider the limitation of the user's device. Therefore, I came up with two highly configurable solutions that make a balance between space and runtime.

I implemented 2 types of caches to record the visited items: Least Recent Used Cache and Least Frequent Used Cache. Both of them have the same job: to hole visited items in a limited capacity, but the rule that decides what item they hold is a little bit different. Just like their name, when they used up their capacity, and a new item comes, the LRU cache will discard the least recently used item and record the incoming one. And the LFU cache will discard the least frequently used one and record the new one.

By implement them using double linked list and hashmap, the get method and put method both runs in O(1) time. And the space it take is O(n). Therefore, the performance of the cache is at the same level as the hashset, but have a limited capacity and a much more meaningful inventory.

After some experiment, both of the LRU and LFU cache outperforms the hashset (same capacity) on runtime. the LRU slightly outperforms LFU, but it mostly depends on the input.

## How to run the code.

<code> python3 main.py #filename# #LRU/LFU# #capacity#</code>

#filename# is the file that stores the large batch of item ID. It is required that each ID is separated by newline '\n'.

Type LRU or LFU to run the code with the type of cache.

#capacity# is an int value that represents the maximum space the cache is allowed to use.

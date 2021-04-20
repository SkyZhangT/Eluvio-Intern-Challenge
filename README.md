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

1. I configured a multithreading environment that accepts at most 5 simultaneous works at the same time. So it should not getting any 429 status codes. The result of each thread is awaited and returned to the main thread.

2. Since the items are coming in large batchs, I implemented 2 types of caches to record the visited items: Least Recent Used Cache and Least Frequent Used Cache. Both of them have the same job: to hole visited items in a limited capacity, but the rule that decide what item they hold is a little bit different. Just like their name, when they used up their capacity, and a new item comes, the LRU cache will discard the least recent used item and record the incoming one. And the LFU cache will discard the least frequently used one and record the new one.

## How to run the code.

<code> python3 main.py #filename# #LRU/LFU# #capacity#</code>

#filename# is the file that stores the large batch of item ID. It is required that each ID are separated by newline '\n'.

Type LRU or LFU to run the code with the type of cache.

#capacity# is a int value represents the maximum space the cache allowed to use.

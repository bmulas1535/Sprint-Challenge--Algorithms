#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) The _while_ loop has, by itself, a O(n^3) runtime complexity. However, as _a_ is increased by n^2 at each true condition, the worse case runtime is actually O(n). This is because _a_ is increased by n^2, effectively setting a max cap on the while loop runtime at _n_ operations. The total runtime for this code is _O(n)_


b) Line 17 `for i in range(n):` will run _n_ times, regardless of all other operations, so we start with a runtime of O(n). Following `j = 1`, the `while j < n` is going to proc n - 2 times due to i starting at 0, and j starting at 1 (it won't proc when j == n). When the condition procs true, j is incremented by 2 times it's current value. That reduces the runtime by half at each iteration (log(n)). The total runtime for this code is _O(n log(n))_


c) This code is quite simple. Each run will return `2 + f(n - 1)`, which will recurse. Once n = 0, the stack will fill back in with all of the accumulated `2 + n` values, with the final return being double the original input. The total runtime for this code is _O(n)_.

## Exercise II

The fastest way to determine the floor that at and above which eggs will break would be to start at any floor (it doesn't matter which), and throw 1 egg. If the egg breaks, you are above the floor, and that floor is below you. Travel down halfway between the floor you are on and the bottom. If the egg does not break, the floor is above you, and you are below the floor. Travel halfway between where you are and the top floor.

At the next landing, repeat the eggicide. The rules will remain the same. After the smallest amount of egg losses possible, you will eventually arrive at the point where there is only 1 floor option remaining, and this is the floor at or above which eggs will break. Problem solved.

You can use a binary search for this.
Assume that we have a binary tree with values ranging from 1 - 100 in a balanced tree.
floor f = 33 (these are really strong eggs)

We start at floor 52, so current_floor = 52
The first thing we do is toss an egg.

```
def throw_egg():
  if current_floor.value < f:
    egg = 'safe'
  else:
    egg = 'broken'
  return egg

>>> print(throw_egg())
>>> 'broken'
  ```

so if the egg breaks, we are at or above the floor, let's go down, which on the tree is to the left.
```
if egg = 'broken':
    last_floor = current_floor
    current_floor = current_floor.left
```
This will take us down halfway between our current floor and the bottom. From here, we can see what floor we're on, and then toss the egg.
```
>>> current_floor.value
>>> 26

>>> print(throw_egg())
>>> 'safe'
```

The egg is safe, so we are below the floor where it would break. We'll need to now travel halfway between 26 and 52.

```
if egg == 'safe':
    last_floor = current_floor
    current_floor = current_floor.right

>>> current_floor.value
>>> 39
```

We'll keep doing this until there are no more floors.

This would require us to keep a record of each node where a left split was taken, in the event that we land on the correct floor, split left, and then split right until we hit the bottom of the tree. In this special circumstance, the only correct option is the last node at which a left split was taken. We could reduce the amount of eggs that need to be thrown if there was some indication of us having chosen the correct floor before hitting the bottom of the tree.

The worst case runtime complexity for this operation is _O(log(n))_

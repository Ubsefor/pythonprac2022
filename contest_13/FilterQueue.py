#!/usr/bin/env python3

import asyncio

class FilterQueue(asyncio.Queue):

  def __contains__(self, filth):
    for i in filter(filth, self._queue):
      return True
    return False

  @property
  def window(self):
    # first obj of queue if its not empty
    return self._queue[0] if not self.empty() else None

  def later(self):
    if not self.empty():
      return self.put_nowait(self.get_nowait())
    else:
      raise asyncio.QueueEmpty

  # filth because I really hate this task, sorry(
  def get(self, filth=lambda x: None) :
    # if <%> in Queue
    if filth in self:
      while not filth(self.window):
        # resched to last
        self.later()

    return super().get()

# async def putter(n, queue):
#     for i in range(n):
#         await queue.put(i)

# async def getter(n, queue, filter):
#     for i in range(n):
#         await asyncio.sleep(0.1)
#         yield await queue.get(filter)

# async def main():
#     queue = FilterQueue(10)
#     asyncio.create_task(putter(20, queue))
#     async for res in getter(20, queue, lambda n: n % 2):
#         print(res)

# asyncio.run(main())

# async def putter(n, queue):
#     for i in range(n):
#         await queue.put(i)


# async def getter(n, queue):
#     for i in range(n):
#         await asyncio.sleep(0.03)
#         queue.later()
#         yield await queue.get()


# async def main():
#     queue = FilterQueue(10)
#     asyncio.create_task(putter(20, queue))
#     async for res in getter(20, queue):
#         print(res)

# asyncio.run(main())

# async def putter(n, queue):
#     for i in range(n):
#         await queue.put(i)

# async def getter(n, queue, filter):
#     res = 0
#     for i in range(n):
#         await asyncio.sleep(0)
#         res += (i % 7 - 3) * await queue.get(filter)
#     return res

# async def main():
#     queue = FilterQueue()
#     res = await asyncio.gather(putter(200, queue), getter(200, queue, lambda n: n % 2))
#     print(res[1])

# asyncio.run(main())

# EOF
#!/usr/bin/env python3

import asyncio
    
class NotifyEvent(asyncio.Event):

  def __init__(self):
    self.recvs = dict()
    super().__init__()

  def set(self, name=None):
    self.me = name

    if name in self.recvs:
      self.recvs[name] += 1
    else:
      self.recvs[name] = 1

    super().set()
    self.clear()

  async def wait(self):
    await super().wait()
    return self.me


async def task(name, notify):
  while True:
    recv = await notify.wait()

    if (recv == None):
      return

    if (recv == name):
      total = 0
      for i in notify.recvs:
        total += notify.recvs[i]
      print(str(name) + ": " + str(notify.recvs[name]) + " / " + str(total - notify.recvs[name]))     


# async def sender(names, notify):
#     for name in names:
#         notify.set(name)
#         await asyncio.sleep(0.1)
#         notify.clear()
#     notify.set()

# async def main():
#     notify = NotifyEvent()
#     tasks = {n: task(n, notify) for n in "12"}
#     targets = "1", "2", "2", "2", "2", "1", "2", "1", "1"
#     await asyncio.gather(*(list(tasks.values()) + [sender(targets, notify)]))

# asyncio.run(main())

# EOF

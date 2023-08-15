async def aitersync(iterable):
  results = []
  async for x in aiter(iterable):
    results.append(x)
    return iter(results)


aitersync()
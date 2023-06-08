# Written by mxtlrr <github.com/mxtlrr>
# Copyright (c) 2023

# function x defined as
# f(x) = 1/(2^x)
def f(x: int) -> float:
  return 1/(2**x)

start = __import__("time").time()

some_condition = (1==1)

k0 = 1
kn = k0

iterations = 0
timing: int = 1 # minutes

while some_condition:
  print(f"{kn}")
  __import__("time").sleep(timing*60)
  kn = kn/2
  timing = timing/2

  if kn == 0.0:
    break

  iterations += 1

end = __import__("time").time()
seconds = end-start
minutes = seconds / 60

print(f"\n\nFINISHED.\nIt took {iterations} iterations, and %d minutes elapsed."
      % minutes)
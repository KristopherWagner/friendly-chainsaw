test = [0, 2, 7, 0]
actual = [11, 11, 13, 7, 0, 15, 5, 5, 4, 4, 1, 1, 7, 1, 15, 11]

def getHighestValueIndex(mem):
  high = (0, mem[0])
  for i in range(1, len(mem)):
    if mem[i] > high[1]:
      high = (i, mem[i])

  return high

def distributeMemory(mem, highestIndex, amt):

  if amt > len(mem) - 1:
    # normal situation
  
    orig = amt % (len(mem) - 1)
    others = int(amt / (len(mem) - 1))

    for i in range(0, len(mem)):
      if i == highestIndex:
        mem[i] = orig
      else:
        mem[i] += others
  else:
    # not everything gets memory
    i = highestIndex + 1
    mem[highestIndex] = 0

    # in case the highest index is the last entry
    # this would be so much cleaner if python had a do..while
    if i >= len(mem):
      i = 0

    while amt > 0:
      mem[i] += 1
      amt -= 1

      i += 1
      if i >= len(mem):
        i = 0

  return mem

def checkForDuplicate(mem, history):
  retVal = False

  for i in range(0, len(history)):
    if mem == history[i]:
      retVal = True

  return retVal

def addToHistory(history, add):
  copy = []

  for item in add:
    copy.append(item)

  history.append(copy)

def main(mem):
  done = False
  history = []
  addToHistory(history, mem)
  i = 0

  while not done:
    (highestIndex, amt) = getHighestValueIndex(mem)
    mem = distributeMemory(mem, highestIndex, amt)
    done = checkForDuplicate(mem, history)
    addToHistory(history, mem)
    i += 1
  
  return i

if __name__ == "__main__":
  print(main(test))
  print(main(actual))

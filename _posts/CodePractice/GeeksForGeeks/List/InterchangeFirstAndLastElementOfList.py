import time
def interchage(inputList):
  '''using temp, this will interchange fists and last element of list'''

  temp = inputList[0]
  inputList[0]=inputList[len(inputList)-1]
  inputList[len(inputList)-1]= temp
  return inputList

def interchage1(inputList):
  '''using slice, this will interchange fists and last element of list'''

  inputList[0], inputList[-1]=inputList[-1], inputList[0]
  return inputList

def interchange2(inputList):
  '''using packing unpacking'''
  a,*b,c = inputList
  p,q = c,a
  return [p,*b,q]

if __name__ == '__main__':
  try:
    userList = [int(x) for x in input("enter comma separator integer value only =").split(',')]
    print(f'Entered list is {userList}')


    startTime = time.time()
    print(f'interchanged list using temp is = {interchage(userList)}')
    endTime = time.time()
    print(f'timeComplexity = {endTime-startTime}')

    print(f'Entered list is {userList}')

    startTime = time.time()
    print(f'interchanged list using slice is = {interchage1(userList)}')
    endTime = time.time()
    print(f'timeComplexity = {endTime - startTime}')

    print(f'Entered list is {userList}')

    startTime = time.time()
    print(f'interchanged list using slice is = {interchange2(userList)}')
    endTime = time.time()
    print(f'timeComplexity = {endTime - startTime}')

  except Exception as e:
    print(e)

import sys
import collections
#import time
#from testrandomcase import randomcase

#from worstcase import worst_case
#if odd -> man
#if even -> woman

# try deque collection for all lists
# std out for print
#strings = randomcase(1000)

strings = sys.stdin.readlines()

#start_time = time.time()
cases = int(strings[2].strip().split()[-1])
s = {}
preferences = collections.deque([True]) #odd id = man ... even id = woman
mQueue = collections.deque([])
wPaired = {}
count = 1

for i in range(4, len(strings)):
    row = strings[i].strip().split()[1:]
    row = collections.deque([int(x) for x in row])
    preferences.append(row)
    if count % 2 == 1:
        mQueue.append(count)
    count += 1

#Create Inverse List for woman

inverse = {}
for i in range(2, 2*cases+1,2):
    subInverse = {}
    place = 2
    for j in range(0,cases):
        subInverse[preferences[i][j]] = j
    inverse[i] = subInverse

while len(mQueue) != 0:
    manId = mQueue[0]


    for index in range(0,len(preferences[manId])):
        womenId = preferences[manId][index]
        #Woman not paired yet, so pair it and move on to next male
        if wPaired.get(womenId) is None:
            s[manId] = womenId
            wPaired[womenId] = manId
            mQueue.popleft()
            # after matching need to remove the woman from the male preference such that it doesnt repeat the selection when in queue again
            preferences[manId].remove(womenId)
            break
        else:
            #Woman Paired already compare if the woman wants current man or new man
            currentManId = wPaired.get(womenId)
            preferenceOfCurrentMan = inverse[womenId][currentManId]
            preferenceOfNewMan = inverse[womenId][manId]

            #The lower the number the higher the priority and we want to swap
            if preferenceOfNewMan < preferenceOfCurrentMan:
                s[manId] = womenId
                wPaired[womenId] = manId
                mQueue.popleft()
                mQueue.appendleft(currentManId)
                preferences[manId].remove(womenId)
                break


[ sys.stdout.write(str(i)+" "+str(s[i])+"\n") for i in range(1,2*cases+1,2)]


#sys.stdout.write("--- %s seconds ---" % (time.time() - start_time))
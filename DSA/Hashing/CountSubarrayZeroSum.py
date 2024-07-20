'''Problem Description
Given an array A of N integers.

Find the count of the subarrays in the array which sums to zero. Since the answer can be very large, return the remainder on dividing the result with 109+7'''

# A = [1, -1, -2, 2]

# A = [-1, 2, -1]
A = [-57,84,-317,-349,-4,297,65,36,-23,350,-219,-213,190,-86,-235,238,-326,35,149,106,115,394,200,32,-191,-386,236,-190,-108,-163,336,40,265,60,-167,-246,131,74,216,40,-231,287,-227,318,185,177,-74,-65,310,-182,-330,231,-395,-30,-272,0,300,-380,-51,178,153,97,-347,327,381,169,265,239,-216,143,208,-251,314,55,-369,-313,90,-312,93,181,-206,-175,171,115,52,-246,-99,151,-108,-73,-46,-84,23,51,-360,161,-341,-30,-393,-72,75,-138,-249,281,-251,63,-242,-302,-222,168,74,182,387,155,268,99,268,-63,-189,97,-16,63,-211,-246,-122,84,223,166,37,-290,361,282,-85,-135,-351,39,350,133,-358,-359,71,210,-87,-28,-259,-28,-14,-42,32,362,347,-220,-244,-255,-369,272,196,-254,-26,152,-384,186,72,-254,-100,316,84,147,-278,263,131,127,289,-78,-158,300,301,-280,-102,371,-63,345,156,286,-40,-390,195,120,-117,65,-56,-188,-359,286,-51,15,-195,91,-261,-378,184,-308,149,-190,-308,43,110,181,-268,264,218,-349,-281,235,310,-269,-296,272,192,-75,130,289,383,217,-316,67,-22,367,116,-207,-342,-16,-7,-6,-208,95,-197,272,178,-64,274,-370,-64,-3,-225,-308,218,257,308,-151,259,-182,388,123,-109,-280,-93,-151,-310,-44,288,74,-42,-337,333,210,204,214,327,-85,107,285,5,43,-145,263,208,-56,-93,90,-347,269,-334,137,-222,-328,21,227,187,154,358,71,277,-28,-224,196,-317,-82,324,360,-172,226,-239,-57,-231,-154,137,-205,-14,-209,-49,-281,-17,-57,169,-305,251,96,-333,-18,4,-62,195,85,-385,-14,293,-183,110,-69,-26,-41,-394,292,234,212,23,-176,179,-37,1,205,-246,245,-57,83,387,-301,84,394,-263,-246,-80,-233,-217,-246,-257,358,-86,-321,-51,-147,-295,-33,-340,160,-207,121,-150,-123,133,60,-212,278,-153,70,-66,-191,-365,-357,140,-383,-190,395,-87,41,-394,-124,-137,203,-317,-193,94,281,-40,-396]

def findZeroSumSubarray(A):
    pfsum = [0]*len(A)
    pfsum[0] = A[0]
    for i in range(1, len(A)):
        pfsum[i] = pfsum[i-1] + A[i]

    print('pfsum:', pfsum)
    count = 0

    print('count:', count)
    freq = {}
    freq[0] =1
    for i in pfsum:
        if i not in freq:
            freq[i] =1
        else:
            count +=freq[i]
            freq[i] +=1
    return count


print(findZeroSumSubarray(A))
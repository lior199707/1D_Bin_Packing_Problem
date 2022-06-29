
def howSum(capacity, weights, demand, error, memo={}):
    # if we already discovered a solution for the current capacity
    if capacity in memo: return memo[capacity]
    # if exceeded the capacity
    if capacity < 0: return None
    # if found a solution
    if capacity <= error:
        return []
    currDemand = eval(repr(demand))
    # run on all the items(weights)
    for i, weight in enumerate(weights):
        # print(numofRun)
        # choose an item only if it has demand
        if currDemand[i] > 0:
            # indicates we chose the item
            currDemand[i] -= 1
            # calculate the capacity left after choosing the item
            remainder = capacity - weight
            # find a solution for the new capacity
            remainderResult = howSum(remainder, weights, eval(repr(currDemand)), error, memo)
            # if the solution found, containing this item, is valid, doesn't exceed the capacity
            if remainderResult != None:
                # add it to the memoization
                memo[capacity] = [*remainderResult, weight]
                return memo[capacity]
            else:
                currDemand[i] += 1
    # if there isn't even 1 valid solution
    memo[capacity] = None
    return None


def howSumSolution(capacity, weights, demand):
    # find a combination that fills the bin completely
    memo = {}
    error = 0
    bin = howSum(capacity, weights, demand, 0, memo)
    # while didn't find a solution that fills the bin completely
    while bin is None:
        memo = {}
        error += 0.01
        # try finding a solution with a bigger error
        bin = howSum(capacity, weights, demand, error/100*capacity, memo)
    print('bin contains:', bin)
    size = len(weights)
    # create a list that every index indicates how many times we used each item to fill the bin
    res = [0 for x in weights]
    # for every weight in the weights list
    for index in range(size):
        # search for its appearances in the bin
        for weight in bin:
            # if found an appearance
            if weight == weights[index]:
                # indicate we used 1 of the specifies item
                res[index] += 1
    print('k list:', res, '\n')
    return res


"""bin = howSum(capacity, weights, eval(repr(demand)))
print(demand)
print(bin)"""


def cutStock(weights, demand, capacity):
    def getTotalWeight(d):
        """

        :param d: demand list
        :return: the total weight of the items in the demand list
        """
        totalSum = 0
        for weight, numOfPieces in zip(weights, d):
            totalSum += weight * numOfPieces
        return totalSum

    def printSolution(b):
        """
        prints the solution found for filing the bins

        :param b: bins list
        """
        totalOfEachItem = [0 for _ in demand]
        for index, bin in enumerate(b):
            print(f'bin number {index + 1}: {bin[0]}, total weight: {bin[1]} ,precentage filled: {bin[2]}%')
            totalOfEachItem = [x + y for x, y in zip(totalOfEachItem, bin[0])]
        print('total order:', totalOfEachItem)
        print('original demand:', demand)

    currDemand = eval(repr(demand))
    # calculate total weight of the demand
    currTotalWeight = getTotalWeight(currDemand)
    # number of bins used for solution
    totalSumOfBins = 0
    bins = []
    # while we can't store all the items of the demand in a single bin
    while currTotalWeight > capacity:
        # find a combination that fills the bin
        result = howSumSolution(capacity, weights, eval(repr(currDemand)))
        # checks how many times this combination can be used according to the demand
        numOfBins = min([x // y for x, y in zip(currDemand, result) if y != 0 and x != 0])
        # calculate the total weight of the items stored in the bin
        weightOfBin = getTotalWeight(result)
        # calculate the percentage of the bin that is loaded
        precentageOfBin = weightOfBin / capacity * 100
        # use 'numIfBins' bins to store the combination and update the total weight of the items in the demand list
        for _ in range(numOfBins):
            bins.append((result, weightOfBin, precentageOfBin))
            currTotalWeight -= weightOfBin
        # add the used number of bins to the total num of bins used for solution
        totalSumOfBins += numOfBins
        # update the demand
        currDemand = [i - (numOfBins * j) for i, j in zip(currDemand, result)]
    # if there are still items that need to be stored in the demand list store them in one more bin
    if currTotalWeight != 0:
        totalSumOfBins += 1
        bins.append((currDemand, currTotalWeight, currTotalWeight / capacity * 100))
    printSolution(bins)


weights = [992, 806, 771, 604, 496, 200, 120, 44]
demand = [10, 20, 5, 12, 8, 30, 20, 18]
capacity = 6000
cutStock(weights, demand, capacity)
demand = [6, 12, 18, 8, 10, 4, 12, 4, 10, 8]
weights = [1304, 978, 843, 702, 661, 504, 440, 319, 230, 175]
cutStock(weights, demand, capacity)
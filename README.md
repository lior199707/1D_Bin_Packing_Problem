# 1D Bin Packing Problem

The 1D bin cutting problem is a classic optimization problem in computer science and operations research. 
It involves cutting one-dimensional items of varying lengths according to the demand of the customer and storing them in a set of one-dimensional bins of a fixed length. 
The goal is to minimize the number of bins used while ensuring that all the items are cut to their required lengths without overlap.

## Description

The program converts said problem to a weights problem.
Because the problem is a 1 dimensional problem the items' lengths and the bin's capacity can be converted to items weigths and bin's weight capacity, 
the total items' length from the bin's total length is the same as the total items' weight from the total bin's weight.

### Input:

1) weights list: containing all the potential weights a item can have (uquivalent to all the different lengths an items can be cut to).
2) demand list: containing the customer's demand from each item.
* Both arrays shoud be of same size.
3) capacity: the total weight a bin can hold (equivalent to the total length of the bin).

For example:
```python
weights = [992, 806, 771, 604, 496, 200, 120, 44]
demand = [10, 20, 5, 12, 8, 30, 20, 18]
capacity = 6000
```
The weights array stores all the different weights/length of items.<br>
The demand array indicates that the customer wants 10 items of weight 992, 20 items of weight 806 and so on, so to conclude demand[i] is the amount nedded of the item: weights[i].
* If the customer wants 0 pieces of a specific item the demand of the item (the value of demand[i]) should be 0.

### Output

 prints the result of the minimum amount of containers needed for delivering the shippment and their actual content
 
 For example, given the above input the output is:
 
bin number 1: [5, 0, 0, 0, 0, 4, 2, 0], total weight: 6000 ,precentage filled: 100.0% <br>
bin number 2: [5, 0, 0, 0, 0, 4, 2, 0], total weight: 6000 ,precentage filled: 100.0% <br>
bin number 3: [0, 6, 0, 1, 0, 1, 3, 0], total weight: 6000 ,precentage filled: 100.0% <br>
bin number 4: [0, 6, 0, 1, 0, 1, 3, 0], total weight: 6000 ,precentage filled: 100.0% <br>
bin number 5: [0, 6, 0, 1, 0, 1, 3, 0], total weight: 6000 ,precentage filled: 100.0% <br>
bin number 6: [0, 2, 4, 1, 0, 0, 4, 5], total weight: 6000 ,precentage filled: 100.0% <br>
bin number 7: [0, 0, 0, 8, 2, 0, 0, 4], total weight: 6000 ,precentage filled: 100.0% <br>
bin number 8: [0, 0, 0, 0, 6, 12, 3, 6], total weight: 6000 ,precentage filled: 100.0% <br>
bin number 9: [0, 0, 1, 0, 0, 7, 0, 3], total weight: 2303 ,precentage filled: 38.38333333333333% <br>
total order: [10, 20, 5, 12, 8, 30, 20, 18] <br>
original demand: [10, 20, 5, 12, 8, 30, 20, 18] <br>

* In every bin array (for example: [5, 0, 0, 0, 0, 4, 2, 0]), the value of bin[i] is the number of the item: weigths[i] stored in the bin.

## Usage

clone or open the project in pycharm <br>
initialaize the wanted weights array, demand array and bin's capacity <br>

```python
if __name__ == "__main__":
    weights = [992, 806, 771, 604, 496, 200, 120, 44]
    demand = [10, 20, 5, 12, 8, 30, 20, 18]
    capacity = 6000
```

run the program or use the cutStock function as follows:

```python
cutStock(weights, demand, capacity)
```

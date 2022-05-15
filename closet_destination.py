# Implement an algorithm to find plan for the closest X destinations
"""
Given a list of N possible delivery destinations, implement an algorithm to create the delivery plan for the closest X destinations.

Input
The input to the function/method consisits of two arguments:
allLocations, a list where each element consists of a pair of integers representing the x and y coordinates of the delivery locations;
numDeliveries, an integer representing the number of deliveries that will be delivered in the plan(X).

Output
Return a list of elements where each element of the list represents the X closest x and y integer coordinates of the delivery destinations, where X represents the numDeliveries input. If there is one tie, use the location with the closest X coordinate. If no location is possible, return a list with an empty location - not just an empty list.

Note
The plan starts with the truck's location [0.0]. The distance of the truck from a delivery destination (x,y) is the square root of x^2 + y^2. If there are multiple ties, then return the locations starting with the closest X-coordinate as long as you satisfy returning exactly X delivery locations. The returned output can be in any order.
"""

from heapq import nsmallest


def shortestWay(allLocations: list[int], numDeliveries: int):
    def key(location):
        x, y = location
        return (x**2+y**2, x)

    result = nsmallest(numDeliveries, allLocations, key=key)
    if len(result) != numDeliveries:
        return [[]]
    return result


if __name__ == "__main__":

    print(shortestWay([[1, 2], [3, 4], [1, -1], [0, 2]], 2))

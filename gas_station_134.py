def canCompleteCircuit(gas, cost):
    """
    :type gas: List[int]
    :type cost: List[int]
    :rtype: int
    """
    ### The key point here is to understand: if we start with some point i, and if at point k we failed, then any point 
    ### between i and k will not be appropriate choice as well. Such starting point must has positive surplus, otherwise
    ### we will not be able to reach next point. Another thing is that is total surplus is negative, then there will 
    ### not be any solution. If positive, there should be?

    total_surplus = 0
    surplus = 0
    i = 0
    start = 0
    
    for i in range(len(gas)):
        total_surplus += gas[i] - cost[i] 
        surplus += gas[i] - cost[i] 
        if surplus < 0:
            start = i+1
            surplus = 0
    return -1 if (total_surplus < 0) else start



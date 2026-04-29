###########################
# 6.0002 Problem Set 1a: Space Cows 
# Name:
# Collaborators:
# Time:

from ps1_partition import get_partitions
import time

#================================
# Part A: Transporting Space Cows
#================================

# Problem 1
def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """
    # TODO: Your code here
    cow_text= open(filename,"r")#opean the text file 
    dic_cow={}#key,the name of the cow , and value the weight of the cow
    for line in cow_text:
        name,weight= line.split(",")
        dic_cow[name]=int(weight)
    cow_text.close()

    return dic_cow 

# Problem 2
def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    cows= sorted(cows.items(),key=lambda x:x[1],reverse=True)#sort the items and return tuples inside list
    list_trips=[]
    
    while cows:
        list_cow_trip=[]#list of cows taken in each trip
        added_weght= 0
        for cow in cows[:]:
            if added_weght+cow[1]<= limit:
                added_weght+= cow[1]
                list_cow_trip.append(cow[0])
                cows.remove(cow)
        list_trips.append(list_cow_trip)       
    return list_trips
     

    

# Problem 3
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips 
        Use the given get_partitions function in ps1_partition.py to help you!
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # TODO: Your code here
    list_cows=list(cows.keys())
    for trip in get_partitions(list_cows):
        
        broken=False
        count=0 #counts each succesful round from each trip
        for round in trip:
            weight_added= 0
            for cow in round:
                if weight_added+cows[cow]<=limit:
                    weight_added+= cows[cow]
                else:
                    broken=True
                    break
        
            if broken:
                break
        if not broken:
            return trip
             
                

        
# Problem 4
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    # TODO: Your code here
    dic_cows=load_cows("ps1_cow_data.txt")
    start_greedy= time.time()
    greedy_result=greedy_cow_transport(dic_cows,limit=10)
    end_greedy=time.time()
    start_brute= time.time()
    brute_result=brute_force_cow_transport(dic_cows,limit=10)
    end_brute=time.time()
    print("Greedy result:", greedy_result)
    print("Greedy trips:", len(greedy_result))
    print("Greedy time:", end_greedy - start_greedy)

    print("Brute result:", brute_result)
    print("Brute trips:", len(brute_result))
    print("Brute time:", end_brute - start_brute)
compare_cow_transport_algorithms()




    

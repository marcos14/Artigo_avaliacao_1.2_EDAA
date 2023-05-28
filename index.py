import time
import sys

import Utils as u
import SequentialSearch as ss
import BinarySearch as bs
import numpy as np
import pandas as pd

print("recursionlimit: ", sys.getrecursionlimit())
sys.setrecursionlimit(60000)
print("recursionlimit: ", sys.getrecursionlimit())


results = {
    "ss":[],
    "bs":[],
    "ll":[],
    "bst": []
    }

lista = []
num_inter_range = 3000
num_inter_fim = 30000
num_inter_atu = 0


while num_inter_atu < num_inter_fim:
    num_inter_atu += num_inter_range
    utils = u.Utils(num_inter_atu)
    
    #
    print("Init SequentialSearch with: ",num_inter_atu," elements")
    sSearch = ss.SequentialSearch()
    for index in range(100):
        st = time.process_time()
        sSearch.sequential_search(utils.rondom_search_item(), utils.get_in_array())
        et = time.process_time()
        res = (et - st) * 1000
        results["ss"].append({"lentgh": num_inter_atu, "time": res, "Comparisons": sSearch.getComparisons()})

    print('CPU Execution time:', res, 'milliseconds')
    print('Number of comparisons: ', sSearch.getComparisons())
    print("End SequentialSearch with: ",num_inter_atu," elements")
    
    #
    print("")
    #
    
    print("Init BinarySearch with: ",num_inter_atu," elements")
    bSearch = bs.BinarySearch()
    array = utils.get_in_array()
    for index in range(100):
        st = time.process_time()
        bSearch.search(utils.rondom_search_item(), array, 0, len(array) - 1)
        et = time.process_time()
        res = (et - st) * 1000
        results["bs"].append({"lentgh": num_inter_atu, "time": res, "Comparisons": bSearch.getComparisons()})
    print('CPU Execution time:', res, 'milliseconds')
    print('Number of comparisons: ', bSearch.getComparisons())
    print("End BinarySearch with: ",num_inter_atu," elements")

    #
    print("")
    #

    print("Init LinkedList with: ",num_inter_atu," elements")
    array = utils.get_in_linked_list()
    for index in range(100):
        st = time.process_time()
        array.index(utils.rondom_search_item())
        et = time.process_time()
        res = (et - st) * 1000
        results["ll"].append({"lentgh": num_inter_atu, "time": res, "Comparisons": array.getComparisons()})
    print('CPU Execution time:', res, 'milliseconds')
    print('Number of comparisons: ', array.getComparisons())
    print("End LinkedList with: ",num_inter_atu," elements")

    #
    print("")
    #

    print("Init BinarySearchTree with: ",num_inter_atu," elements")
    array = utils.get_in_binary_tree()
    for index in range(100):
        st = time.process_time()
        array.find_node(utils.rondom_search_item())
        et = time.process_time()
        res = (et - st) * 1000
        results["bst"].append({"lentgh": num_inter_atu, "time": res, "Comparisons": array.getComparisons(), "height": array.height(0)})
    print('CPU Execution time:', res, 'milliseconds')
    print('Number of comparisons: ', array.getComparisons())
    print("End BinarySearchTree with: ",num_inter_atu," elements")
  
    
#print("results: ", results)

#ss
print("results: ", results["ss"])


data_show = {}
data_show["Nome"] = ["Sequential Search", "Binary Search",
                     "Linked List Search", "Binary Search Tree"]

data_show["AVG Time"] = [
    np.average([item["time"] for item in results["ss"] if item["lentgh"] == 3000]), 
    np.average([item["time"] for item in results["bs"] if item["lentgh"] == 3000]), 
    np.average([item["time"] for item in results["ll"] if item["lentgh"] == 3000]),
    np.average([item["time"] for item in results["bst"] if item["lentgh"] == 3000])
    ]


data_show["AVG Comparisons"] = [
    np.average([item["Comparisons"] for item in results["ss"] if item["lentgh"] == 3000]), 
    np.average([item["Comparisons"] for item in results["bs"] if item["lentgh"] == 3000]), 
    np.average([item["Comparisons"] for item in results["ll"] if item["lentgh"] == 3000]),
    np.average([item["Comparisons"] for item in results["bst"] if item["lentgh"] == 3000])
    ]

data_show["STD Time"] = [
    np.std([item["time"] for item in results["ss"] if item["lentgh"] == 3000]), 
    np.std([item["time"] for item in results["bs"] if item["lentgh"] == 3000]), 
    np.std([item["time"] for item in results["ll"] if item["lentgh"] == 3000]),
    np.std([item["time"] for item in results["bst"] if item["lentgh"] == 3000])
    ]


data_show["STD Comparisons"] = [
    np.std([item["Comparisons"] for item in results["ss"] if item["lentgh"] == 3000]), 
    np.std([item["Comparisons"] for item in results["bs"] if item["lentgh"] == 3000]), 
    np.std([item["Comparisons"] for item in results["ll"] if item["lentgh"] == 3000]),
    np.std([item["Comparisons"] for item in results["bst"] if item["lentgh"] == 3000])
    ]

data_show["Worse Time"] = [
    np.max([item["time"] for item in results["ss"] if item["lentgh"] == 3000]), 
    np.max([item["time"] for item in results["bs"] if item["lentgh"] == 3000]), 
    np.max([item["time"] for item in results["ll"] if item["lentgh"] == 3000]),
    np.max([item["time"] for item in results["bst"] if item["lentgh"] == 3000])
    ]


data_show["Worse Comparisons"] = [
    np.max([item["Comparisons"] for item in results["ss"] if item["lentgh"] == 3000]), 
    np.max([item["Comparisons"] for item in results["bs"] if item["lentgh"] == 3000]), 
    np.max([item["Comparisons"] for item in results["ll"] if item["lentgh"] == 3000]),
    np.max([item["Comparisons"] for item in results["bst"] if item["lentgh"] == 3000])
    ]

# "ss"
# "bs"
# "ll"
# "bst"


df = pd.DataFrame(data_show)

print(df)

print("average", np.average([item["height"] for item in results["bst"] if item["lentgh"] == 3000]))
print("std", np.std([item["height"] for item in results["bst"] if item["lentgh"] == 3000]))
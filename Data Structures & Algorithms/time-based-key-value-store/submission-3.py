class TimeMap:

    def __init__(self):
        self.hashmap = collections.defaultdict(list) #key : [(timestamp, value)]
   
    #O(1) time and O(n * m) space
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hashmap[key].append((timestamp, value))


    #O(logn) time
    def get(self, key: str, timestamp: int) -> str:
        listToSearch = self.hashmap[key]

        #if list is empty or the timestamp cant exist within the list
        if not listToSearch or listToSearch[0][0] > timestamp:
            return ""

        l, r = 0, len(listToSearch) - 1
        while l <= r:
            m = (l + r) // 2
            
            if listToSearch[m][0] > timestamp:
                r = m - 1
            elif listToSearch[m][0] < timestamp:
                l = m + 1
            else:
                return listToSearch[m][-1]
        
        #if we never find the value in the list then r sits on the right most index that has the  last value that is less than the target value
        return listToSearch[r][-1]
        


        

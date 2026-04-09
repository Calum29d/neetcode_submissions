class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        groups = {}

        for word in strs:
            key = "".join(sorted(word)) #makes a key that will be the same for every word that contains the same letters
            
            if key not in groups:
                groups[key] = [] #initialise empty array for group
                groups[key].append(word) #adds the first word to the array group
            else:
                groups[key].append(word) #adds another word to the array group, but doesnt need to create a new array 

        return list(groups.values()) #converts the hashmap of keys and values into an array of values from each key


        
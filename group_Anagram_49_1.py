#first attempt code used anagram logic that if sorted version of string same then 
#those strings are anaagrams of each other and you can map what strings have same sortedString 
#in a hashmap and then append all of the groups int a list
class Solution(object):
    def groupAnagrams(self, strs):
        listSol = []
        stringMap = {}
        for string in strs:
            sortedString = "".join(sorted(string))
            if sortedString in stringMap:
                stringMap[sortedString].append(string)

            else:
                stringMap[sortedString]  = [string]
        
        for sortedStringKey in stringMap:
            listSol.append(stringMap[sortedStringKey])
        return listSol
     
"""
SudoCode understanding

- First found out how you can sort a string in python using “.join(sorted)) function
- Made a map of each sortedString has what corresponding strings if two strings have the same sorted string then they will be added to same sorted string key and keep appending if thats the case
- At the end of making the sorted stringmap, combine all values into one big list of a list of strings.
"""

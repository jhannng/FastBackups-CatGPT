"""
    Written By: Jui Kai Hang
    Copyright (c) 2023 Jui Kai Hang
"""
from Application.fast_backups import FastBackups
from Application.cat_gpt import CatsTrie

class Main():

    def fast_backups_driver(self):
        # Fast Backups
        connections = [(0, 1, 3000), (1, 2, 2000), (1, 3, 1000), (0, 3, 2000), (3, 4, 2000), (3, 2, 1000)]
        maxIn = [5000, 3000, 3000, 3000, 2000]
        maxOut = [5000, 3000, 3000, 2500, 1500]
        origin = 0
        targets = [4, 2]
        
        driver = FastBackups()
        result = driver.max_throughput(connections, maxIn, maxOut, origin, targets)
        print(result)
        
    def cat_gpt_driver(self):
        # CatGPT
        sentences = ["abc", "abazacy", "dbcef", "xzz", "gdbc", "abazacy", "xyz", "abazacy", "dbcef", "xyz", "xxx", "xzz"]
        mycattrie = CatsTrie(sentences)
        
        prompt = "ab"
        result = mycattrie.autoComplete(prompt)
        print(result)
        
        prompt = "a"
        result = mycattrie.autoComplete(prompt)
        print(result)
        
        prompt = "dbcef"
        result = mycattrie.autoComplete(prompt)
        print(result)
        
        prompt = "dbcefz"
        result = mycattrie.autoComplete(prompt)
        print(result)
        
        prompt = "ba"
        result = mycattrie.autoComplete(prompt)
        print(result)
        
        prompt = "x"
        result = mycattrie.autoComplete(prompt)
        print(result)
        
        prompt = ""
        result = mycattrie.autoComplete(prompt)
        print(result)
        
        sentences = ["abc", "abczacy", "dbcef", "xzz", "gdbc", "abczacy", "xyz", "abczacy", "dbcef", "xyz", "xxx", "xzz"]
        mycattrie = CatsTrie(sentences)
        
        prompt = "abc"
        result = mycattrie.autoComplete(prompt)
        print(result)
        
if __name__ == "__main__":
    main = Main()
    main.fast_backups_driver()
    main.cat_gpt_driver()
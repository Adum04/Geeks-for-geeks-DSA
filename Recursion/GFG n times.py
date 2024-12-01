def printGfg(self, n):
    if n < 1:
        return
    print("GFG", end=" ")
    self.printGfg(n - 1)

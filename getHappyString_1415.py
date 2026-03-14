class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        S = 3*2**(n-1)
        if k > S:
            return ""
        ck = k
        klist = []
        for i in range(n):
            klist.append(k)
            if k % 2 == 1:
                k = (k // 2) + 1
            else:
                k = k//2
        ltlst = ["a","b","c"]
        idx = 0
        count = 0
        nword = ""
        klist.sort()
        #swich the idx logic with right and left.
        for j in klist:
            if count == 0:
                idx = j - 1
                nword = nword + ltlst[idx]
                last = ltlst[idx]
            else:
                if last == "a":
                    if j % 2 == 1:
                        last = "b"
                    else:
                        last = "c"
                elif last == "b":
                    if j % 2 == 1:
                        last = "a"
                    else:
                        last = "c"
                elif last == "c":
                    if j % 2 == 1:
                        last = "a"
                    else:
                        last = "b"
                nword += last

            count += 1
            
        return nword

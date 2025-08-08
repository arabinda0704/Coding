class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # if not digits:
        #     return []

        # res = [""]
        # digitToChar = {
        #     "2": "abc",
        #     "3": "def",
        #     "4": "ghi",
        #     "5": "jkl",
        #     "6": "mno",
        #     "7": "qprs",
        #     "8": "tuv",
        #     "9": "wxyz",
        # }

        # for digit in digits:
        #     tmp = []
        #     for curStr in res:
        #         for c in digitToChar[digit]:
        #             tmp.append(curStr + c)
        #     res = tmp
        # return res

        #Bacttrack

        res = []
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }

        def backtrack(i, curStr):
            if i == len(digits):
                res.append(curStr)
                return
            for c in digitToChar[digits[i]]:
                backtrack(i + 1, curStr + c)

        if digits:
            backtrack(0, "")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  

        return res
        
class Solution:
    def printVertically(self, s: str) -> List[str]:
        result = s.split()

        n, max_val = len(result), max([len(i) for i in result])

        for i in range(n):
            result[i] += (max_val-len(result[i]))*"*"

        answer = []

        for j in range(max_val):
            str1 = ""
            for i in range(n):
                str1 += result[i][j]
            answer.append(str1)

        for i in range(len(answer)):
            answer[i] = answer[i].replace("*"," ")
            answer[i] = answer[i].rstrip()

        return answer
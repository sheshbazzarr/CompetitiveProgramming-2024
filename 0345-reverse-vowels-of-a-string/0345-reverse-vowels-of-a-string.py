class Solution:
    def reverseVowels(self, s: str) -> str:
        string_list = list(s)
        i, j = 0, len(string_list) - 1
        vowels = set("aeiouAEIOU")

        while i < j:
            while i < j and string_list[i] not in vowels:
                i += 1
            while i < j and string_list[j] not in vowels:
                j -= 1

            string_list[i], string_list[j] = string_list[j], string_list[i]
            i += 1
            j -= 1

        return "".join(string_list)
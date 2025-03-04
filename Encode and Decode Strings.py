class Solution:

    def encode(self, strs: list[str]) -> str:
        result = ""
        for elem in strs:
            result += chr(len(elem)) + elem
        return result

    def decode(self, s: str) -> list[str]:
        """
        FIRST SOLUTION ))))
        strs = []
        i = 0
        tim_s = ''
        while i < len(s):
            if 'a' <= s[i] <= 'z':
                tim_s += s[i]
            else:
                if tim_s != '':
                    strs.append(tim_s)
                    tim_s = ''
            i += 1
        return strs
        """

        result = []
        i = 0
        while i < len(s):
            length = ord(s[i])
            i += 1
            result.append(s[i : i + length])
            i += length
        return result


settings = Solution()

strs = ["neet", "code", "love", "you"]

s = "♦neet♦code♦love♥you"

# print(settings.encode(strs))
print(settings.decode(settings.encode(strs)))

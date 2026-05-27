class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            result += f"{str(s)}`"
        print(result)
        return result

    def decode(self, s: str) -> List[str]:
        results = []
        result = ""
        for char in s:
            if char == "`":
                results.append(result)
                result = ""
            else:
                result += char
        return results
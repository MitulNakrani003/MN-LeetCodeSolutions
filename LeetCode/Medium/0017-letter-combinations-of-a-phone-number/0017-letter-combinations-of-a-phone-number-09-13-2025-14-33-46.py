class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        
        letter_map = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz",
        }
        
        all_combinations = []

        def backtrack(index, path):
            if len(path) == len(digits):
                all_combinations.append("".join(path))
                return
            possible_letters = letter_map[digits[index]]
            for letter in possible_letters:
                path.append(letter)
                backtrack(index+ 1, path)
                path.pop()
        
        backtrack(0,[])
        return all_combinations

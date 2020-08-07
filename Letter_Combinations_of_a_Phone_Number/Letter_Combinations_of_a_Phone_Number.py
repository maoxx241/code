class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        table = {
            '1': '',
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
            '0': ' '}
        all_combinations = [''] if digits else []
        for digit in digits:
            current_combinations = []
            for letter in table[digit]:
                for combination in all_combinations:
                    current_combinations.append(combination + letter)
            all_combinations = current_combinations
        return all_combinations
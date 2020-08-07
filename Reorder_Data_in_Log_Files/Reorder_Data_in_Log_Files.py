class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter = []
        digit=[]
        for log in logs:
            if log.split()[1].isdigit():
                digit.append(log)
            else:
                letter.append(log)
        #letter.sort(key=lambda x: x.split()[0])
        letter.sort(key=lambda letter: (letter.split()[1:],letter.split()[0]))
        return letter+digit
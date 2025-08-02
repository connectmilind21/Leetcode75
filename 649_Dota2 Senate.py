class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)
        radient = deque()
        dire = deque()

        for i, s in enumerate (senate):
            if s == "R":
                radient.append(i)
            else:
                dire.append(i)
        
        while dire and radient:
            rad_index = radient.popleft()
            dire_index = dire.popleft()

            if rad_index < dire_index:
                radient.append(rad_index + n)
            else:
                dire.append(dire_index + n)
        return "Radiant" if radient else "Dire"
        
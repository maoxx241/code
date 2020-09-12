class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        if hour==12: hour=0
        mp=360*minutes/60
        hp=360*hour/12+(minutes/60)*(360/12)
        return min(360-abs(hp-mp),abs(hp-mp))

from collections import defaultdict

class Analyzer:
    def __init__(self, logs):
        self.logs=logs

    def durations(self):
        d=defaultdict(list)
        stack={}
        for ts,e in self.logs:
            if "ENTER" in e:
                stack[e]=ts
            elif "EXIT" in e:
                en=e.replace("EXIT","ENTER")
                if en in stack:
                    d[en].append(ts-stack[en])
        return d


class Parser:
    def __init__(self, path):
        self.path = path

    def parse(self):
        logs=[]
        with open(self.path) as f:
            for l in f:
                if l.startswith("LOG"):
                    _,ts,e=l.strip().split(",")
                    logs.append((int(ts),e))
        return logs

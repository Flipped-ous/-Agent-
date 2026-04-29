
class Optimizer:
    def __init__(self, d):
        self.d=d

    def suggest(self):
        res=[]
        for k,v in self.d.items():
            avg=sum(v)/len(v)
            if avg>5:
                res.append(f"{k}: latency high -> split or DMA")
            if "IMU" in k:
                res.append(f"{k}: raise priority")
        return res

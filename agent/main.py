
from core.parser import Parser
from core.analyzer import Analyzer
from core.optimizer import Optimizer
from ui.visual import show

def main():
    logs=Parser("../data/log.txt").parse()
    d=Analyzer(logs).durations()

    print("=== Metrics ===")
    for k,v in d.items():
        print(k, sum(v)/len(v))

    print("\n=== Suggestions ===")
    for s in Optimizer(d).suggest():
        print(s)

    show(d)

if __name__=="__main__":
    main()


import matplotlib.pyplot as plt

def show(d):
    names=[]
    vals=[]
    for k,v in d.items():
        names.append(k)
        vals.append(sum(v)/len(v))
    plt.bar(names,vals)
    plt.xticks(rotation=30)
    plt.title("Latency")
    plt.show()

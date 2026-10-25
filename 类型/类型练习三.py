def analyze(scores:list[int])->tuple[int,float,int,int]:
    total=sum(scores)
    return (total,total/len(scores),max(scores),min(scores))

def show_report(name:str, scores:list[int])->None:
    a,b,c,d = analyze(scores)
    print(f"{name}:总分 {a}, 平均分{b:.1f}, 最高{c}, 最低{d}")


show_report("小明",[88,92,75])
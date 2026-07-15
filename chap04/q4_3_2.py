numbers=[1,2,3,4]
def func_hint(*args):
    print("args:",args)
    print("len(args):",len(args))

func_hint(*numbers)
"""実行結果
args: (1, 2, 3, 4)
len(args): 4
"""

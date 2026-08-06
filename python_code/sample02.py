def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    return x/y


def opreation1(x,y):
    return [x+y, x-y, x*y, x/y]

def opreation2(x,y):
    return x+y, x-y, x*y, x/y
  
print(opreation1(10,5))
print(f"add={opreation2(10,5)[0]}, sub={opreation2(10,5)[1]}, mul={opreation2(10,5)[2]}, div={opreation2(10,5)[3]}")
  
  
  
  
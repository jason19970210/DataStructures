import datetime

def hanoiH(n, a, b, c):
    param_stack_recursion2 = [[n, a, b, c]]

    while param_stack_recursion2:
        m, pa, pb, pc = param_stack_recursion2.pop()
        
        param_stack_recursion1 = []
        while True:
            if m == 1:
                #print(pa, pc) # hanoiH(1, A, B, C)
                
                # hanoiH(m - 1, A, C, B) is completed
                leng = len(param_stack_recursion2)
                while param_stack_recursion1:
                    m = m + 1
                    sa, sb, sc = param_stack_recursion1.pop() 
                    
                    # hanoiH(m - 1, B, A, C)
                    param_stack_recursion2.insert(leng, [m - 1, sb, sa, sc])
                      
                if param_stack_recursion2:
                    _, mb, ma, mc = param_stack_recursion2[-1] 
                    #print(ma, mc) # move A to C
                
                break
            
            param_stack_recursion1.append([pa, pb, pc])
            # hanoi(m - 1, A, C, B)
            m = m - 1
            pa, pb, pc = pa, pc, pb

n = 3
while n < 68 :
    start = datetime.datetime.now()
    hanoiH(n, 'A', 'B', 'C')
    end = datetime.datetime.now()
    print(n,end-start)
    n = n + 5
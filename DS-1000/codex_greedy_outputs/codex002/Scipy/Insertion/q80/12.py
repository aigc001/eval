
for t in range (4):
    def const(x):    
        y=x[t]
        return y
    cons.append({'type':'ineq', 'fun': const})

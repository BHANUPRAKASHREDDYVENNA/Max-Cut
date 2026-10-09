import numpy as np

def qaoa_state(gamma,beta,edges,n):
    state=np.ones(2**n,dtype=complex)/np.sqrt(2**n)
    for idx in range(2**n):
        bits=[(idx>>q)&1 for q in range(n)]
        cost=sum(w for u,v,w in edges if bits[int(u)]!=bits[int(v)])
        state[idx]*=np.exp(-1j*gamma*cost)
    c=np.cos(beta)
    s=-1j*np.sin(beta)
    for q in range(n):
        step=2**q
        for base in range(0,2**n,2*step):
            for off in range(step):
                i,j=base+off,base+off+step
                a,b=state[i],state[j]
                state[i]=c*a+s*b
                state[j]=s*a+c*b
    return state

def probabilities(state):
    p=np.abs(state)**2
    return p/p.sum()

def optimize_p1(edges,n,grid=21):
    best=(-1.0,0.0,0.0)
    for gamma in np.linspace(0,np.pi,grid):
        for beta in np.linspace(0,np.pi/2,grid):
            p=probabilities(qaoa_state(gamma,beta,edges,n))
            exp=0.0
            for idx,prob in enumerate(p):
                bits=[(idx>>q)&1 for q in range(n)]
                exp += prob*sum(w for u,v,w in edges if bits[int(u)]!=bits[int(v)])
            if exp>best[0]:
                best=(exp,gamma,beta)
    return best

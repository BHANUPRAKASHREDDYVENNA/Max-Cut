from collections import deque
def shortest_path(n,coupling,src,dst):
    adj={i:[] for i in range(n)}
    for a,b in coupling: adj[a].append(b); adj[b].append(a)
    q=deque([src]); prev={src:None}
    while q:
        u=q.popleft()
        if u==dst: break
        for v in adj[u]:
            if v not in prev: prev[v]=u; q.append(v)
    if dst not in prev: raise ValueError("unreachable")
    path=[]; u=dst
    while u is not None: path.append(u); u=prev[u]
    return path[::-1]
def route_edges(edges,p):
    swaps=twoq=0
    for u,v,w in edges:
        d=len(shortest_path(p["num_qubits"],p["coupling_map"],int(u),int(v)))-1
        swaps+=max(0,d-1); twoq+=1+3*max(0,d-1)
    return {"swaps":swaps,"two_qubit_ops":twoq,"depth_proxy":max(1,2*len(edges)+4*swaps)}

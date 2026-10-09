import numpy as np
from .qaoa import qaoa_state,probabilities
from .problem import cut_value
from .routing import route_edges
def benchmark(p,edges,n,gamma,beta,optimum,shots,seed):
    prob=probabilities(qaoa_state(gamma,beta,edges,n)); route=route_edges(edges,p)
    rng=np.random.default_rng(seed); counts=rng.multinomial(shots,prob)
    p2=p["noise"]["two_qubit_error"]; pr=p["noise"]["readout_error"]
    pflip=min(.45,1-(1-p2)**max(1,route["two_qubit_ops"]/max(1,n)))
    total=0.; hits=0; total_cut=0.
    for idx,c in enumerate(counts):
        bits=np.array([(idx>>q)&1 for q in range(n)],dtype=int)
        for _ in range(int(c)):
            b=bits.copy(); b[rng.random(n)<pflip]^=1; b[rng.random(n)<pr]^=1
            val=cut_value(b,edges); total_cut+=val; hits+=int(val>=optimum-1e-12); total+=1
    optp=hits/total
    return {"processor":p["name"],"noisy_expected_cut":total_cut/total,"approximation_ratio":(total_cut/total)/optimum,"optimal_cut_probability":optp,"standard_error":np.sqrt(optp*(1-optp)/total),"shots":int(total),"swaps":route["swaps"],"two_qubit_ops":route["two_qubit_ops"],"depth_proxy":route["depth_proxy"],"physical_qubits":p["num_qubits"],"proxy_bitflip_probability":pflip}

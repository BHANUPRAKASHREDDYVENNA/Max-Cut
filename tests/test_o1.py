from src.problem import brute_force_optimum
from src.routing import route_edges
def test_reference():
    value,bits=brute_force_optimum(4,[[0,1,1],[1,2,1],[2,3,1],[3,0,1]])
    assert value==4 and len(bits)==4
def test_routing():
    x=route_edges([[0,4,1],[1,3,1]],{"num_qubits":5,"coupling_map":[[0,1],[1,2],[2,3],[3,4]]})
    assert x["swaps"]>0 and x["two_qubit_ops"]>2

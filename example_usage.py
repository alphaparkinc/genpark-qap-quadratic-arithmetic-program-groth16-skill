from client import QAPReduction

qap = QAPReduction(roots=[1, 2])
valid = qap.check_qap_identity(a_eval=3, b_eval=4, c_eval=12, x=1)
print(f"QAP divisibility valid at root x=1: {valid}")

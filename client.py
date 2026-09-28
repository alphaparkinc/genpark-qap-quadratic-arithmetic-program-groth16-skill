"""Quadratic Arithmetic Program (QAP) Engine.
100% Python Standard Library.
"""

class QAPReduction:
    """Quadratic Arithmetic Program reduction from R1CS constraints."""
    PRIME = 2147483647

    def __init__(self, roots=None):
        self.roots = roots if roots else [1, 2]

    def compute_vanishing_poly(self, x):
        res = 1
        for r in self.roots:
            res = (res * (x - r)) % self.PRIME
        return res

    def check_qap_identity(self, a_eval, b_eval, c_eval, x):
        lhs = (a_eval * b_eval - c_eval) % self.PRIME
        t_val = self.compute_vanishing_poly(x)
        if t_val == 0:
            return lhs == 0
        return (lhs % t_val) == 0

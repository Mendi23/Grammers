"""generate

Usage:
    generate.py <grammar> [-n NUM] [-h] [-t]

Options:
    -h --help               Show this message
    -n NUM --number=NUM     number of lines [default: 1]
    -t                      bla bla

"""

from collections import defaultdict
import random


class PCFG(object):
    def __init__(self):
        self._rules = defaultdict(list)
        self._sums = defaultdict(float)

    def add_rule(self, lhs, rhs, weight):
        assert (isinstance(lhs, str))
        assert (isinstance(rhs, list))
        self._rules[lhs].append((rhs, weight))
        self._sums[lhs] += weight

    @classmethod
    def from_file(cls, filename):
        grammar = PCFG()
        with open(filename) as fh:
            for line in fh:
                line = line.split("#")[0].strip()
                if not line: continue
                w, l, r = line.split(None, 2)
                r = r.split()
                w = float(w)
                grammar.add_rule(l, r, w)
        return grammar

    def is_terminal(self, symbol): return symbol not in self._rules

    def gen(self, symbol, flag):
        if self.is_terminal(symbol):
            return symbol
        expansion = (self.gen(s, flag) for s in self.random_expansion(symbol))

        if flag:
            return self.build_formatted_arr(symbol, expansion)
        return " ".join(expansion)

    def build_formatted_arr(self, symbol, expansion):
        WIDTH = 25
        res = [f"({symbol}"]
        indent = " " * len(res[-1])
        for s in expansion:
            if not isinstance(s, list): # terminal
                s = (s,)
            for x in s:
                llen = len(res[-1]) + 1
                if llen + len(x) < WIDTH:
                    indent = " " * llen
                    res[-1] += " " + x
                else:
                    res.append(indent + x)
        res[-1] += ")"
        return res

    def random_sent(self, flag):
        res = self.gen("ROOT", flag)
        return "\n".join(res) if flag else res

    def random_expansion(self, symbol):
        """
        Generates a random RHS for symbol, in proportion to the weights.
        """
        p = random.random() * self._sums[symbol]
        for r, w in self._rules[symbol]:
            p = p - w
            if p < 0:
                return r


if __name__ == '__main__':
    import docopt

    args = docopt.docopt(__doc__)

    grammarfile = args["<grammar>"]
    num = int(args["--number"])
    pcfg = PCFG.from_file(grammarfile)

    for _ in range(num):
        print(pcfg.random_sent(args["-t"]))

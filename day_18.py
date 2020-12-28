import fileinput
import re
from functools import partial, reduce
from operator import add, mul

OPERATORS = {'+': add, '*': mul}
SIMPLE_EXPR_RE = re.compile(r'\([^()]+\)')
ADD_WITH_PARENTHESES_RE = re.compile(r'(\()?(\d+ \+ \d+)(?(1)\))')


def main():
    exprs = list(fileinput.input())

    print(part_1(exprs))
    print(part_2(exprs))


def eval_simple_expr(expr):
    return reduce(lambda acc, x: acc(int(x)) if isinstance(acc, partial) else partial(OPERATORS[x], acc),
                  expr.split(), partial(add, 0))


def eval_match_expr(match_expr):
    return str(eval_simple_expr(match_expr.group()[1:-1]))


def eval_expr(expr, add_before_mul=False):
    if add_before_mul:
        expr = ADD_WITH_PARENTHESES_RE.sub(r'(\2)', expr)
    expr, number_of_subs_made = SIMPLE_EXPR_RE.subn(eval_match_expr, expr)

    while number_of_subs_made > 0:
        if add_before_mul:
            expr = ADD_WITH_PARENTHESES_RE.sub(r'(\2)', expr)
        expr, number_of_subs_made = SIMPLE_EXPR_RE.subn(eval_match_expr, expr)

    return eval_simple_expr(expr)


def part_1(exprs):
    return sum(map(eval_expr, exprs))


def part_2(exprs):
    return sum(map(partial(eval_expr, add_before_mul=True), exprs))


if __name__ == '__main__':
    main()

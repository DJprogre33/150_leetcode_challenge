class Solution:
    """link to the problem: https://leetcode.com/problems/evaluate-reverse-polish-notation/"""
    @staticmethod
    def v1_eval_rpn(tokens: list[str]) -> int:
        """
        Time complexity: O(n) 74ms beats 80.53%
        Space complexity: 0(n) 16.69mb beats 83.80%
        """
        operators = {
            "+": lambda x, y: x + y,
            "-": lambda x, y: x - y,
            "*": lambda x, y: x * y,
            "/": lambda x, y: int(x / y)
        }
        stack = []

        for token in tokens:
            if token in "+-*/":
                n1, n2 = stack.pop(), stack.pop()
                result = operators[token](n2, n1)
                stack.append(result)
            else:
                stack.append(int(token))
        return stack[0]

    @staticmethod
    def v2_eval_rpn(tokens: list[str]) -> int:
        """
        Time complexity: O(n) 68ms beats 93.60%
        Space complexity: 0(n) 16.59mb beats 98.78%
        """
        stack = []

        for token in tokens:
            if token == "+":
                n1, n2 = stack.pop(), stack.pop()
                stack.append(n2 + n1)
            elif token == "-":
                n1, n2 = stack.pop(), stack.pop()
                stack.append(n2 - n1)
            elif token == "*":
                n1, n2 = stack.pop(), stack.pop()
                stack.append(n2 * n1)
            elif token == "/":
                n1, n2 = stack.pop(), stack.pop()
                stack.append(int(n2 / n1))
            else:
                stack.append(int(token))
        return stack[0]

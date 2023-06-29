from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []

        for i in range(len(tokens)):
            v = tokens[i]

            if v.lstrip('-').isnumeric():
                st.append(int(v))
            else:
                first, second = st.pop(), st.pop()
                print(str(second) + ' ' + v + ' ' + str(first))
                if v == '+':
                    st.append(second + first)
                elif v == '-':
                    st.append(second - first)
                elif v == '*':
                    st.append(second * first)
                elif v == '/':
                    st.append(int(second / first))

        return st.pop()


sol = Solution()
print(sol.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))

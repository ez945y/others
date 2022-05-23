
def main():
    def generateParenthesis(self, n: int) -> list[str]:
        res = []
        def gen(s, l, r, n):
            if not (l > n or r > n) and r>1: 
                res.append(s)
                return

            gen(s + '(', l+1, r, n)
            gen(s + ')', l, r+1, n)
            return

        gen("", 0, 0, n)

        return res
    gogo=generateParenthesis(self,3)
    print(gogo)


if __name__ == '__main__':
    main()
class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        symbols = list(dominoes)
        n = len(symbols)
        forces = [0] * n

        # Left to right pass for 'R'
        force = 0
        for i in range(n):
            if symbols[i] == 'R':
                force = n
            elif symbols[i] == 'L':
                force = 0
            else:
                force = max(force - 1, 0)
            forces[i] += force

        # Right to left pass for 'L'
        force = 0
        for i in range(n - 1, -1, -1):
            if symbols[i] == 'L':
                force = n
            elif symbols[i] == 'R':
                force = 0
            else:
                force = max(force - 1, 0)
            forces[i] -= force

        # Build the result
        result = []
        for f in forces:
            if f > 0:
                result.append('R')
            elif f < 0:
                result.append('L')
            else:
                result.append('.')

        return ''.join(result)
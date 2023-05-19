def maior_primo(num):

    def eh_primo(n):

        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    for i in range(num, 1, -1):
        if eh_primo(i):
            return i

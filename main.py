import math
from datetime import datetime
import random

def add(u, v, b):
    d1 = len(u)
    d2 = len(v)
    d = "0" * (abs(d2 - d1))
    n = d1
    if d1 < d2:
        u = d + u
        n = d2
    else:
        if d1 > d2:
            v = d + v
    k = 0
    w = list("0" * (n + 1))
    for j in range(n, 0, -1):
        w[j] = str((int(u[j - 1]) + int(v[j - 1]) + k) % b)
        k = (int(u[j - 1]) + int(v[j - 1]) + k) // b
    w[0] = str(k)
    w = str(int("".join(w)))
    ans = []
    for i in w:
        ans.append(i)
    return ans


def short(u, v, b):
    r = 0
    w = []
    u = u[::-1]
    for j in range(len(u) - 1, -1, -1):
        w.append(str((r * b + int(u[j])) // v))
        r = (r * b + int(u[j])) % v
    return int("".join(w)), r


def substract(u, v, b):
    d1 = len(u)
    d2 = len(v)
    d = "0" * (abs(d2 - d1))
    n = d1
    if int(u) < int(v):
        return '-1'
    if d1 < d2:
        u = d + u
        n = d2
    else:
        if d1 > d2:
            v = d + v
    k = 0
    j = 0
    w = list("0" * (n + 1))
    for j in range(n, 0, -1):
        w[j] = str((int(u[j - 1]) - int(v[j - 1]) + k) % b)
        k = (int(u[j - 1]) - int(v[j - 1]) + k) // b
    w = str(int("".join(w)))
    ans = []
    for i in w:
        ans.append(i)
    return ans


def multiply(u, v, b):
    n = len(u)
    m = len(v)
    ans = list('0' * (m + n))
    u = u[::-1]
    v = v[::-1]
    for j in range(m):
        k = 0
        if v[j] != 0:
            for i in range(n):
                t = int(u[i]) * int(v[j]) + int(ans[i + j]) + k
                ans[i + j] = str(t % b)
                k = t // b
        if k != 0:
            ans[j + n] = str(k)
    ans = ans[::-1]
    return ans


def division(a, c, b):
    a = str(a)
    c = str(c)
    if a == "0":
        return '0', '0'
    if len(a) < len(c):
        return 0, int(a)
    nm = len(a)
    n = len(c)
    m = nm - n
    u = []
    v = []
    for char in a:
        u.append(int(char))
    for char in c:
        v.append(int(char))
    d = b // (v[0] + 1)
    if d == 1:
        u = u[::-1]
        u.append('0')
        u = u[::-1]
    else:
        u = multiply(u, str(d), b)
        v = multiply(v, str(d), b)
    if len(u) != m + n - 1:
        u = u[::-1]
        u.append('0')
        u = u[::-1]
    u = u[::-1]
    v = v[::-1]
    Q = list('0' * (m + 1))
    for j in range(m, -1, -1):
        q_r = short(str((int(u[j + n]) * b + int(u[j + n - 1]))), int(v[n - 1]), b)
        q = q_r[0]
        r = q_r[1]
        while True:
            flag = True
            if n >= 2:
                if q * int(v[n - 2]) > b * r + int(u[j + n - 2]):
                    q -= 1
                    r += int(v[n - 1])
                    flag = False
                else:
                    if q == b:
                        q -= 1
                        r += int(v[n - 1])
                        flag = False
            else:
                if q == b:
                    q -= 1
                    r += int(v[n - 1])
                    flag = False
            if r >= b or flag:
                break
        tmp_u = u[j: j + n + 1]
        tmp_u = tmp_u[::-1]
        v = v[::-1]
        for i in range(len(v)):
            v[i] = str(v[i])
        tmp_v = multiply(str("".join(v)), str(q), b)
        for i in range(len(tmp_u)):
            tmp_u[i] = str(tmp_u[i])
        if str(substract("".join(tmp_u), "".join(tmp_v), b)) != '-1':
            sub_res = substract("".join(tmp_u), "".join(tmp_v), b)
            sub_res = sub_res[::-1]
            while len(sub_res) < n + 1:
                sub_res.append('0')
            it = 0
            for i in range(j, j + n + 1):
                u[i] = sub_res[it]
                it += 1
        else:
            tmp_u = substract("".join(tmp_v), "".join(tmp_u), b)
            newb = pow(b, n + 1)
            tmp_u = substract(str(newb), "".join(tmp_u), b)
            tmp_v = v
            q -= 1
            sum_res = add("".join(tmp_v), "".join(tmp_u), b)
            sum_res = sum_res[::-1]
            it = 0
            for i in range(j, j + n):
                u[i] = sum_res[it]
                it += 1
        v = v[::-1]
        tmp = str(q)
        Q.append(tmp[0])
    Q = int("".join(Q))
    tmp_u = u[:n]
    tmp_u = tmp_u[::-1]
    rem = short(tmp_u, d, b)[0]
    return Q, rem


def power(x, n, b, mod):
    if int(n) == 0:
        return division(1, mod, b)[1]
    N = n
    Y = 1
    Z = x
    Z = division(str(Z), mod, b)[1]
    while True:
        tmp = N
        N = short(str(N), 2, b)[0]
        if short(str(tmp), 2, b)[1] != 0:
            Y = multiply(str(Y), str(Z), b)
            Y = "".join(Y)
            Y = division(str(Y), mod, b)[1]
            if N == 0:
                break
        Z = multiply(str(Z), str(Z), b)
        Z = "".join(Z)
        Z = division(str(Z), mod, b)[1]
    return Y


def Power(x, n, b):
    if int(n) == 0:
        return 1
    N = n
    Y = 1
    Z = x
    while True:
        tmp = N
        N = short(str(N), 2, b)[0]
        if short(str(tmp), 2, b)[1] != 0:
            Y = multiply(str(Y), str(Z), b)
            Y = "".join(Y)
            if N == 0:
                break
        Z = multiply(str(Z), str(Z), b)
        Z = "".join(Z)
    return int(Y)


def is_prime(n, k):
    if n == 2:
        return True
    if n == 3:
        return True
    if (n < 2) | (division(str(n), 2, 10)[1] == 0):
        return False
    t = int("".join(substract(str(n), '1', 10)))
    s = 0
    while division(t, 2, 10)[1] == 0:
        t = division(t, 2, 10)[0]
        s += 1
    for i in range(k):
        a = random.randint(2, n - 2)
        x = power(a, t, 10, n)
        if (x == 1) | (x == int("".join(substract(str(n), '1', 10)))):
            continue
        for j in range(s - 1):
            x = power(x, 2, 10, n)
            if x == 1:
                return False
            if x == int("".join(substract(str(n), '1', 10))):
                break
        if x != int("".join(substract(str(n), '1', 10))):
            return False
    return True


def generate(k):
    mod = 16
    xo = random.randint(1, int("".join(substract(str(Power(2, 16, 10)), '1', 10))))
    c = random.randint(1, int("".join(substract(str(Power(2, 16, 10)), '1', 10))))
    while division(c, 2, 10)[1] == 1:
        c = random.randint(1, int("".join(substract(str(Power(2, 16, 10)), '1', 10))))
    const = 19381
    const_power = 16
    yo = xo
    K = [k]
    tmpk = k
    while tmpk >= (mod + 1):
        tmpk = division(tmpk, 2, 10)[0]
        K.append(tmpk)
    s = len(K) - 1
    P = [0 for _ in range(0, s + 1)]
    tmo_ps = Power(2, int(K[s]) - 1, 10)
    while True:
        tmo_ps = int("".join(add(str(tmo_ps), '1', 10)))
        if is_prime(tmo_ps, math.floor(math.log2(tmo_ps))):
            break
    P[s] = tmo_ps
    m = s - 1
    while m >= 0:
        rm = int(division(K[m], mod, 10)[0]) + 1
        escape = False
        while not escape:
            Y = [yo]
            for i in range(0, int(rm)):
                tmp_mult = multiply(str(Y[i]), str(const), 10)
                tmp_add = add(tmp_mult, str(c), 10)
                tmp_add = int("".join(tmp_add))
                tmp_mod = division(tmp_add, str(Power(2, mod, 10)), 10)[1]
                Y.append(tmp_mod)
            Ym = 0
            for i in range(0, int(rm)):
                tmp_power = Power(2, const_power * i, 10)
                tmp_mult = multiply(str(Y[i]), str(tmp_power), 10)
                Ym += int("".join(tmp_mult))
            #Ym = division(str(Ym), str(Power(2, mod, 10)), 10)[1]
            Y[0] = Ym
            tmp_first = division(str(Power(2, int(K[m]) - 1, 10)), str(P[m + 1]), 10)[0] + 1
            tmp_second = multiply(str(Power(2, int(K[m]) - 1, 10)), str(Ym), 10)
            tmp_third = multiply(str(mod), str(rm), 10)
            tmp_third = int("".join(tmp_third))
            tmp_fourth = multiply(str(Power(2, tmp_third, 10)), str(P[m + 1]), 10)
            tmp_second = int("".join(tmp_second))
            tmp_fourth = int("".join(tmp_fourth))
            tmp_fifth = division(str(tmp_second), str(tmp_fourth), 10)[0]
            #tmp_fifth = int(''.join(tmp_fifth))
            N = add(str(tmp_first), str(tmp_fifth), 10)
            if short(N, 2, 10)[1] != 0:
                N = add(N, '1', 10)
            kk = 0
            while True:
                tmp_first = add(N, str(kk), 10)
                tmp_first = int("".join(tmp_first))
                tmp_second = multiply(str(P[m + 1]), str(tmp_first), 10)
                tmp_second = int("".join(tmp_second))
                P[m] = int("".join(add(str(tmp_second), '1', 10)))
                if int(P[m]) <= Power(2, K[m], 10):
                    escape = True
                    tmp_first = add(N, str(kk), 10)
                    tmp_second = multiply(str(P[m + 1]), tmp_first, 10)
                    tmp_second = int("".join(tmp_second))
                    tmp_third = power('2', tmp_second, 10, str(P[m]))
                    tmp_first = int(''.join(tmp_first))
                    tmp_fourth = power('2', tmp_first, 10, str(P[m]))
                    k_add = False
                    if tmp_third == 1:
                        if tmp_fourth != 1:
                            escape = True
                            k_add = True
                            m -= 1
                            break
                    if not k_add:
                        kk += 2
                else:
                    escape = False
                    break
    if k < 17:
        p = Power(2, k - 1, 10) + 1
        q = Power(2, division(str(k), '2', 10)[0] - 1, 10) + 1
        s = 0
        while True:
            if p == q * s + 1:
                if is_prime(q, math.floor(math.log2(q))):
                    if p < Power(int("".join(multiply(str(q), '2', 10))) + 1, 2, 10):
                            if power('2', str(s), 10, p) != power('1', '0', 10, p):
                                return p, q, s
            if p < q * s + 1:
                q += 2
                s = 0
            else:
                s += 2
            if q > Power(2, division(str(k), '2', 10)[0], 10):
                p = int("".join(add(str(p), '1', 10)))
                q = Power(2, division(str(k), '2', 10)[0] - 1, 10) + 1
    s = division(int("".join(substract(str(P[0]), '1', 10))), str(P[1]), 10)[0]
    return P[0], P[1], xo, c, s


def gcd(a, b):
    while b:
        a = division(str(a), str(b), 10)[1]
        tmp = a
        a = b
        b = tmp
    return a


def eiler(p):
    ans = p
    i = 2
    while Power(i, 2, 10) <= p:
        mod = division(str(p), str(i), 10)[1]
        if mod == 0:
            while division(str(p), str(i), 10)[1] == 0:
                p = division(str(p), str(i), 10)[0]
            ans = int("".join(substract(str(ans), str(division(str(ans), str(i), 10)[0]), 10)))
        i += 1
    if p > 1:
        ans = int("".join(substract(str(ans), str(division(str(ans), str(p), 10)[0]), 10)))
    return ans


def generate_g(p):
    phi = p - 1
    n = phi
    i = 2
    fact = []
    while Power(i, 2, 10) <= n:
        mod = division(str(n), str(i), 10)[1]
        if mod == 0:
            fact.append(i)
            while division(str(n), str(i), 10)[1] == 0:
                n = division(str(n), str(i), 10)[0]
        i += 1
    if n > 1:
        fact.append(n)
    while True:
        while True:
            g = random.randint(2, p - 1)
            if gcd(g, p) == 1:
                break
        for j in range(len(fact)):
            if power(g, division(str(phi), str(fact[j]), 10)[0], 10, p) == 1:
                break
            if j == len(fact) - 1:
                return g


def test_g(g, p):
    ls = []
    for i in range(1, p):
        ls.append(power(g, i, 10, p))
    ls.sort()
    if len(ls) != p - 1:
        return False
    ring = []
    for i in range(1, p):
        ring.append(i)
    if ls == ring:
        return True
    else:
        return False


def closed_key(p):
    while True:
        x = random.randint(1, p - 1)
        if gcd(x, p - 1) == 1:
            break
    return x


def generate_y(g, x, p):
    return power(g, x, 10, p)


def block(message, p):
    alpha = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя0123456789.,/?';:<>[]{} -!()\n"
    alpha = alphabet(alpha)
    coded_text = ""
    for i in message:
        for j in alpha:
            if j[0] == i:
                coded_text += str(j[1])
                print(str(j[0]) + " " + str(j[1]) + '\n')
                break
    current = ""
    tmp = ""
    blocks = []
    i = 0
    while i < len(coded_text):
        tmp += coded_text[i]
        while True:
            i += 1
            if i == len(coded_text):
                current = tmp
                break
            current = tmp
            tmp += coded_text[i]
            if int(tmp) >= p:
                i -= 1
                break
        blocks.append(current)
        tmp = ""
        i += 1
    print("Подряд идущие блоки " + coded_text + '\n')
    print("Блоки, уже разбитые: \n" )
    print(blocks)
    print('\n')
    return blocks


def open_keys(p):
    g = generate_g(p)
    #if test_g(g, p):
        #print("g явлется образующим группы")
    #else:
        #print("g не является образующим группы")
    x = closed_key(p)
    y = generate_y(g, x, p)
    file = open("Открытый ключ.txt", 'w')
    file.writelines(str(p) + '\n')
    file.writelines(str(g) + '\n')
    file.close()


def closed_keys(p):
    x = closed_key(p)
    keys = open("Открытый ключ.txt", 'r').readlines()
    y = generate_y(int(keys[1]), x, int(keys[0]))
    file = open("Ключи Боба.txt", 'w')
    file.writelines(str(y) + "\n")
    file.writelines(str(x))
    file.close()


def alphabet(alpha):
    answer = []
    counter = 111
    for i in alpha:
        if counter % 10 == 0:
            counter += 1
        answer.append([i, counter])
        counter += 1
    print(answer)
    return answer


def encrypt(message, keys):
    print("Сообщение: \n")
    print(message)
    print('\n')
    p = int(keys[0])
    g = int(keys[1])
    print("p = " + str(p) + '\n')
    print("g = " + str(g) + '\n')
    blocks = block(message, p)
    file = open("Криптограмма.txt", 'w')
    closed = open("Ключи Боба.txt", 'r').readlines()
    y = int(closed[0])
    print('y = ' + str(y) + '\n')
    print('a b:\n')
    for blk in blocks:
        k = random.randint(2, p - 3)
        print("k = " + str(k) + '\n')
        a = power(g, k, 10, p)
        tmp1 = power(y, k, 10, p)
        tmp2 = power(int(blk), 1, 10, p)
        b = power(int("".join(multiply(str(tmp1), str(tmp2), 10))), 1, 10, p)
        file.write(str(a) + " ")
        file.write(str(b) + " ")
        print(a, b)
    file.close()


def decrypt(crypt, keys):
    alpha = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя0123456789.,/?';:<>[]{} -!()\n"
    alpha = alphabet(alpha)
    closed = open("Ключи Боба.txt", 'r').readlines()
    x = int(closed[1])
    encrypted_blocks = crypt.split(" ")
    blocks = ""
    file = open("Расшифрованное сообщение.txt", 'w')
    i = 0
    while i < len(encrypted_blocks) - 2:
        a = encrypted_blocks[i]
        b = encrypted_blocks[i + 1]
        i += 2
        p = int(keys[0]) - 1
        tmp1 = int("".join(substract(str(p), str(x), 10)))
        tmp2 = power(str(a), str(tmp1), 10, str(p + 1))
        tmp3 = power(str(b), 1, 10, str(p + 1))
        M = power(int("".join(multiply(str(tmp2), str(tmp3), 10))), 1, 10, str(p + 1))
        blocks += str(M)
    i = 0
    while i < len(blocks) - 2:
        tmp = blocks[i] + blocks[i + 1] + blocks[i + 2]
        for j in alpha:
            if j[1] == int(tmp):
                file.write(j[0])
                break
        i += 3


def main():
    #print(power('2', '712', 10, 713))
    #print(is_prime(1301, math.floor(math.log2(1301))))
    #print(is_prime(74873, math.floor(math.log2(74873))))
    not_error = True
    while not_error:
        print("Введите операцию: 0 для генерации ключей и 1 для шифрования, 2 для расшифрования.")
        mode = input()
        try:
            if (int(mode) != 0) & (int(mode) != 1) & (int(mode) != 2):
                print("Введен символ отличный от 0 или 1")
                not_error = True
            else:
                not_error = False
        except ValueError:
            print("Введен символ отличный от 0 или 1")
            not_error = True
    b = 10
    if mode == '0':
        not_error = True
        print("Программа работает только со степенью счисления 10")
        while not_error:
            print("Введите неотрицательное простое число p:")
            p = input()
            try:
                if int(p) < 0:
                    not_error = True
                    print("Ошибка: Введено отрицательное число")
                else:
                    if not is_prime(int(p), math.floor(math.log2(int(p)))):
                        not_error = True
                        print("Ошибка: Введите простое число")
                    else:
                        not_error = False
            except ValueError:
                print('Ошибка: Введено не число')
                not_error = True
        not_error = True
        open_keys(int(p))
        keys = open("Открытый ключ.txt", 'r').readlines()
        closed_keys(int(keys[0]))
    else:
        if mode == '2':
            keys = open("Открытый ключ.txt", 'r').readlines()
            crypt = open("Криптограмма.txt", 'r').read()
            decrypt(crypt, keys)
            print("Криптограмма успешно расшифрована в файл 'Расшифрованное сообщение.txt'")
        else:
            if mode == '1':
                text = open("Открытый текст.txt", mode='r').read()
                message = ""
                for i in text:
                    message += i.lower()
                keys = open("Открытый ключ.txt", 'r').readlines()
                closed_keys(int(keys[0]))
                encrypt(message, keys)
                print("Текст успешно зашифрован в файл 'Криптограмма.txt'.")


if __name__ == "__main__":
    main()
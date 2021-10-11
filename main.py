def read_list():
    lista = []
    lista_str = input("Citeste numere separate de spatiu ")
    lista_str_split = lista_str.split(' ')
    for num_str in lista_str_split:
        lista.append(int(num_str))
    return lista


def print_menu():
    print(' ')
    print("1. Citire date: ")
    print("2. Determinare cea mai lungă subsecvență cu proprietatea ca toate numerele sunt divizibile cu k: ")
    print("3. Determinare cea mai lungă subsecvență cu proprietatea ca Toate numerele sunt în progresie aritmetică: ")
    print("4. Iesire")


def elemente_diviz_k(lst: list[int], k: int):
    '''
    Determina daca o lista are toate numerele divizibile cu k
    :param lst: Lista de numere intregi
    :param k: Numarul cu care sunt divizibile
    :return: True daca lista e formata doar din numere divizibile cu k si False in caz contrar
    '''
    for x in lst:
        if x % k != 0:
            return False
    return True


def test_elemente_diviz_k():
    assert elemente_diviz_k([2, 4, 6], 2) is True
    assert elemente_diviz_k([5, 10, 15], 2) is False
    assert elemente_diviz_k([5, 10, 15], 5) is True


def get_longest_div_k(lst: list[int], k: int) -> list[int]:
    '''
    Determinare cea mai lungă subsecvență cu proprietatea ca toate numerele sunt divizibile cu k:
    :param lst: Lista de numere naturale
    :param k: Numarul cu care sunt divizibile
    :return: Cea mai lungă subsecvență cu toate numerele divizibile cu k
    '''
    sub_max = []
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            if elemente_diviz_k(lst[i:j+1], k) and len(sub_max) < len(lst[i:j+1]):
                sub_max = lst[i:j+1]
    return sub_max


def test_get_longest_div_k():
    assert get_longest_div_k([1, 2, 4, 6, 1, 2, 3, 5], 2) == [2, 4, 6]
    assert get_longest_div_k([1, 2, 4, 6, 1, 2, 3, 5, 10, 15, 20], 5) == [5, 10, 15, 20]
    assert get_longest_div_k([1, 2, 4, 6, 1, 2, 3, 5, 10, 15, 20], 7) == []


def elemente_progresie_aritmetica(lst: list[int]):
    '''
    Determina daca toate numerele sunt in progresie aritemtica
    :param lst: Lista de numere naturale
    :return: True daca numerele din lista sun in progresie aritmetica, altfel returneaza False
    '''
    if len(lst) < 2:
        return True
    elif len(lst) >= 2:
        dif = lst[1] - lst[0]
        for i in range(0,len(lst)-1):
            if lst[i+1] - lst[i] != dif:
                return False
    return True


def get_longest_arithmetic_progression(lst: list[int]) -> list[int]:
    '''
    Determina cea mai lunga subsecventa cu proprietatea ca toate numerele se afla in progresie aritmetica
    :param lst: Lista de numere naturale
    :return: Cea mai lunga subsecventa cu toate numerele in progresie aritmetica
    '''
    sub_max = []
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            if elemente_progresie_aritmetica(lst[i:j+1]) and len(sub_max) < len(lst[i:j+1]):
                sub_max = lst[i:j+1]
    return sub_max


def test_get_longest_arithmetic_progression():
    assert get_longest_arithmetic_progression([1, 2, 3, 4]) == [1, 2, 3, 4]
    assert get_longest_arithmetic_progression([1, 5, 3, 4]) == [1, 5]
    assert get_longest_arithmetic_progression([1]) == [1]

def main():
    lista = []
    while True:
        print_menu()
        Optiune = int(input("Alege o optiune: "))
        if Optiune == 1:
            lista = read_list()
        elif Optiune == 2:
            k = int(input("K cu care sa fie divizibile numerele: "))
            print('Cea mai lunga subsecventa cu toate numerele divizibile cu ', k, 'este: ', get_longest_div_k(lista, k))
        elif Optiune == 3:
            print('Cea mai lunga subsecventa cu numerele aflate in progresie aritmetica este' , get_longest_arithmetic_progression(lista))
        elif Optiune == 4:
            break

if __name__ == '__main__':
    test_elemente_diviz_k()
    test_get_longest_div_k()
    test_get_longest_arithmetic_progression()
    main()
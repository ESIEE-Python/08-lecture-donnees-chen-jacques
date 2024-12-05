"""lecture de fichier"""
#import random

FILENAME = "listes.csv"

#### Fonctions secondaires

def read_data(filename):
    """retourne le contenu du fichier <filename>

    Args:
        filename (str): nom du fichier à lire

    Returns:
        list: le contenu du fichier (1 list par ligne)
    """
    with open(filename, 'r', encoding='UTF-8') as f:
        l = [list(map(int, i.strip().split(";"))) for i in f.readlines()]
    return l

def get_list_k(data, k):
    """k-ieme liste"""
    return data[k]

def get_first(l):
    """premier élément"""
    return l[0]

def get_last(l):
    """dernier élément"""
    return l[-1]

def get_max(l):
    """élément le plus grand"""
    return max(l)

def get_min(l):
    """élément le plus petit"""
    return min(l)

def get_sum(l):
    """somme des éléments"""
    return sum(l)


#### Fonction principale


def main():
    """main"""

    data = read_data(FILENAME)
    for i, l in enumerate(data):
        print(i, l)
    k = 37
    print(k, get_list_k(data, 37))


if __name__ == "__main__":
    main()

import math

from matplotlib import pyplot as plt

alphabet = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11,
            'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22,
            'x': 23, 'y': 24, 'z': 25}

def encode_vigenere(message, mot_code):
    """
    Cette fonction réalise le chiffrement de vigenere du message
    param message: message en chiffrer
    param mot_code: clé de chiffrement
    return: cryptogramme
    """
    message_encrypted = ''
    values_list = []
    split_message = []
    for i in range(0, len(message), len(mot_code)):
        split_message.append(message[i: i + len(mot_code)])
    split_message = [message[i: i + len(mot_code)] for i in range(0, len(message), len(mot_code))]
    for each_split in split_message:
        i = 0
        for letter in each_split:
            values_list.append((alphabet[letter] + alphabet[mot_code[i]]) % 26)
            i += 1
    for x in values_list:
        for k, v in alphabet.items():
            if x == v:
                message_encrypted += ''.join(k)
    return message_encrypted


def decode_vigenere(message, mot_code):
    """
     Cette fonction réalise le déchiffrement de vigenere du cryptogramme
    param cryptogramme: cryptogramme à déchiffrer
    param mot_code: clé de chiffrement
    return: message en clair
    """
    message_decrypted = ""
    values_list = []
    split_encrypted = []
    for i in range(0, len(message), len(mot_code)):
        split_encrypted.append(message[i: i + len(mot_code)])
    for each_split in split_encrypted:
        i = 0
        for letter in each_split:
            values_list.append((alphabet[letter] - alphabet[mot_code[i]]) % 26)
            i += 1
    for x in values_list:
        for k, v in alphabet.items():
            if x == v:
                message_decrypted += ''.join(k)
    return message_decrypted


def guess_password(cryptogramme, len_password):
    """
    Cette fonction détermine le mot de passe surt base du cryptogramme et de la longueur du mot de passe.
    Elle utilise la cryptanalyse du chiffre de césar pour déterminer chaque lettre du mot de passe.
    param cryptogramme: cryptogramme à cryptanalyser
    param len_password: longueur du mot de passe
    return: le mot de passe deviné
    """
    cryptogramme_split = []
    key = []
    prob_pass = ''
    frequencies = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0,
                   'm': 0,
                   'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0,
                   'z': 0}
    alphabet_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                     'u',
                     'v', 'w', 'x', 'y', 'z']

    for shift in range(len_password):
        cryptogramme_split.append(cryptogramme[shift::len_password])

    for split in cryptogramme_split:
        for letter in split:
            if letter in frequencies:
                frequencies[letter] = split.count(letter)
            else:
                pass
        most_frequent = max(frequencies, key=frequencies.get)
        key.append(alphabet_list.index(most_frequent) - alphabet_list.index('e'))
    for i in key:
        for k, v in alphabet.items():
            if i == v:
                prob_pass += k

    return prob_pass


def guess_key_lenght(histo):
    """
    Cette fonction détermine la longueur du mot de passe.
    La valeur correspond au mode de l'histogramme des pgcd des distances des répétitions.
    param histo: histogramme des pgcd
    return: la longueur du mot de passe (le mode)
    """
    frq_dict = {}
    for i in histo:
        frq_dict[i] = histo.count(i)
    max_value = max(frq_dict.values())
    for k, v in frq_dict.items():
        if v == max_value:
            return k
        else:
            continue


def build_histogram(pgcd):
    """
    Cette méthode construit l'histogramme des pgcd.
    param: les pgcd
    return: histogramme des pgcd
    """
    plt.hist(pgcd, bins=5, range=(min(pgcd), max(pgcd)), align='mid')
    return plt.show()


def get_pgcd(distances):
    """
    Cette fonction calcul le pgcd entre toutes les distances de répétitions
    param distances: distances de répétition
    return: les pgcd des distances 2 à 2
    """
    split_distances = []
    pgcd_list = []
    for i in range(0, len(distances), 2):
        split_distances.append(distances[i:i + 2])
    for a in split_distances:
        if len(a) == 2:
            pgcd_list.append(math.gcd(a[0], a[1]))
        else:
            pgcd_list.append(math.gcd(a[0]))
    return pgcd_list


def get_sequence_positions(cryptogramme):
    """
    Cette fonction identifie les séquences de 3 lettres qui se répetent et leur position.
    param cryptogramme: cryptogramme à cryptanalyser
    return: dictionnaire des séquences (clé=séquence de 3 lettres) et leurs positions (valeur=tableau de position)
    """
    seq_dict = {}
    split_crypto = []
    for i in range(0, len(cryptogramme), 3):
        split_crypto.append(cryptogramme[i:i + 3])
    ct = 3
    for x in split_crypto:
        try:
            seq_dict[x] = [cryptogramme.index(x), cryptogramme.index(x, ct)]
            ct += 3
        except ValueError:
            ct += 3

    return seq_dict


def get_distances(dictionary_len_3):
    """
    Cette fonction calcul les distances des réptitions sur base de la position des occurences.
    param dictonary_len_3: les répititions et leur position
    return: les distances
    """
    distances = []
    for v in dictionary_len_3.values():
        distances.append(v[1] - v[0])
    return distances


def cryptanalyse_vigenere(cryptogramme):
    """
    Cette fonction réalise une cryptanalyse d'un cryptogramme de vigenère.
    Elle détermine les séquences de répétition via get_sequence_positions
    Calcul les distances via get_distances
    Détermine les pgcd via get_pgcd et leur histogramme via build_histogram
    Devine la longueur du mot de passe via guess_key_lenght et le mot de passe lui-même via guess_password
    Le mot de passe est alors afficher et sa valeur finale demandée à l'utilisateur,
     afin de corriger les éventuelles erreurs de cryptanalyse.

    param cryptogramme: cryptogramme à cryptanalyser
    return: message en clair
    """
    ditionnaire = get_sequence_positions(cryptogramme)
    distance = get_distances(ditionnaire)
    gcds = get_pgcd(distance)
    pass_lenght = guess_key_lenght(gcds)
    prob_pass = guess_password(cryptogramme, pass_lenght)
    return decode_vigenere(cryptogramme, prob_pass)

"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""


def value_of_card(card):
    """Determine the scoring value of a card.

    :param card: str - given card.
    :return: int - value of a given card.  See below for values.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """
    # verificamos se a entrada não é uma string
    if not isinstance(card, str):
        # caso não seja, retornaremos um erro de tipo
        raise TypeError("A função só aceita strings")
    # tentamos
    try:
        # fazer a entrada virar diretamente o valor dela no jogo
        # caso ela seja a carta de um número
        CardValue = int(card)
    # E então, se falharmos, tentamos ver se é um rei, uma rainha,
    # um ace ou um valete  
    except:
        # Fazemos a entrada ficar em maiuscula para não ser case sensitive
        card = card.upper()
        # verificamos se é um ace separadamente, visto que ele tem um valor diferente
        if card == "A":
            # e, se sim, daclaramos que ele vale um retornando a função
            return 1
        # verificamos, também, se é um rei, uma rainha ou um valete
        elif card == "J" or card == "Q" or card == "K":
            # e, se assim for, retornamos a função dizando que a carta vale 10
            return 10
        # e caso não seja nenhuma dessas outras declaramos que ou um erro na entrada
        else:
            raise ValueError("A função aceita apenas numeros, em formato" +
                             "de stirng, ou as letras: A, J, Q ou K")
    # caso a entrada for um número no formato de uma string
    else:
        # verificamos se é um valor válido
        if 2 <= CardValue <= 10:
            # caso seja o retornamos
            return CardValue
        else:
            # e, se não, devolvemos o erro correspondente
            raise ValueError("Os valores númericos das cartas só estão entre" +
                             " 2 e 10")


def higher_card(card_one, card_two):
    """Determine which card has a higher value in the hand.

    :param card_one, card_two: str - cards dealt in hand.  See below for values.
    :return: str or tuple - resulting Tuple contains both cards if they are of equal value.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """
    # Calculando o valor da carta 1
    ValueCardOne = value_of_card(card_one)
    # Calculando o valor da carta 2
    ValueCardTwo = value_of_card(card_two)
    # verificando se a carta 1 é maior do que a segunda
    if ValueCardOne > ValueCardTwo:
        # retornando o valor da carta 1, se esse for o caso
        return card_one
    # caso não seja, verificando se a carta doi é maior do que a primeira com
    # um if em vez de elif. Já que, se a comparação a cima for verdadeira o
    # programa não vai executar essa função de qualquer forma
    if ValueCardOne < ValueCardTwo:
        # caso a segunda carta seja maior retornamos ela
        return card_two
    # e caso as duas comparações anteriores sejam falsas, sabemos que elas tem
    # o mesmo valor e basta retornar os dois
    return  card_one, card_two


def value_of_ace(card_one, card_two):
    """Calculate the most advantageous value for the ace card.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: int - either 1 or 11 value of the upcoming ace card.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """

    pass


def is_blackjack(card_one, card_two):
    """Determine if the hand is a 'natural' or 'blackjack'.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: bool - is the hand is a blackjack (two cards worth 21).

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """

    pass


def can_split_pairs(card_one, card_two):
    """Determine if a player can split their hand into two hands.

    :param card_one, card_two: str - cards dealt.
    :return: bool - can the hand be split into two pairs? (i.e. cards are of the same value).
    """

    pass


def can_double_down(card_one, card_two):
    """Determine if a blackjack player can place a double down bet.

    :param card_one, card_two: str - first and second cards in hand.
    :return: bool - can the hand can be doubled down? (i.e. totals 9, 10 or 11 points).
    """

    pass

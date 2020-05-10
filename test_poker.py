import pytest
import random
from poker import Ranking, Hands, PKCard

non_flush_suit = 'CHSDS'
flush_suit = 'SSSSS'
test_cases = {
    Ranking.STRAIGHT_FLUSH:(
        tuple(zip('45678', flush_suit)),
        tuple(zip('65432', flush_suit)),
        ),
    Ranking.FOUR_OF_A_KIND: (
        tuple(zip('TTTTQ', non_flush_suit)),
        tuple(zip('22229', non_flush_suit)),
        ),
    Ranking.FULL_HOUSE: (
        tuple(zip('88877', non_flush_suit)),
        tuple(zip('22299', non_flush_suit)),
        ),
    Ranking.FLUSH: (
        tuple(zip('AJT98', flush_suit)),
        tuple(zip('AJ987', flush_suit)),
        ),
    Ranking.STRAIGHT: (
        tuple(zip('23456', non_flush_suit)),
        tuple(zip('45678', non_flush_suit)),
        tuple(zip('56789', non_flush_suit)),
        ),
    Ranking.THREE_OF_A_KIND: (
        tuple(zip('888A9', non_flush_suit)),
        tuple(zip('88847', non_flush_suit)),
        ),
    Ranking.TWO_PAIRS: (
        tuple(zip('AA998', non_flush_suit)),
        tuple(zip('AA778', non_flush_suit)),
        tuple(zip('JJTTK', non_flush_suit)),
       ),
    Ranking.ONE_PAIR: (
        tuple(zip('88AT9', non_flush_suit)),
        tuple(zip('88AT7', non_flush_suit)),
        tuple(zip('77AKQ', non_flush_suit)),
      ),
    Ranking.HIGH_CARD: (
        tuple(zip('AJT98', non_flush_suit)),
        tuple(zip('AJT97', non_flush_suit)),
        tuple(zip('QJT97', non_flush_suit)),  
      ),
}
def cases(*rankings):
    """get the test cases for ranking. all rankings if empty rankings
    """
    if not rankings:
        rankings = test_cases.keys()
    
    return \
        [ ([r+s for r, s in case], ranking)
                    for ranking in rankings
                        for case in test_cases[ranking]
        ]


@pytest.mark.parametrize("faces, expected", cases(Ranking.STRAIGHT))
def test_is_straight(faces, expected):
    origin_hand = [PKCard(c) for c in faces]
    random.shuffle(faces)
    origin_hand.sort()
    hand = Hands([PKCard(c) for c in faces])
    result = hand.is_straight()
    assert result == True
    assert hand.cards == origin_hand

@pytest.mark.parametrize("faces, expected", cases(Ranking.FLUSH))
def test_is_flush(faces, expected):
    origin_hand = [PKCard(c) for c in faces]
    random.shuffle(faces)
    origin_hand.sort()
    hand = Hands([PKCard(c) for c in faces])
    result = hand.is_flush()
    assert result == True
    assert hand.cards == origin_hand
    print(origin_hand)

@pytest.mark.parametrize("faces, expected", cases(Ranking.STRAIGHT_FLUSH))
def test_straight_flush(faces, expected):
    origin_hand = [PKCard(c) for c in faces]
    random.shuffle(faces)
    origin_hand.sort()
    hand = Hands([PKCard(c) for c in faces])
    result = hand.straightflush()
    assert result == True
    assert hand.cards == origin_hand

@pytest.mark.parametrize("faces, expected", cases(Ranking.FOUR_OF_A_KIND, Ranking.FULL_HOUSE, Ranking.THREE_OF_A_KIND, Ranking.TWO_PAIRS, Ranking.ONE_PAIR, Ranking.HIGH_CARD))
def test_find_a_kind(faces, expected):
    origin_hand = [PKCard(c) for c in faces]
    random.shuffle(faces)
    origin_hand.sort()
    hand = Hands([PKCard(c) for c in faces])
    result = hand.find_a_kind()
    assert result == expected
    assert hand.cards == origin_hand

@pytest.mark.parametrize("faces, expected", cases())
def test_tell_hand_ranking(faces, expected):
    origin_hand = [PKCard(c) for c in faces]
    random.shuffle(faces)
    origin_hand.sort()
    hand = Hands([PKCard(c) for c in faces])
    result = hand.tell_hand_ranking()
    assert result == expected
    assert hand.cards == origin_hand


# def test_compare_user():
#     hand_cases = [Hands(faces) for faces, ranking in cases()]
#     for hand in hand_cases:
#         hand.numd()
#     sorted_cases = sorted(hand_cases, reverse=True)
#     assert sorted_cases == hand_cases
    # 이거해보고 저거해보고...test_compare_user에
    # Hands 와 Hands 끼리는 등호가 성립하지 않는다고 하여
    # TypeError발생... tie-break 함수때문인 것 같지만
    # 뜯어보기엔 시간이 촉박...
   
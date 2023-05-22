import pytest

from homeworks_polina.hw15_zinovieva import Material, Spiritual


@pytest.mark.positive
def test_buy_matart():
    matart = Material(
        type="test_type", author="test_author", name="test_name", price=0, year=0
    )
    matart.purchase()
    assert matart.purchase() == "You have bought a painting, now you have 20000 euros"


def test_valuation():
    matart = Material(
        type="test_type", author="test_author", name="test_name", price=0, year=1920
    )
    assert matart.buy(name="qa") == "qa wants to buy a painting"


def test_buy_spiritual():
    spirart = Spiritual(type="test_type", author="test_auth", price=0, name="Test_name")
    assert spirart.purchase() == "You can't buy spiritual art, its priceless"


def test_music_in_museum():
    harry = Spiritual(
        type="test_type", author="Harry Styles", price=0, name="Test_name"
    )
    assert harry.music_in_museum() == "['Harry Styles']-allowed music author"
    mozart = Spiritual(type="test_type", author="Mozart", price=0, name="Test_name")
    assert mozart.music_in_museum() == "['Mozart']-allowed music author"
    melovin = Spiritual(type="test_type", author="Melovin", price=0, name="Test_name")
    assert melovin.music_in_museum() == "['Melovin']-allowed music author"
    diana = Spiritual(type="test_type", author="Diana Ross", price=0, name="Test_name")
    assert diana.music_in_museum() == "['Diana Ross']-allowed music author"
    lynyrd = Spiritual(
        type="test_type", author="Lynyrd Skynyrd", price=0, name="Test_name"
    )
    assert lynyrd.music_in_museum() == "['Lynyrd Skynyrd']-allowed music author"


@pytest.mark.negative
def test_buy_matart_n():
    matart = Material(
        type="test_type", author="test_author", name="test_name", price=30000, year=0
    )
    matart.purchase()
    assert (
        matart.purchase()
        == "Your account balance will be -10000. It is < 0. Sorry,next time."
    )


def test_music_in_museum_n():
    outer = Spiritual(type="test_type", author="Polina", price=0, name="Test_name")
    assert outer.music_in_museum() == "Don't listen to it"

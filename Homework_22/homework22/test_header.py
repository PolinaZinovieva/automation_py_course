import time


def test01_check_store_open(header_block):
    header_block.open_store()


def test02_check_search_store(header_block):
    header_block.find_game()


def test03_check_distribution(header_block):
    header_block.open_distribution()


def test04_check_support(header_block):
    open_page = header_block.open_support()
    game_click = open_page.click_game()
    game_click.open_game()


def test05_check_unreal_engine(header_block):
    header_block.open_ue()




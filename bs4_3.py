import mechanicalsoup
import time

test_url = 'http://olympus.realpython.org/dice'
browser = mechanicalsoup.Browser()


def dynamic_web_scrap():
    check_page = browser.get(test_url)
    get_tag = check_page.soup.select('#result')[0]
    result = get_tag.text

    print('Dice outcome:\t', result)

def dynamic_web_scrap1():
    for i in range(4):
        check_page1 = browser.get(test_url)
        get_tag1 = check_page1.soup.select('#result')[0]
        result1 = get_tag1.text
        print('Dice outcome1:\t', result1)
        time.sleep(3)


def dynamic_web_scrap2():
    while True:
        check_page2 = browser.get(test_url)
        get_tag2 = check_page2.soup.select('#result')[0]
        result2 = get_tag2.text
        print('\n\tDice outcome2:\t', result2)
        time.sleep(3)


if __name__ == '__main__':
    #dynamic_web_scrap()
    #dynamic_web_scrap1()
    dynamic_web_scrap2()
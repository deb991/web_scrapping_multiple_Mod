import mechanicalsoup

test_url = 'http://olympus.realpython.org/login'

def test_html_form():
    '''Now we are trying to operate html form using mechanicalsoup'''

    base_url = 'http://olympus.realpython.org'
    browser = mechanicalsoup.Browser()

    print('Test URL:\t', test_url)
    login_page = browser.get(test_url)
    login_page_html = login_page.soup

    form = login_page_html.select("form")[0]
    form.select("input")[0]["value"] = "zeus"
    form.select("input")[1]["value"] = "ThunderDude"

    profile_page = browser.submit(form, login_page.url)
    #links = profile_page.soup.select("a")
    #for link in links:
    #    address = base_url +  link['href']
    #    text = link.text
    #    print(f"{text}: {address}")

    print('Title:\t', profile_page.soup.title)

if __name__ == '__main__':
    test_html_form()
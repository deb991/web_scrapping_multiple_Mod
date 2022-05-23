from urllib.request import urlopen
import re

# test_url = "http://olympus.realpython.org/profiles/aphrodite"
# test_url = "http://olympus.realpython.org/profiles/poseidon"
test_url = "http://olympus.realpython.org/profiles/dionysus"


page = urlopen(test_url)
html_bytes = page.read()
'''Extracting HTML from web page'''
html_conv = html_bytes.decode("utf-8")
'''Getting whole HTML code structure in text format'''


# print('HTML COnversion:\t', html_conv)

def text_scrap1():
    '''Use only first url to manage simple operation'''
    '''Extracting text usiung string operation method'''
    title_index = html_conv.find("<title>")

    '''Since .find() returns the index of the first occurrence 
    of a substring, you can get the index of the 
    opening <title> tag by passing the string "<title>" to .find():'''

    # print('Title Index:\t', title_index)

    '''Find keyword basically gives the first charector's index position'''
    '''So into that case if we need to find any specific keyword & its last charector's index  position'''

    start_index = title_index + len("<title>")
    print('Start Index:\t', start_index)

    title_end_index = html_conv.find("</title>")
    print('End Index:\t', title_end_index)

    '''Now extracting specific region & part from the page using tag names
    Hence we are onlt capturing the first keyword of the tag, casue 
    we only need to reach out to the certain keyword & extract the name'''

    get_text1 = html_conv[start_index:title_end_index]
    print('Extract Title:\t', get_text1)

    return get_text1


def scrap_regex(args):
    string = args
    pattern1 = '<title.*?>.*?</title.*?>'  # Define pattern to find among html tags <>
    match_result = re.search(pattern1, string, re.IGNORECASE)  # Check from source string set.
    title = match_result.group()  # whether match or not to check.
    title = re.sub("<.*?>", "", title)  # Remove HTMl tags <>
    print('Extract title from web:\t', title)
    return title

def test_scrap_regex(args):
    string = args
    #print('text:\t', args)
    name_pattrn = '<h2.*?>.*?</h2.*?>'
    name_match = re.search(name_pattrn, string, re.IGNORECASE)
    find_name = name_match.group()
    find_name = re.sub('<.*?>', "", find_name)
    #print('Name Found:\t', find_name)


def test_scrap_regex1(args):
    html_txt = args
    for string in ['Name:', 'Favorite Color:']:
        str_start_idx = html_txt.find(string)
        text_start_idx = str_start_idx + len(string)

        next_html_offset = html_txt[text_start_idx:].find('<')
        text_end_idx = text_start_idx+next_html_offset

        get_text = html_txt[text_start_idx:text_end_idx]
        clean_text = get_text.strip(' \r\n\t')
        print('Scrapped text:\t', clean_text)



if __name__ == '__main__':
    # text_scrap1()
    #scrap_regex(html_conv)
    #test_scrap_regex(html_conv)
    test_scrap_regex1(html_conv)
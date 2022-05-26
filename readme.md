<h1>Scrape and Parse Text From Websites</h1>
<h2>Extract Text From HTML With String Methods</h2>
One way to extract information from a web page’s HTML is to use string methods. For instance, you can use .find() to search through the text of the HTML for the <title> tags and extract the title of the web page.

Let’s extract the title of the web page you requested in the previous example. If you know the index of the first character of the title and the first character of the closing </title> tag, then you can use a string slice to extract the title.

Since .find() returns the index of the first occurrence of a substring, you can get the index of the opening <title> tag by passing the string "<title>" to .find():

You don’t want the index of the <title> tag, though. You want the index of the title itself. To get the index of the first letter in the title, you can add the length of the string "<title>" to title_index:


<h2>A Primer on Regular Expressions</h2>
Regular expressions—or regexes for short—are patterns that can be used to search for text within a string. Python supports regular expressions through the standard library’s re module.

Note: Regular expressions aren’t particular to Python. They’re a general programming concept and can be used with any programming language.

To work with regular expressions, the first thing you need to do is import the re module:

Armed with all this knowledge, let’s now try to parse out the title from a new profile page, which includes this rather carelessly written line of HTML:


The .find() method would have a difficult time dealing with the inconsistencies here, but with the clever use of regular expressions, you can handle this code quickly and efficiently:

Let’s take a closer look at the first regular expression in the pattern string by breaking it down into three parts:

<title.*?> matches the opening <TITLE > tag in html. The <title part of the pattern matches with <TITLE because re.search() is called with re.IGNORECASE, and .*?> matches any text after <TITLE up to the first instance of >.

.*? non-greedily matches all text after the opening <TITLE >, stopping at the first match for </title.*?>.

</title.*?> differs from the first pattern only in its use of the / character, so it matches the closing </title / > tag in html.

The second regular expression, the string "<.*?>", also uses the non-greedy .*? to match all the HTML tags in the title string. By replacing any matches with "", re.sub() removes all the tags and returns only the text.

Note: Web scraping in Python or any other language can be tedious. No two websites are organized the same way, and HTML is often messy. Moreover, websites change over time. Web scrapers that work today are not guaranteed to work next year—or next week, for that matter!

Regular expressions are a powerful tool when used correctly. This introduction barely scratches the surface. For more about regular expressions and how to use them, check out the two-part series


<h3>test_scarp_regex1</h3>
It looks like there’s a lot going on in this forloop, but it’s just a little bit of arithmetic to calculate the right indices for extracting the desired text. Let’s break it down:

1. You use html_text.find() to find the starting index of the string, either "Name:" or "Favorite Color:", and then assign the index to string_start_idx.
2. Since the text to extract starts just after the colon in "Name:" or "Favorite Color:", you get the index of the the character immediately after the colon by adding the length of the string to start_string_idx and assign the result to text_start_idx.
3. You calculate the ending index of the text to extract by determining the index of the first angle bracket (<) relative to text_start_idx and assign this value to next_html_tag_offset. Then you add that value to text_start_idx and assign the result to text_end_idx.
4. You extract the text by slicing html_text from text_start_idx to text_end_idx and assign this string to raw_text.
5. You remove any whitespace from the beginning and end of raw_text using .strip() and assign the result to clean_text.

<h2>Code execution Steps</h2>

``python.exe C:/Users/002CSC744/Documents/web_scrapping_mult/web_scarp.py``

``python.exe C:/Users/002CSC744/Documents/web_scrapping_mult/bs4_1.py``

``python.exe C:/Users/002CSC744/Documents/web_scrapping_mult/bs4_2.py``

``python.exe C:/Users/002CSC744/Documents/web_scrapping_mult/bs4_3.py``


<h3>**Result:**</h3>

<h4>web_scarp.py</h4>

`Dionysus`

`Wine`

<h4>bs4_1.py</h4>

``soup Image Find:	 <img src="/static/dionysus.jpg"/>``

``Link:	 http://olympus.realpython.org//profiles/aphrodite``

``Link:	 http://olympus.realpython.org//profiles/poseidon``

``Link:	 http://olympus.realpython.org//profiles/dionysus``

<h4>bs4_2.py</h4>

``Test URL:	 http://olympus.realpython.org/login``

``Title:	 <title>All Profiles</title>``

<h4>bs4_3.py</h4>
``Dice outcome2:	 2``

``Dice outcome2:	 3``

``Dice outcome2:	 5``

``Dice outcome2:	 3``

``Dice outcome2:	 5``

``Dice outcome2:	 4``

``Dice outcome2:	 6``

``Dice outcome2:	 3``

``Dice outcome2:	 3``


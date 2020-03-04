import validators, requests
from bs4 import BeautifulSoup as soup

VALID_HTML_TAGS = ["a","abbr","acronym","address","area","b","base","bdo","big","blockquote","body","br","button","caption","cite","code","col","colgroup","dd","del","dfn","div","dl","DOCTYPE","dt","em","fieldset","form","h1","h2","h3","h4","h5","h6","head","html","hr","i","img","input","ins","kbd","label","legend","li","link","map","meta","noscript","object","ol","optgroup","option","p","param","pre","q","samp","script","select","small","span","strong","style","sub","sup","table","tbody","td","textarea","tfoot","th","thead","title","tr","tt","ul","var"]

def get_user_url(prompt):
    """Helper function to get a url from user input safely"""
    while True:
        user_input = input(prompt)
        if validators.url(user_input):
            break
        else:
            print ("that does not appear to be valid input")
    return user_input

def get_user_tag(prompt):
    """Helper function to get a html tag from user input safely"""
    while True:
        user_input = input(prompt)
        if user_input in VALID_HTML_TAGS:
            break
        else:
            print ("that does not appear to be a valid html tag")
    return user_input

def get_tag_from_page(tag, url):
    """a function that allows you to pull out a tag (passed as an argument to your function) from any URL (also passed as an argument to your function)"""
    response = requests.get(url)
    content = response.content
    blob = soup(content, 'lxml')
    return blob.find_all(tag)

def make_meaningful(blob):
    """a function to format the output in a meaningful way"""
    # div - Generally used for spacing on the page and don't contain text or useful attributes.  Meaningful for div tags might be counting the number of divs that are on the page.
    # li - Most of these have the `class=gallerybox` that makes them a container for the crater information that we're looking for on the page, but they don't contain text or useful attributes.  Meaningful for li tags might be counting the number of divs that are on the page.
    # a - Have a href attribute.  Some a tags on this page contain img tags and some contain text. Meaningful for a tags might be displaying the href attribute and checking if it has text or title attribute.
    # img - Have a src attribute and a width and height attribute.  Meaningful for img tags might be displaying the src attribute or counting how many images have the same width or height.
    return blob

def write_file(blob, filename):
    """a function to write the formatted results to a txt file"""
    # TBD

if __name__ == "__main__":
    url = get_user_url("Please provide a url, specifying the protocol (i.e. http:// or https://): ")
    tag = get_user_tag("Please provide a html tag: ")
    print (get_tag_from_page(tag,url))

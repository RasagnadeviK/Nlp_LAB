import nltk
import re
paragraph = """Larry Page and Sergey Brin, two students at Stanford University, USA, started
Backrub in early 1996. They made it into a company, Google Inc., on September
7, 1998 at a friend's garage in Menlo Park, California. In February 1999, the
company moved to 165 University Ave., Palo Alto, California, and then moved
to another place called the Googleplex. In September 2001, Google's rating
system (PageRank, for saying which information is more helpful) got a U.S.
Patent. The patent was to Stanford University, with Lawrence (Larry) Page as
the inventor (the person who first had the idea). Google makes a percentage of
its money through America Online and InterActiveCorp. It has a special group
known as the Partner Solutions Organization (PSO) which helps make contracts,
helps making accounts better, and gives engineering help."""
sentences=nltk.sent_tokenize(paragraph)
patterns = {
    'name': r'Larry Page|Sergey Brin|Lawrence \(Larry\) Page',  # Patterns for names
    'location': r'[A-Z][a-zA-Z\s]+,\s[A-Z][a-zA-Z\s]+',  # Patterns for locations
    'time': r'(?:\b(?:\d{1,2}\s)?(?:January|February|March|April|May|June|July|August|September|October|November|December)\s\d{4}\b)',  # Patterns for time
    'organization': r'Google Inc\.|Google|Stanford University|America Online|InterActiveCorp|Partner Solutions Organization \(PSO\)'  # Patterns for organizations
}
def highlight_details(text):
    highlighted_text = text
    for key, pattern in patterns.items():
        matches = re.findall(pattern, highlighted_text)
        for match in matches:
            highlighted_text = re.sub(re.escape(match), f"\033[1;33m{match}\033[m", highlighted_text)
    return highlighted_text
highlighted_sentences=[highlight_details(sentence) for sentence in sentences]
highlighted_paragraph = '. '.join(highlighted_sentences)
print(highlighted_paragraph)

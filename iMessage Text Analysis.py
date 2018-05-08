import re
import string
frequency = {}
document_text = open('your_file_name', 'r')
text_string = document_text.read().lower()
match_pattern = re.findall(r'\b[a-z]{3,15}\b', text_string)
#below list can be edited
excludedwords = ['about', 'actually', 'after', 'again', 'all', 'already', 'also', 'always', 'and',
                 'any', 'anything', 'are', 'around', 'away', 'back', 'bad', 'because', 'been',
                 'before', 'being', 'better', 'bit', 'but', 'can', 'cause', 'check', 'close', 'could',
                 'course', 'day', 'days', 'did', 'didn', 'does', 'doesn', 'doing', 'don', 'dont', 'done', 'down',
                 'enough', 'even', 'ever', 'every', 'everything', 'few', 'find', 'fine', 'first', 'flight'
                ,'for', 'from', 'get', 'getting', 'give', 'going', 'gonna', 'good', 'got', 'great',
                 'guess', 'guy', 'had', 'hahahah', 'has', 'hate', 'have', 'haven', 'having', 'her',
                 'here', 'hey', 'him', 'his', 'how', 'idk', 'ill', 'into', 'its', 'ive', 'just',
                 'keep', 'kinda', 'know', 'last', 'later', 'least', 'leave', 'left', 'let',
                 'liked', 'little', 'lolol', 'long', 'look', 'lot', 'made', 'make', 'makes', 'making',
                 'maybe', 'mean', 'might', 'minutes', 'more', 'much', 'never', 'new', 'next', 'not',
                 'now', 'off', 'one', 'only', 'other', 'out', 'over', 'people', 'phone', 'picture',
                 'place', 'plan', 'probably', 'put', 'ready', 'really', 'right', 'room', 'said',
                 'same', 'saw', 'say', 'second', 'see', 'send', 'sent', 'she', 'should', 'since',
                 'some', 'something', 'soon', 'sorry', 'sounds', 'start', 'still', 'stuff',
                 'such', 'sure', 'take', 'taking', 'text', 'tell', 'than', 'that', 'thats', 'the',
                 'them', 'then', 'there', 'they', 'thing', 'things', 'think', 'thinking', 'this',
                 'tho', 'those', 'though', 'thought', 'time', 'today', 'told', 'too', 'took',
                 'try', 'trying', 'ugh', 'until', 'use', 'very', 'wait', 'wanna', 'wanted', 'was',
                 'wasn', 'watching', 'way', 'week', 'weird', 'well', 'went', 'were', 'what', 'when',
                 'where', 'which', 'while', 'who', 'why', 'will', 'woke', 'work', 'working',
                 'would', 'yea', 'yeah', 'yes', 'yesterday', 'yet','with','need',
                 'like', 'god', 'lol', 'your' ,'you', 'case', 'hear', 'help', 'hour'
                 'myself', 'won', 'hes', 'seriously', 'show', 'cant', 'want', 'come' ]
for word in match_pattern:
    count = frequency.get(word,0)
    frequency[word] = count + 1
     
frequency_list = frequency.keys()
 
for words in sorted(frequency_list):
    if frequency[words] > 3 and words not in excludedwords and words in ClaudiaAdjectives:
        print words, frequency[words]

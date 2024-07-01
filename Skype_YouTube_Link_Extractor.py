from skpy import Skype
from getpass import getpass
import re

sk = Skype("dbadasyan", getpass(), "token.txt")
ch = sk.chats["8:tigranbadasyan"]

def extract_youtube_links(message):
    youtube_regex = r'(?:https:\/\/)?(?:www\.)?(youtube|youtu)\.(com|be)\/(watch\?v=)?([\w-]+)'
    links = re.finditer(youtube_regex, message, re.DOTALL)
    search = []

    for match in links:
        search.append(match.group(0))

    return list(set(search))

youtube_links = []

while True:
    for msg in ch.getMsgs():
        print(msg.content[:50])
        youtube_links = extract_youtube_links(msg.content)
        print(youtube_links)
        with open("youtube_links.txt", "a") as file:
                for link in youtube_links:
                    file.write(link + "\n")
        youtube_links = []


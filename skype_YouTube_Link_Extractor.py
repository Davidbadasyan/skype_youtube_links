from skpy import Skype
from getpass import getpass
import re
import time

def extract_youtube_links(message):
    """Extract YouTube links from a message using a regular expression."""
    youtube_regex = r'(https:\/\/)?(www\.)?(youtube|youtu)\.(com|be)\/(watch\?v=)?([\w-]+)'
    links = re.findall(youtube_regex, message, re.DOTALL)
    return list(set(''.join(match) for match in links))

def main():
    # Log in to Skype
    skype_username = "your skype nic"
    skype_password = getpass("Enter your Skype password: ")
    sk = Skype(skype_username, skype_password, "token.txt")
    
    # Specify the chat ID
    chat_id = "person nic"
    ch = sk.chats[chat_id]

    # Continuously monitor the chat for new messages
    while True:
        try:
            for msg in ch.getMsgs():
                # Print the first 50 characters of the message content
                print(msg.content[:50])
                
                # Extract YouTube links from the message content
                youtube_links = extract_youtube_links(msg.content)
                print(youtube_links)
                
                # Save the extracted links to a file
                if youtube_links:
                    with open("youtube_links.txt", "a") as file:
                        for link in youtube_links:
                            file.write(link + "\n")
                
                # Wait a short period before checking for new messages
                time.sleep(1)
        
        except Exception as e:
            # Handle any exceptions that occur
            print(f"An error occurred: {e}")
            time.sleep(5)  # Wait before retrying

if __name__ == "__main__":
    main()

# Skype YouTube Link Extractor

This script monitors a specific Skype chat for incoming messages, extracts any YouTube links, and saves them to a file named `youtube_links.txt`.

## Features

- Connects to a Skype account using the `skpy` library.
- Monitors a specified Skype chat for new messages.
- Extracts YouTube links from the messages using a regular expression.
- Saves the extracted YouTube links to a text file.

## Requirements

- Python 3.x
- `skpy` library

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/skype-youtube-link-extractor.git
    cd skype-youtube-link-extractor
    ```

2. Install the required libraries:

    ```bash
    pip install skpy
    ```

## Usage

1. Update the script with your Skype credentials and the Skype chat ID:

    ```python
    from skpy import Skype
    from getpass import getpass
    import re

    sk = Skype("your skype nic", getpass(), "token.txt")
    ch = sk.chats["person nic"]
    ```

2. Run the script:

    ```bash
    python skype_youtube_link_extractor.py
    ```

3. The script will continuously monitor the specified Skype chat for new messages and save any extracted YouTube links to `youtube_links.txt`.

## Contributing

If you would like to contribute to this project, please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License.

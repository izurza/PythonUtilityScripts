# Paraphrase Script 🔄

This script automates the task of paraphrasing text. Provide the text and let the script do the rest, breaking down the text into chunks, sending them for paraphrasing, and saving the paraphrased text in a file.

## Usage 🛠
You can easily use this script from the terminal. Navigate to the directory containing `paraphraser.py`, then run:
--data is the text you want to paraphrase.
--config is optional, to choose the browser for Selenium. Default is Firefox.
--limit is optional, to set the word limit per batch. Default is 125

```bash
python3 paraphraser.py --data "Your text here." --config Firefox --limit 125
```
## Requirements 📋
- Python 3
- Selenium WebDriver

## Setup 🔧
Ensure you have all necessary packages installed. Install dependencies using the provided `requirements.txt` file with pip.

## Contributions 🤝
Contributions are welcome. Feel free to open an Issue or a Pull Request.

## License 📄
This project is licensed under the MIT License - see the LICENSE.md file for details.

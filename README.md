# ФШ Grammar Fix Script

This is a Python script that uses the OpenAI API to check and correct the grammar and style of text using the GPT-3.5 Turbo or Text-DaVinci-003 models. It provides a convenient way to enhance the quality of text by refining its grammar and style. Additionally, it offers the option to switch between the two models.

## Usage

1. Clone or download this repository to your local machine.

2. Install the required Python packages. You can use pip to install the necessary dependencies. You can do this with the following command:

`pip install -r requirements.txt`

3. Set up your OpenAI API key by replacing `"YOUR_OPENAI_API_KEY"` with your actual API key in the script.

4. Run the script:

`python.exe ai-grammar_fix.py`

or, if you want to run it windowless:

`pythonw.exe ai-grammar_fix.py`

Once the script is running (you will notice the abc icon in your Windows tray bar), you can utiuse the following features (click on a tray icon with the right mouse button):

- **Hotkey Trigger**: Press `Alt+Ctrl+G` to initiate the grammar check process. This will copy the selected text, check its grammar and style, and replace it with the corrected text on your clipboard.

- **Model Switching**: You can switch between the GPT-3.5 Turbo and Text-DaVinci-003 models by right-clicking the script's system tray icon and selecting "Switch Model."

- **Exit**: To exit the script, right-click the system tray icon and select "Exit."

## Notes
- The script has been tested to run under Windows 10 and Python 3.12.

- The script emulates the copy (`Ctrl+C`) and paste (`Ctrl+V`) actions to interact with the clipboard.

- The model used for grammar checking can be switched between GPT-3.5 Turbo and Text-DaVinci-003.

- Make sure to keep your OpenAI API key secure and replace `"YOUR_OPENAI_API_KEY"` with your actual key.

- The icon for the system tray is set as "grammar-fix.ico," which should be placed in the same directory as the script.

- This script is tailored for Windows; if you are using a different operating system, some features may not work as expected.

- This script was last updated with knowledge up to September 2021, and any changes or updates to dependencies may require modifications to the script.

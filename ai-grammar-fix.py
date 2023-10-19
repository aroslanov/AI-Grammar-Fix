import pyautogui
import keyboard
import time
import openai
import pyperclip
import sys
import os
import pystray
from PIL import Image
from pynput.keyboard import Controller, Key
from pystray import MenuItem as item
import easygui
#import ctypes

kbd = Controller()
#global model
model = "gpt-3.5-turbo" if len(sys.argv) > 1 and sys.argv[1] == "-gpt" else "text-davinci-003"

# Set your OpenAI API key
api_key = "YOUR_OPENAI_API_KEY"
prompt = "Check the grammar and style of the following text (be polite and as short as possible):\n{text}\n\nCorrected text:"
gpt_prompt = "You are a grammar and style editor, tasked with enhancing the quality of the given text. Your goal is to refine the grammar and style to make the content more precise, coherent, and engaging."

# Function to check grammar using OpenAI API
def check_grammar(text, model):
    openai.api_key = api_key
    if model == "gpt-3.5-turbo":
        openai.api_key = api_key
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": gpt_prompt},
                {"role": "user", "content": prompt.format(text=text)},
            ],
            max_tokens=100,
            temperature=0,
        )
        corrected_text = response.choices[0].message.content.strip()
    else:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt.format(text=text),
            max_tokens=100,
            temperature=0,
        )
        corrected_text = response.choices[0].text.strip()
    return corrected_text

# Function to get text from clipboard
def get_text_from_clipboard():
    return pyperclip.paste()

# Function to set text to clipboard
def set_text_to_clipboard(text):
    pyperclip.copy(text)

#Here is a function to emulate Ctrl+C (copy). I understand that it may not be the most elegant solution, but it is the only way it works on my PC.
def copy_text():
    pyautogui.hotkey('ctrl', 'c')
    pyautogui.keyDown('ctrl')
    pyautogui.keyDown('c')
    pyautogui.keyUp('c')
    pyautogui.keyUp('ctrl')
    keyboard.press_and_release('ctrl+c')
    kbd.press(Key.ctrl)
    kbd.press('c')
    kbd.release('c')
    kbd.release(Key.ctrl)

# Function to paste text from clipboard
def paste_text():
    pyautogui.hotkey('ctrl', 'v')

def switch_model(item):
    global icon
    global model
    if model == "gpt-3.5-turbo":
        model = "text-davinci-003"
    else:
        model = "gpt-3.5-turbo"
    easygui.msgbox(f"Model switched to {model}", title="Model Switched")
    #ctypes.windll.user32.MessageBoxW(0, f"Model switched to {model}", "Model Switched", 1)


def exit_action(icon, item):
    icon.stop()    

def init_tray_icon():
    global icon
    # Get the script's directory
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Construct the full path to the icon image
    icon_path = os.path.join(script_dir, "grammar-fix.ico")

    image = Image.open(icon_path) 
    icon = pystray.Icon("AI Grammar Fix", image, "AI Grammar Fix", menu=generate_menu())
    icon.run()

def generate_menu():
    return pystray.Menu(
        item('Switch Model', switch_model),
        item('Exit', exit_action),
    )

def main():
    # Register a hotkey (Alt+Ctrl+G) to trigger the grammar check process
    keyboard.add_hotkey('alt+ctrl+g', lambda: check_and_correct_grammar())

    # Initialize the tray icon and menu
    init_tray_icon()

def check_and_correct_grammar():
    # Simulate Ctrl+C (copy) to copy selected text to clipboard
    copy_text()

    # Delay to ensure the clipboard has the copied text
    time.sleep(0.5)

    # Get text from clipboard
    text_to_check = get_text_from_clipboard()
    #print(text_to_check)

    if not text_to_check:
        print("Clipboard is empty.")
        return

    # Check grammar using the appropriate function based on the option
    corrected_text = check_grammar(text_to_check, model)

    # Set corrected text to clipboard
    set_text_to_clipboard(corrected_text)

    print(f"Grammar check complete using {model}. Corrected text copied to clipboard.")
    
    paste_text()

if __name__ == "__main__":
    main()

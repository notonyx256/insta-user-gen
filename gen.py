import itertools
import requests
import time

# Function to generate all possible 4-character combinations
def generate_usernames():
    chars = "abcdefghijklmnopqrstuvwxyz"
    combinations = itertools.product(chars, repeat=4)
    usernames = [''.join(combo) for combo in combinations]
    return usernames

# Function to check if a username is available (Instagram doesn't provide an official API for this)
def check_availability(username):
    url = f"https://www.instagram.com/{username}/"
    response = requests.get(url)

    # If the response is a 404, the username is available
    if response.status_code == 404:
        return True
    return False

# Main function to find available usernames
def find_available_usernames():
    usernames = generate_usernames()
    available_usernames = []

    for username in usernames:
        # Check availability
        try:
            if check_availability(username):
                print(f"Username available: {username}")
                available_usernames.append(username)
        except Exception as e:
            print(f"Error checking {username}: {e}")

        # Wait to avoid hitting Instagram's rate limit
        time.sleep(0.5)  # Adjust the sleep time as needed to avoid blocking

    return available_usernames

# Run the function and get the available usernames
available_usernames = find_available_usernames()
print(f"Found {len(available_usernames)} available usernames.")
  

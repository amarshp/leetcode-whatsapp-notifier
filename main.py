import requests
import os
from twilio.rest import Client

# === LeetCode usernames ===
users = {
    "FipPBdPicZ": "Amarsh",
    "codezilla1305": "Vivek"
}

# === Twilio credentials ===
twilio_whatsapp_number = "whatsapp:+14155238886"
account_sid = os.getenv("ACCOUNT_SID")
auth_token = os.getenv("AUTH_TOKEN")
your_whatsapp_number = os.getenv("WHATSAPP_TO")


# === LeetCode query function ===
def get_user_stats(username):
    url = "https://leetcode.com/graphql"
    query = {
        "query": """
        query getUserProfile($username: String!) {
          allQuestionsCount {
            difficulty
            count
          }
          matchedUser(username: $username) {
            submitStatsGlobal {
              acSubmissionNum {
                difficulty
                count
              }
            }
          }
        }
        """,
        "variables": {"username": username}
    }

    headers = {"Content-Type": "application/json"}
    response = requests.post(url, json=query, headers=headers)

    if response.status_code != 200:
        raise Exception(f"Failed to fetch data for {username}")

    data = response.json()
    stats = data['data']['matchedUser']['submitStatsGlobal']['acSubmissionNum']
    solved = {d['difficulty'].lower(): d['count'] for d in stats}
    return solved

# === Score calculation ===
def calculate_score(stats):
    return (
        stats.get('easy', 0) * 1 +
        stats.get('medium', 0) * 2 +
        stats.get('hard', 0) * 4
    )

# === Enhanced comparison message with detailed stats ===
def get_comparison_message(u1, u2):
    stats1 = get_user_stats(u1)
    stats2 = get_user_stats(u2)

    score1 = calculate_score(stats1)
    score2 = calculate_score(stats2)

    name1 = users[u1]
    name2 = users[u2]

    # Build the main comparison message
    if score1 > score2:
        diff = score1 - score2
        main_msg = f"{name1} is beating {name2} by {diff} points today 🔥"
    elif score2 > score1:
        diff = score2 - score1
        main_msg = f"{name2} is beating {name1} by {diff} points today 🔥"
    else:
        main_msg = f"{name1} and {name2} are tied at {score1} points 🤝"

    # Build detailed stats for both users
    def format_user_stats(name, stats, score):
        easy = stats.get('easy', 0)
        medium = stats.get('medium', 0)
        hard = stats.get('hard', 0)
        return f"{name}: {score} points ({easy} easy, {medium} medium, {hard} hard)"

    user1_details = format_user_stats(name1, stats1, score1)
    user2_details = format_user_stats(name2, stats2, score2)

    # Combine everything into the final message
    full_message = f"""✅ Daily LeetCode Update:
{main_msg}

📊 Current Scores:
{user1_details}
{user2_details}"""

    return full_message

# === Send WhatsApp message ===
def send_whatsapp_message(body):
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body=body,
        from_=twilio_whatsapp_number,
        to=your_whatsapp_number
    )
    print(f"Sent message ID: {message.sid}")

# === Run ===
if __name__ == "__main__":
    try:
        message = get_comparison_message("FipPBdPicZ", "codezilla1305")
        print("Message to send:")
        print(message)
        print("\n" + "="*50 + "\n")
        send_whatsapp_message(message)
    except Exception as e:
        print("Error:", e)
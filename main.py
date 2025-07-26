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

# === Compare and build message ===
def get_comparison_message(u1, u2):
    stats1 = get_user_stats(u1)
    stats2 = get_user_stats(u2)

    score1 = calculate_score(stats1)
    score2 = calculate_score(stats2)

    name1 = users[u1]
    name2 = users[u2]

    if score1 > score2:
        diff = score1 - score2
        msg = f"{name1} is beating {name2} by {diff} points today 💪"
    elif score2 > score1:
        diff = score2 - score1
        msg = f"{name2} is beating {name1} by {diff} points today 🔥"
    else:
        msg = f"{name1} and {name2} are tied at {score1} points 🟰"

    return msg

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
        print("Message to send:", message)
        send_whatsapp_message(message)
    except Exception as e:
        print("Error:", e)

# 📈 LeetCode WhatsApp Notifier

Automatically compares two LeetCode users' progress daily and sends a score update to WhatsApp using Twilio.

---

## 🚀 Features

- Fetches LeetCode stats for two users
- Calculates score using custom formula:

  \`\`\`
  score = (easy × 1) + (medium × 2) + (hard × 4)
  \`\`\`

- Sends a message like:  
  > Vivek is beating Amarsh by 18 points today 💪

- Runs daily using GitHub Actions  
- Uses Twilio WhatsApp API (free tier supported)

---

## 🔧 Setup

### 1. Clone the Repository

\`\`\`bash
git clone https://github.com/YOUR_USERNAME/leetcode-whatsapp-notifier.git
cd leetcode-whatsapp-notifier
\`\`\`

### 2. Create \`main.py\`

Contains the LeetCode comparison and Twilio messaging logic.

### 3. Install Dependencies

\`\`\`bash
pip install -r requirements.txt
\`\`\`

### 4. Set Up GitHub Secrets

Go to **Settings → Secrets → Actions → New repository secret**, and add:

| Name            | Value                                  |
|-----------------|----------------------------------------|
| \`TWILIO_SID\`    | Your Twilio Account SID                |
| \`TWILIO_AUTH\`   | Your Twilio Auth Token                 |
| \`WHATSAPP_TO\`   | Your WhatsApp number (\`whatsapp:+91...\`) |

You can get these from the [Twilio WhatsApp Sandbox](https://www.twilio.com/console/sms/whatsapp/learn)

---

## 🕒 GitHub Actions

This workflow is in \`.github/workflows/daily.yml\` and is set to:

- ⏰ Run every day at **9:30 AM IST** (\`0 4 * * *\` UTC)  
- 🧪 Supports manual trigger via \`workflow_dispatch\`

### To test it manually:

1. Go to the **Actions** tab  
2. Select the workflow  
3. Click **“Run workflow”**

---

## ✏️ Customize

- Change usernames in \`main.py\`:

  \`\`\`python
  users = {
      "FipPBdPicZ": "Amarsh",
      "codezilla1305": "Vivek"
  }
  \`\`\`

- Change scoring weights or message format if desired  
- Add history tracking, leaderboard, or Google Sheets logging

---

## 📱 Demo Output

\`\`\`
Vivek is beating Amarsh by 14 points today 🔥
\`\`\`

---

## 📦 Tech Stack

- Python 3  
- Twilio WhatsApp API  
- GitHub Actions  
- LeetCode GraphQL API

---

## 🛡️ License

MIT License — free to use, modify, and share!

---

Made with ❤️ for coding rivalries!

# 📈 LeetCode WhatsApp Notifier

Automatically compares two LeetCode users' progress daily and sends a score update to WhatsApp using Twilio.

## 🚀 Features

- Fetches LeetCode stats for two users via GraphQL API
- Calculates score using custom formula: **score = (easy × 1) + (medium × 2) + (hard × 4)**
- Sends personalized messages like: *"Vivek is beating Amarsh by 18 points today 💪"*
- Runs daily using GitHub Actions scheduler
- Uses Twilio WhatsApp API (free tier supported)

## 🔧 Setup

### 1. Clone the Repository
```bash
git clone https://github.com/YOUR_USERNAME/leetcode-whatsapp-notifier.git
cd leetcode-whatsapp-notifier
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure User Settings
Edit the usernames in `main.py`:
```python
users = {
    "FipPBdPicZ": "Amarsh",
    "codezilla1305": "Vivek"
}
```

### 4. Set Up Twilio WhatsApp
1. Create a [Twilio account](https://www.twilio.com/try-twilio)
2. Access the [Twilio WhatsApp Sandbox](https://www.twilio.com/console/sms/whatsapp/learn)
3. Follow the sandbox setup instructions to connect your WhatsApp number

### 5. Configure GitHub Secrets
Go to **Settings → Secrets and variables → Actions → New repository secret** and add:

| Secret Name     | Description                           | Example                    |
|-----------------|---------------------------------------|----------------------------|
| `TWILIO_SID`    | Your Twilio Account SID               | `ACxxxxxxxxxxxxxxxx`       |
| `TWILIO_AUTH`   | Your Twilio Auth Token                | `xxxxxxxxxxxxxxxx`         |
| `WHATSAPP_TO`   | Your WhatsApp number                  | `whatsapp:+1234567890`     |

## 🕒 Automation with GitHub Actions

The workflow file `.github/workflows/daily.yml` is configured to:
- ⏰ Run every day at **9:30 AM IST** (`30 4 * * *` in UTC)
- 🧪 Support manual triggers via `workflow_dispatch`

### Manual Testing
1. Go to the **Actions** tab in your repository
2. Select the "Daily LeetCode Comparison" workflow
3. Click **"Run workflow"** → **"Run workflow"**

## 📋 Project Structure
```
leetcode-whatsapp-notifier/
├── main.py                    # Main script with comparison logic
├── requirements.txt           # Python dependencies
├── .github/workflows/daily.yml # GitHub Actions workflow
└── README.md                  # This file
```

## ✏️ Customization Options

### Change Scoring Formula
Modify the scoring weights in `main.py`:
```python
def calculate_score(easy, medium, hard):
    return (easy * 1) + (medium * 2) + (hard * 4)
```

### Customize Messages
Update the message format in the notification function:
```python
if score1 > score2:
    message = f"{name1} is beating {name2} by {score1 - score2} points today 🔥"
```

### Future Enhancements
- Add weekly/monthly summaries
- Track progress history
- Create leaderboard with multiple users
- Integration with Google Sheets for data logging
- Add streak tracking and achievements

## 📱 Sample Output
```
✅ Daily LeetCode Update:
Vivek is beating Amarsh by 14 points today 🔥

📊 Current Scores:
Vivek: 156 points (12 easy, 28 medium, 8 hard)
Amarsh: 142 points (18 easy, 22 medium, 7 hard)
```

## 🛠️ Tech Stack
- **Python 3.8+** - Core programming language
- **Twilio API** - WhatsApp messaging service
- **GitHub Actions** - Automated scheduling
- **LeetCode GraphQL API** - Data fetching
- **Requests** - HTTP client library

## 🐛 Troubleshooting

### Common Issues
- **Authentication Error**: Verify your Twilio credentials in GitHub Secrets
- **WhatsApp Not Receiving**: Ensure your number is properly connected to Twilio sandbox
- **Workflow Not Running**: Check if the repository has Actions enabled
- **LeetCode API Issues**: Verify usernames are correct and profiles are public

### Debug Mode
Add debug logging by setting environment variable:
```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

## 🤝 Contributing
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)  
5. Open a Pull Request

## 📄 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments
- LeetCode for providing the GraphQL API
- Twilio for the WhatsApp integration
- GitHub Actions for free automation

---
*Made with ❤️ for coding rivalries and friendly competition!*

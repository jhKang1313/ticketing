from slack_sdk import WebhookClient
from slack_sdk.errors import SlackApiError
def send_slack_notification(message):
    client = WebhookClient("https://hooks.slack.com/services/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")
    try:
        response = client.send(text=message)
    except SlackApiError as e:
        print("Error sending Slack notification:", e.response["error"])

#notification_message = "이제또 까네"

# Slack에 알림 보내기
#send_slack_notification(notification_message)




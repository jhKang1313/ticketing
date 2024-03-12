from slack_sdk import WebhookClient
from slack_sdk.errors import SlackApiError
from datetime import datetime
def send_slack_notification(webhook_url, message):
    client = WebhookClient(webhook_url)

    try:
        response = client.send(text=message)
    except SlackApiError as e:
        print("Error sending Slack notification:", e.response["error"])

slack_webhook_url = "https://hooks.slack.com/services/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"

datetime.strftime(datetime.now(), 'yyyyMMdd')
notification_message = f"Time is {datetime.strftime(datetime.now(), 'yyyyMMdd')}"

# Slack에 알림 보내기
send_slack_notification(slack_webhook_url, notification_message)




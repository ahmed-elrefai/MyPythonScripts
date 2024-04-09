import os.path
import base64
import mimetypes
from email.message import EmailMessage

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/gmail.modify"]


def build_gmail_service():
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
          creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
            "creds.json", SCOPES
        )
        creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open("token.json", "w") as token:
            token.write(creds.to_json())
    return build("gmail", "v1", credentials=creds)

def main():
    """Shows basic usage of the Gmail API.
    Lists the user's Gmail labels.
    """
    service = build_gmail_service()
    mail_subject = "Eid Mubarak!"
    mail_text = """Hello There, this is this is just Ahmed Elrefai
wishing you happy eid, through a python automated message.
Check linkedin to know more!
https://www.linkedin.com/in/ahmed-elrefai/"""
    emails = ["mail1@domain.com", "mail2@domain.com", "mail3@domain.com"]
    # attachment = "eid mubarak.jpeg"
    # message = create_draft(service, TO, mail_subject, mail_text)
    # send_draft(service,message)
    for TO in emails:
        send_message(service, TO, mail_subject, mail_text)

def create_draft(service, TO, subject , mail_content, attachment=None) -> EmailMessage:
    user_profile = service.users().getProfile(userId='me').execute()
    me = user_profile['emailAddress']
    message = EmailMessage()

    message["From"] = me
    message["To"] = TO
    message["Subject"] = subject
    message.set_content(mail_content)
        
    if attachment: 
        type_subtype, _ = mimetypes.guess_type(attachment)
        maintype, subtype = type_subtype.split("/")

        with open(attachment, "rb") as fp:
            attachment_data = fp.read()
        message.add_attachment(attachment_data, maintype, subtype)

    encoded_message = base64.urlsafe_b64encode(message.as_bytes()).decode()

    create_draft_request_body = {"message": {"raw": encoded_message}}
    draft = (
        service.users()
        .drafts()
        .create(userId="me", body=create_draft_request_body)
        .execute()
    )
    return message

def send_draft(service, message:EmailMessage):
    encoded_message = base64.urlsafe_b64encode(message.as_bytes()).decode()

    create_message = {"raw": encoded_message}
    send_message = (
        service.users()
        .messages()
        .send(userId="me", body=create_message)
        .execute()
    )
    print("Draft sent successfully!, id:", send_message['id'])

def send_message(service, TO, mail_subject , mail_content, attachment=None):
    user_profile = service.users().getProfile(userId='me').execute()
    me = user_profile['emailAddress']
    message = EmailMessage()

    message["From"] = me
    message["To"] = TO
    message["Subject"] = mail_subject
    message.set_content(mail_content)
        
    if attachment: 
        type_subtype, _ = mimetypes.guess_type(attachment)
        maintype, subtype = type_subtype.split("/")

        with open(attachment, "rb") as fp:
            attachment_data = fp.read()
        message.add_attachment(attachment_data, maintype, subtype)

    encoded_message = base64.urlsafe_b64encode(message.as_bytes()).decode()

    create_message = {"raw": encoded_message}
    send_message = (
        service.users()
        .messages()
        .send(userId="me", body=create_message)
        .execute()
    )
    print("email sent successfully!, id:", send_message['id'])

if __name__ == "__main__":
  main()
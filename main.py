
import poplib
from email import parser

from env import USERNAME, PASSWORD


def print_mails():
    pop_conn = poplib.POP3_SSL('pop.mail.ru', 995)
    pop_conn.user(USERNAME)
    pop_conn.pass_(PASSWORD)
    mailbox_size = pop_conn.stat()
    print("mailbox size is " + str(mailbox_size))

    # Get messages from server:
    messages = [pop_conn.retr(i) for i in range(1, len(pop_conn.list()[1]) + 1)]

    # Concat message pieces:
    messages = [b"\n".join(mssg[1]) for mssg in messages]

    # Parse message intom an email object:
    messages = [parser.Parser().parsestr(mssg.decode('utf-8')) for mssg in messages]
    for message in messages:
        print(f"{message['subject']} : {message['From']}\n")
        print(f"Date : {message['Date']}\n")
        print(f"To : {message['To']}\n")
        for part in message.walk():
            if part.get_content_type():
                body = part.get_payload(decode=True)
                print(body)
    pop_conn.quit()


if __name__ == '__main__':
    print_mails()


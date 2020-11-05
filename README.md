## Description 
The POP module allows getting messages from email.

## Using
To use the module for your email, you need to turn off two-factor authentication, so it is recommended to use the test email address with not real and not important information.

| mail provider |       url         | port    |
|---------------|:-----------------:|:-------:|
| mail          | pop.mail.ru       | 995     |
| gmail         | pop.gmail.com     | 995     |
| microsoft     | pop3.live.com     | 995     |

to get connection `pop_conn = poplib.POP3_SSL('pop.mail.ru', 995)`
to get authorization:
`pop_conn.user(USERNAME)`
`pop_conn.pass_(PASSWORD)`
where `USERNAME` and `PASSWORD` your credentials

to get mails size `mailbox_size = pop_conn.stat()`
to get information `message[<name_of_info>]`

[more information](https://docs.python.org/3/library/poplib.html)
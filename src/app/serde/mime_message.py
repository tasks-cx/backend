from email import policy
from email.parser import Parser

from app.entities.contract import Contract
from app.entities.host import Host
from app.entities.project import Project
from app.entities.task import Task
from app.entities.user import User

class MimeMessage:
    @staticmethod
    def parse_mime_message(raw_message):
        res = []
        parser = Parser(policy=policy.HTTP)
        message = parser.parsestr(raw_message)

        if message.is_multipart():
            for part in message.iter_parts():
                content_type = part.get_content_type()
                content = part.get_content().decode('utf8')

                match content_type:
                    case "application/json+contract":
                        res.append(Contract(content))
                    case "application/json+host":
                        res.append(Host(content))
                    case "application/json+project":
                        res.append(Project(content))
                    case "application/json+task":
                        res.append(Task(content))
                    case "application/json+user":
                        res.append(User(content))
                    case _:
                        continue

        else:
            content_type = message.get_content_type()
            content = message.get_content().decode('utf8')

            match content_type:
                case "application/json+contract":
                    res.append(Contract(content))
                case "application/json+host":
                    res.append(Host(content))
                case "application/json+project":
                    res.append(Project(content))
                case "application/json+task":
                    res.append(Task(content))
                case "application/json+user":
                    res.append(User(content))
                case _:
                    pass
                        
        return res

"""
    example = \"""MIME-Version: 1.0
    Content-Type: multipart/mixed; boundary=frontier

    This is a message with multiple parts in MIME format.
    --frontier
    Content-Type: application/json+contract

    {"uuid":"50f6fae6-99f9-4c72-a7d6-08e8a44342af","project_id":"046e5ca1-4079-4f19-9c4f-ed6f527d275c@wantguns.dev","member_id":"wantguns@wantguns.dev","sign":"ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad","expiry":1692283086,"witness":["3d6edecb-032b-46bb-bce1-87160a17e599","00ce3e9e-322a-46d5-a360-212663ac71ac"],"access":"something"}
    --frontier
    Content-Type: application/octet-stream
    Content-Transfer-Encoding: base64

    PGh0bWw+CiAgPGhlYWQ+CiAgPC9oZWFkPgogIDxib2R5PgogICAgPHA+VGhpcyBpcyB0aGUg
    Ym9keSBvZiB0aGUgbWVzc2FnZS48L3A+CiAgPC9ib2R5Pgo8L2h0bWw+Cg==
    --frontier--
    \"""

    print(MimeMessage.parse_mime_message(example)[0])

        Contract(uuid: 50f6fae699f94c72a7d608e8a44342af, project_id: 046e5ca140794f199c4fed6f527d275c@wantguns.dev, member_id: wantguns@wantguns.dev, sign: ba7816bf8f01cfea414140de5dae2223b00361a396177a9c b410ff61f20015ad, expiry: 2023-08-17 14:38:06+00:00, witness: ['3d6edecb-032b-46bb-bce1-87160a17e599', '00ce3e9e-322a-46d5-a360-212663ac71ac'], access: something)
"""

import datetime
from dataclasses import dataclass
from datetime import date

@dataclass
class User:
    first_name: str
    last_name: str
    email: str
    phone: str
    address: str
    birthday: datetime.date
    gender: str
    subject: str
    hobbies: str
    image: str
    state: str
    city: str


test_user = User(
    first_name='Ksenia',
    last_name='Kapranova',
    email='ksenya14039@mail.ru',
    phone='9973655228',
    address='Moscow',
    birthday=date(1997, 10, 9),
    gender='Female',
    subject='English',
    hobbies='Reading',
    image='wepk.jpeg',
    state='NCR',
    city='Delhi')
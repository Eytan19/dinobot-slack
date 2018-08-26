import requests
import datetime
import json
import argparse
from os import environ


BIRTHDAY_DATA = (
    ['Erica', 'Abramson', '6/21'],
    ['Bolu', 'Adeyeye', '12/22'],
    ['Matt', 'Ale', '6/26'],
    ['Khalid', 'Almoammar', '2/10'],
    ['Josh', 'Andermarch', '12/12'],
    ['Jamsheer', 'Anklesaria', '6/7'],
    ['Mio', 'Asatani', '6/27'],
    ['Dara', 'Blume', '8/13'],
    ['Benny', 'Bursztyn', '10/20'],
    ['Pranav', 'Chachra', '11/3'],
    ['Lisa', 'Chen', '12/21'],
    ['April', 'Chye', '4/16'],
    ['Jose', 'Clautier', '3/17'],
    ['Anya', 'Clifford', '5/24'],
    ['Maor', 'Cohen', '7/22'],
    ['Daniel', 'Dall Acqua', '7/12'],
    ['Greg', 'Doger de Speville', '1/15'],
    ['Hannah', 'Dolgin', '11/28'],
    ['Gillian', 'Dudeck', '7/15'],
    ['Evan', 'Einstein', '4/10'],
    ['Matt', 'Ellis', '12/11'],
    ['Mike', 'Flum', '3/9'],
    ['Kevin', 'Gallagher', '10/18'],
    ['Mitch', 'Gorodokin', '5/10'],
    ['Lindley', 'Gray', '8/25'],
    ['Anchal', 'Gulati', '2/22'],
    ['Oscar', 'Hentschel', '11/4'],
    ['Morgan', 'Holmes', '7/13'],
    ['Keita', 'Ito', '4/4'],
    ['Nick', 'Karr', '11/23'],
    ['Liz', 'Kelley', '9/23'],
    ['Erik', 'Kogut', '12/18'],
    ['Brandon', 'Kong', '1/3'],
    ['Joon', 'Lee', '6/4'],
    ['Joe', 'Lin', '8/20'],
    ['Jeffrey', 'Lothian', '2/26'],
    ['Sandra', 'Lucia', '2/13'],
    ['Joe', 'Lynch', '11/12'],
    ['Liz', 'McCue', '3/29'],
    ['Gabriel', 'Metzger', '6/24'],
    ['Will', 'Miller', '12/15'],
    ['Cyrus', 'Mojdehi', '2/8'],
    ['Mark', 'Mosby', '2/1'],
    ['Amelia', 'Munson', '12/22'],
    ['Gladys', 'Ndagire', '10/2'],
    ['Kelly', "O'Brien", '12/24'],
    ['Valentina', 'Pardo', '11/12'],
    ['Alexa', 'Picciotto', '1/31'],
    ['Adi', 'Prasad', '9/3'],
    ['Justin', 'Reggi', '5/12,'],
    ['Laura', 'Rodgers', '4/2'],
    ['Eytan', 'Schindelhaim', '10/22'],
    ['Janaki', 'Sekaran', '1/2'],
    ['Sid', 'Shanbhag', '7/9'],
    ['David', 'Streger', '4/25'],
    ['Vincent', 'Su', '10/4'],
    ['Maeve', 'Tsivanidis', '8/8'],
    ['Naomi', 'Tudhope', '8/24'],
    ['Nivedita', 'Venkateish', '7/24'],
    ['Rachel', 'Wasser', '4/26'],
    ['Jasper', 'Wu', '12/25'],
    ['Frank', 'Yodice', '6/6'],
    ['Zenah', 'Hasan', '2/1'],
    ['Vicci', 'Zhong', '8/19'],
    ['Sherie', 'Zhou', '8/17'],
)

parser = argparse.ArgumentParser()
parser.add_argument('token')
args = parser.parse_args()

TOKEN = args.token

POST_URL = 'https://hooks.slack.com/services/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'

MEMBER_URL = 'https://columbiabizschool.slack.com/api/users.list'

PARAMS = {'token': TOKEN}

HEADERS = {'content-type': 'application/json'}

def id_lookup():

    response = requests.get(MEMBER_URL, params=PARAMS, headers=HEADERS).json()
    members = response['members']
    id_dict = {member['profile']['real_name']:member['id'] for member in members}
    return id_dict

def bdays(birthday_data, today, id_dict):
    
    todays_bdays = []
    for row in birthday_data:
        bday = row[2]
        bday = bday.split('/')
        month = bday[0]
        day = bday[1]
        if int(month) == today.month and int(day) == today.day:
            todays_bdays.append(row)

    for todays_bday in todays_bdays:
        first_name, last_name = todays_bday[0], todays_bday[1]
        user_id = id_dict[first_name + ' ' + last_name]
        data = {'text': 'Happy birthday <@{}>!!!'.format(user_id)}
        requests.post(POST_URL, data=json.dumps(data), headers=HEADERS)


def main():
    
    today = datetime.datetime.now()
    id_dict = id_lookup()
    bdays(BIRTHDAY_DATA, today, id_dict)


if __name__ == '__main__':
    main()

import requests
import json
from config import config

in_db = ['28815599', '28698911', '28663712', '28523646', '28565173', '28435937', '26950122', '27972554', '28500901',
         '28526918', '28067536', '28521838', '28603180', '28161755', '28704071', '26517066', '28741397', '28672379',
         '28787997', '28659964', '28482746', '28536013', '28215348', '28616135', '28659735', '28702142', '28831069',
         '28795206', '27676924', '28318942', '28719982', '28509632', '27029190', '28813160', '28451687', '28393764',
         '28327595', '28757908', '27912647', '26463105', '28704234', '28606194', '27803820', '24150353', '28662357',
         '28431116', '28665299', '28610106', '28517170', '28428084', '28706554', '28323210', '27475468', '28204241',
         '27868031', '28387844', '27120278', '28006552', '25683674', '19544750', '27721624', '27528609', '28653811',
         '28035996', '28439305', '28809151', '28714640', '28654717', '28183412', '28789879', '27399288', '27493569',
         '28380276', '28767896', '28463419', '28543124', '28326331', '28583343', '28604047', '28842690',
         '28350393', '28064099', '28041076', '25565305', '28074199', '27327064', '28681258', '28603609', '27864869']


def get_new_cars():
    page = 0
    ids = []
    response = requests.get(
        'https://developers.ria.com/auto/search?api_key=' + config.autoriaKey + '&marka_id=84&model_id=780&gear_id=2&size=100&page=' + str(
            page))
    jsn = json.loads(response.text)
    this_ids = jsn['result']['search_result']['ids']
    ids += this_ids
    page += 1
    while this_ids:
        response = requests.get(
            'https://developers.ria.com/auto/search?api_key=' + config.autoriaKey + '&marka_id=84&model_id=780&gear_id=2&size=100&page=' + str(
                page))
        jsn = json.loads(response.text)
        this_ids = jsn['result']['search_result']['ids']
        ids += this_ids
        page += 1

    for id in ids:
        if id not in in_db:
            print(id)


if __name__ == '__main__':
    get_new_cars()

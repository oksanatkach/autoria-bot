# coding=utf-8
from collections import namedtuple
from config import config
import datetime
import json
import re
import requests
from typing import Union

carInfoTuple = namedtuple('carInfo', ['sold', 'added', 'last_updated', 'phone', 'location',
                                      'url', 'price', 'year', 'odometer', 'fuel', 'gear', 'vin',
                                      'plate'])


def get_car_info(user_input: str) -> Union[carInfoTuple, None]:
    if 'auto.ria.com' in user_input:
        car_id = user_input.split('.')[-2].split('_')[-1]
    elif user_input.isdigit():
        car_id = user_input
    else:
        re_match = re.search(r'.*?(\d{8}).*?', user_input)
        if re_match:
            car_id = re_match.group(1)
        else:
            return None

    response = requests.get("https://developers.ria.com/auto/info?api_key=" + config.autoriaKey + "&auto_id=" + car_id)
    info = json.loads(response.text)
    date_added = datetime.datetime.strptime(info['addDate'], '%Y-%m-%d %H:%M:%S')
    date_added_prepped = '-'.join([str(date_added.year), str(date_added.month), str(date_added.day)])
    date_updated = datetime.datetime.strptime(info['updateDate'], '%Y-%m-%d %H:%M:%S')
    date_updated_prepped = '-'.join([str(date_updated.year), str(date_updated.month), str(date_updated.day)])

    myInfo = carInfoTuple(
        sold=info['autoData']['isSold'],
        added=date_added_prepped,
        last_updated=date_updated_prepped,
        phone=info['userPhoneData']['phone'] if 'userPhoneData' in info else None,
        location=info['stateData']['name'] if 'stateData' in info else None,
        url='https://auto.ria.com/euk' + info['linkToView'],
        price=str(info['USD']) + ' USD' if 'USD' in info else None,
        year=str(info['autoData']['year']) if 'year' in info['autoData'] else None,
        odometer=str(info['autoData']['raceInt']) + '000 км' if 'raceInt' in info['autoData'] else None,
        fuel=info['autoData']['fuelName'] if 'fuelName' in info['autoData'] else None,
        gear=info['autoData']['gearboxName'] if 'gearboxName' in info['autoData'] else None,
        vin=info['checkedVin']['vin'] if 'checkedVin' in info else None,
        plate=info['plateNumber'] if 'plateNumber' in info else None
    )

    return myInfo


if __name__ == '__main__':
    myInfo = get_car_info('мій код - 28580797')
    print(myInfo.location)
    myInfo = get_car_info('https://auto.ria.com/uk/auto_volkswagen_beetle_28580797.html')

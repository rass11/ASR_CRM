import time
from threading import Thread

import requests as rq


def _test():
    data = {
    "territoryInitiator": {
        "title": None,
        "guid": None,
        "directionCode": None,
        "channelCode": None,
    }
}
    h = 'https://apiman.south.rt.ru/apiman-gateway/sso-crm/territory-recording/1.0-test/v1/territory-initiators'
    # h = 'http://localhost:5000/'
    ttt = int(time.time() % 1000)
    xid = f'local{ttt}testing'
    # data = {}
    res = {}
    def task(i):
        nonlocal data
        data = data.copy()
        data['functions'] = [i]
        res.update({i: rq.get(
            h,
            # json=data,
            headers={
                'X-Request-Id': f'{xid}{i}',
                'X-API-Key': 'adf985f4-2a89-487a-a5c9-0633888bd84e',
                'X-user-id': '0a3aaba1-a817-48d6-9426-12a9aa1aa2cb',
            }
        )})

    #ths = [Thread(target=task, args=(i, )) for i in range(100)]
    t1 = time.perf_counter()
    for i in range(200):
        task(i)
    t2 = time.perf_counter()
    for k, v in sorted(res.items()):
        t = v.elapsed.total_seconds()
        print(f'{xid}{k}> {t}, {v}')
        if t > 2:
            print('THIS!!11'+'#'*70)
        if not v.ok:
            print('\t' + v.text)
    print(res[0].json())
    print(f'total: {t2-t1}')
    breakpoint()
    # assert r.status_code == 200
    # assert r.json() == {'status': 'ok'}

if __name__ == '__main__':
    _test()


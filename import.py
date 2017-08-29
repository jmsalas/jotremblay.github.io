import requests
import json

key = "dc06f2f4a636e8a39081ea3966c79d8c5fd5ae41"
form_id = "txCvPL"
url = "https://api.typeform.com/v1/form/{}?key={}".format(form_id, key)

r = requests.get(url)

json = json.loads(r.content)
json

results = {'data': []}
questions = dict([(x['id'], x['question']) for x in json['questions']])


for answer in json['responses']:
    if answer['answers']:
        ans = {}
        for k, a in answer['answers'].iteritems():
            ans[questions[k]] = a
        results['data'].append(ans)

print results

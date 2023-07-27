import csv

"""
keys of csv:
    - model name
    - submit date
    - affliation: optional
    - setting: open/multi
    - use_sparql: TRUE/FALSE
    - use_program: TRUE/FALSE
    - ensemble: TRUE/FALSE
    - paper link: url, optional
    - conference: str, optional
    - code link: url, optional
    - overall
    - multihop,qualifier,comparison,logical,count,verify,zeroshot
"""
acc_keys = ['overall','multihop','qualifier','comparison','logical','count','verify','zeroshot']

data_open = []
data_multi = []
with open('leaderboard_data.csv') as f:
    f_csv = csv.DictReader(f)
    for row in f_csv:
        for k in acc_keys:
            row[k] = float(row[k])
        if row['setting'] == 'open':
            data_open.append(row)
        elif row['setting'] == 'multi':
            data_multi.append(row)
        else:
            raise Exception('invalid setting "{}"'.format(row['setting']))

data_open = sorted(data_open, key=lambda x: x['overall'], reverse=True)
data_multi = sorted(data_multi, key=lambda x: x['overall'], reverse=True)

acc_max_open = { k:max(d[k] for d in data_open) for k in acc_keys }
acc_max_multi = { k:max(d[k] for d in data_multi) for k in acc_keys }



def generate(data, acc_max):
    for i, d in enumerate(data):
        if d['paper link']:
            paper = f'<a href="{d["paper link"]}" class="paper-link">[{d["conference"] if d["conference"] else "paper"}]</a>'
        else:
            paper = ''

        if d['code link']:
            code = f'<a href="{d["code link"]}" class="paper-link">[code]</a>'
        else:
            code = ''

        if d['affliation']:
            affliation = f'<span class="affliation">{d["affliation"]}</span><br>'
        else:
            affliation = ''

        badge = ''
        if d['use_program'].lower() == 'true':
            badge += '<span class="badge badge-primary">Program</span>'
        if d['use_sparql'].lower() == 'true':
            badge += '<span class="badge badge-success">SPARQL</span>'
        if d['ensemble'].lower() == 'true':
            badge += '<span class="badge badge-info">Ensemble</span>'

        accs = ['<strong>%.2f</strong>'%d[k] if d[k]==acc_max[k] else '%.2f'%d[k] for k in acc_keys]


        s = f'''<tr>
  <td class="align-middle">{i+1}<br><span class="badge badge-secondary">{d["submit date"]}</span></td>
  <td class="align-middle">{d["model name"]}<sup>{badge}</sup><br>{affliation}{paper}{code}</td>
  <td class="align-middle">{accs[0]}</td>
  <td class="align-middle">{accs[1]}</td>
  <td class="align-middle">{accs[2]}</td>
  <td class="align-middle">{accs[3]}</td>
  <td class="align-middle">{accs[4]}</td>
  <td class="align-middle">{accs[5]}</td>
  <td class="align-middle">{accs[6]}</td>
  <td class="align-middle">{accs[7]}</td>
</tr>'''
        print(s)



print("=== open ended ===")
generate(data_open, acc_max_open)

print("\n\n\n=== multiple choice ===")
generate(data_multi, acc_max_multi)

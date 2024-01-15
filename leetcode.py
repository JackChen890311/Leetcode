import os
import requests
import tqdm

with open('../Papers/Leetcode Notes.md', 'r', encoding='utf8') as f:
    text = f.read().split('\n')

os.makedirs('Questions/', exist_ok=True)
os.makedirs('Topics/', exist_ok=True)
N = len(text)
newlist = []
topics = set()

for i in tqdm.tqdm(range(N)):
    line = text[i]
    if line.startswith('## '):
        continue
    elif line.startswith('### '):
        print(line)
        newlist.append((int(line[4:].split('.')[0]),'### [['+line[4:]+']]\n'))
        with open('questions/' + line[4:] + '.md', 'w', encoding='utf8') as f:
            # f.write(line + '\n')
            t = requests.get('https://leetcode.com/problems/' + line[4:].split('.')[1].split('(')[0].strip().lower().replace(' ','-') + '/description/').text
            idx = t.find('topicTags')
            idx2 = t[idx:].find('}}')
            f.write('### Tags:\n')
            try:
                tags = eval(t[idx+11:idx+idx2])
                tags = [tags[i]['name'] for i in range(len(tags))]
                print(tags)
                for t in tags:
                    f.write('- [['+ t + ']]\n')
                    if t not in topics:
                        topics.add(t)
            except:
                print('ERROR!!!', line[4:])
                
            f.write('### Notes:\n')
            while i + 1 < N - 1 and not text[i + 1].startswith('### '):
                if text[i + 1].startswith('## '):
                    i += 1
                    continue
                f.write(text[i + 1] + '\n')
                i += 1
            i -= 1

newlist = sorted(newlist, key=lambda x: x[0])
with open('Questions.md', 'w', encoding='utf8') as ff:
    for i in range(len(newlist)):
        ff.write(newlist[i][1])

with open('Topics.md', 'w', encoding='utf8') as f:
    for t in topics:
        with open('Topics/' + t + '.md', 'w', encoding='utf8') as f:
            f.write('')
        f.write('### [[' + t.split('.')[0] + ']]\n')


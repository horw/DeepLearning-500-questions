import glob

files = glob.glob('**/第*.md', recursive=True)
files = [(int(fp.split('_')[0][2:]), fp) for fp in files]
files.sort()

output = []
for i, fp in files:
    with open(fp) as f:
        for l in f.readlines():
            if l.startswith("#") and (str(i) in l or '第' in l):
                l = l.strip('\n')
                first = True
                new_str = []
                for ch in l:
                    if ch == ' ':
                        ch = '-'
                        if first:
                            ch = ''
                    else:
                        if ch != '#':
                            first = False
                    if ch == '#':
                        continue
                    new_str.append(ch)
                new_str = ''.join(new_str)
                new_str = new_str.replace('.', '').lower().replace('？', '').replace('（', '').replace('）', '').replace(
                    '：', '')
                l = l.strip('#').strip()
                output.append(f"[{l}]({fp}#{new_str})\n\n")

with open("update_table_of_contents.md", 'w+') as f:
    f.write(''.join(output))

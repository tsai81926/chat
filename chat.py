
def read_file(filename):
    lines = []
    with open(filename, 'r', encoding='utf-8-sig') as f:
        for line in f: #如執行cmd前頭出現編碼'\ufeff'，在utf-8後面加'-sig'除去
            lines.append(line.strip())
    return lines

def convert(lines):#convert轉換
    new = []
    person = None #宣告person為虛無，其他語言稱'null'
    for line in lines:
        if line == 'Jeff':
            person = 'Jeff'
            continue
        elif line == 'Tsai':
            person = 'Tsai'
            continue
        if person:#假如person有值
            new.append(person + ': ' + line)
    return new

def write_file(filename, lines):
	with open(filename, 'w') as f:
		for line in lines:
			f.write(line + '\n')

def main():
    lines = read_file('input.txt')
    lines = convert(lines)#將原本參數丟入運算後新的再覆蓋
    write_file('output.txt', lines)

main()
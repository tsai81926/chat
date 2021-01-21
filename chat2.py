
def read_file(filename):
    lines = []
    with open(filename, 'r', encoding='utf-8-sig') as f:
        for line in f: #如執行cmd前頭出現編碼'\ufeff'，在utf-8後面加'-sig'除去
            lines.append(line.strip())
    return lines

def convert(lines):#convert轉換
    new = []
    person = None #宣告person為虛無，其他語言稱'null'
    蔡旻鈞_word_count = 0
    蔡旻鈞_sticker_count = 0
    蔡旻鈞_image_count = 0
    Sean_word_count = 0
    Sean_sticker_count = 0
    Sean_image_count = 0
    for line in lines:
        s = line.split(' ')
        time = s[0]
        name = s[1]
        if name == '蔡旻鈞':
            if s[2] == '貼圖':
                蔡旻鈞_sticker_count += 1
            elif s[2] == '圖片':
                蔡旻鈞_image_count += 1
            else:
                for m in s[2:]:
                    蔡旻鈞_word_count += len(m)
        elif name == 'Sean':
            if s[2] == '貼圖':
                Sean_sticker_count += 1
            elif s[2] == '圖片':
                Sean_image_count += 1
            else:
                for m in s[2]:
                    Sean_word_count += len(m)
    print('蔡旻鈞說了', 蔡旻鈞_word_count, '個字')
    print('蔡旻鈞傳了', 蔡旻鈞_sticker_count, '個貼圖')
    print('蔡旻鈞傳了', 蔡旻鈞_image_count, '張圖片')
    print('Sean說了', Sean_word_count, '個字')
    print('Sean傳了', Sean_sticker_count, '個貼圖')
    print('Sean傳了', Sean_image_count, '張圖片')
def write_file(filename, lines):
    with open(filename, 'w') as f:
        for line in lines:
            f.write(line + '\n')

def main():
    lines = read_file('[LINE]Sean.txt')
    lines = convert(lines)#將原本參數丟入運算後新的再覆蓋
    #write_file('output.txt', lines)

main()
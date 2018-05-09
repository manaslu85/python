print("1번 문제")
data = '이의덕,이재명,권종수,이재수,박철호,강동희,이재수,김지석,최승만,이성만,박영희,박수호,전경식,송우환,김재식,이유정'

names = data.split(",")
park = 0
kim = 0

for name in names:
    if name.startswith('박'):
        park += 1
    elif name.startswith('김'):
        kim += 1

print(kim, park)  # 1. 김씨와 박씨 count 출력
print(names.count('이재수'))  # 2. "이재수"란 이름 count 출력

names = list(set(names))
print(names)  # 3. 중복을 제거한 이름을 출력
print(sorted(names))  # 4. 중복을 제거한 이름을 오름차순으로 정렬하여 출력



print("")
print("2번 문제")
sum1 = 0
sum2 = 0

for i in range(1, 100+1):
    sum1 += i
    sum2 += i**2  # 제곱의 합

sum1 = sum1 ** 2  # 합의 제곱

print(sum1 - sum2)



print("")
print("3번 문제")

from collections import defaultdict

d = defaultdict(int)
for number in range(1, 100+1):
    for c in str(number):
        d[c] += 1

print(dict(d))



print("")
print("4번 문제")

data = "454679323412356743"

numbers = list(map(int, data))  # 숫자 문자열을 숫자 리스트로 변경
result = []

for i, num in enumerate(numbers):
    result.append(str(num))
    if i < len(numbers)-1:  # 다음수가 있다면
        is_odd = num % 2 == 1  # 현재수가 홀수
        is_next_odd = numbers[i+1] % 2 == 1  # 다음수가 홀수
        if is_odd and is_next_odd: # 연속 홀수
            result.append("-")
        elif not is_odd and not is_next_odd: # 연속 짝수
            result.append("*")

print("".join(result))




print("")
print("5번 문제")

def compress_string(s):
    _c = ""
    cnt = 0
    result = ""
    for c in s:
        if c!=_c:
            _c = c
            if cnt: result += str(cnt)
            result += c
            cnt = 1
        else:
            cnt +=1
    if cnt: result += str(cnt)
    return result

print (compress_string("aaabbcccccca")) #a3b2c6a1 출력






print("")
print("6번 문제")

def chkDupNum(s):
    result = [ ]
    for num in s:
        if num not in result:
            result.append(num)
        else:
            return False
    return len(result) == 10

print(chkDupNum("0123456789")) # True 리턴
print(chkDupNum("01234")) # False 리턴
print(chkDupNum("01234567890")) # False 리턴
print(chkDupNum("6789012345")) # True 리턴
print(chkDupNum("012322456789")) # False 리턴




print("")
print("7번 문제")

dic = {
    '.-':'A','-...':'B','-.-.':'C','-..':'D','.':'E','..-.':'F',
    '--.':'G','....':'H','..':'I','.---':'J','-.-':'K','.-..':'L',
    '--':'M','-.':'N','---':'O','.--.':'P','--.-':'Q','.-.':'R',
    '...':'S','-':'T','..-':'U','...-':'V','.--':'W','-..-':'X',
    '-.--':'Y','--..':'Z'
}

def morse(src):
    result = []
    for word in src.split("  "):
        for char in word.split(" "):
            result.append(dic[char])
        result.append(" ")
    return "".join(result)


print(morse('.... .  ... .-.. . . .--. ...  . .- .-. .-.. -.--'))





print("")
print("8번 문제")
import re

p = re.compile("a[.]{3,}b")

print (p.match("acccb")) # None
print (p.match("a....b")) # 매치객체 출력
print (p.match("aaab")) # None
print (p.match("a.cccb")) # None







print("")
print("9번 문제")
import re

p = re.compile('[a-z]+')
m = p.search("5 python")
print(m.start() + m.end()) # 10 출력





print("")
print("10번 문제")
import re

s = """
park 010-9999-9988
kim 010-9909-7789
lee 010-8789-7768
"""

pat = re.compile("(\d{3}[-]\d{4})[-]\d{4}")
result = pat.sub("\g<1>-####", s)

print(result)






print("")
print("11번 문제")
import re

pat = re.compile(".*[@].*[.](?:com$|net$).*$")

print (pat.match("pahkey@gmail.com"))
print (pat.match("kim@daum.net"))
print (pat.match("lee@myhome.co.kr"))




print("")
print("12번 문제")
from xml.etree.ElementTree import Element, SubElement, ElementTree

blog = Element("blog")
blog.attrib["date"] = "20151231"

SubElement(blog, "subject").text = "Why python?"
SubElement(blog, "author").text = "Eric"
SubElement(blog, "content").text = "Life is too short, You need Python!"

ElementTree(blog).write("blog.xml")




print("")
print("13번 문제")
import json

with open('myinfo.json') as f:
    data = json.load(f)  # json파일을 읽고 딕셔너리로 저장한다.

data['age'] = 40  # age 값을 40으로 변경

with open('myinfo.json', 'w') as f:
    json.dump(data, f, indent=4)  # 딕셔너리를 json 파일로 저장한다.





print("")
print("14번 문제")
from operator import itemgetter

students = [
    ("홍길동", 22),
    ("김철수", 32),
    ("박영희", 17),
]

students = sorted(students, key=itemgetter(1))

print(students)


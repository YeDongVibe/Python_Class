#다음 딕셔너리에 대해 물음에 답하라. 
days = {'January':31, 'February':28, 'March':31, 'April':30, 'May':31, 'June':30, 'July':31, 'August':31, 'September':30, 'October':31, 'November':30, 'December':31}
#사용자가 월을 입력하면 해당 월에 일수를 출력하라
# sen = input("월을 입력하세요")
# print('일수는 ',days.get(sen)) 

#알파벳 순서로 모든 월을 출력하라
# res = list(days.keys())
# print(sorted(res))

#일수가 31인 월을 모두 출력하라
# for ress in days:
#     if days[ress] == 31:
#         print(ress)

#월의 일수를 기준으로 오름차순으로 (key-value) 쌍을 출력하라
# res = sorted(days.items(), key= lambda item:item[1])
# print(res)


#사용자가 월을 3자리만 입력하면 월의 일수를 출력하라.(Jan, Feb 등)
# sen = input("월을 3자리까지만 입력하세요")
# for res in days:
#     if res[0:3] == sen.title():
#         print(days[res])

#---------------------------------------------------------------------------------------------------------------------

d = [{'name':'Todd', 'phone':'555-1414', 'email':'todd@mail.net'}, {'name':'Helga', 'phone':'555-1618', 'email':'helga@mail.net'},{'name':'Princess', 'phone':'555-3141', 'email':''},{'name':'LJ', 'phone':'555-2718', 'email':'lj@mail.net'}]

#전화번호가 8로 끝나는 사용자 이름을 출력하라
# for res in d:
#     if res['phone'][7] == '8':
#         print(res['name'])

#이메일이 없는 사용자 이름을 출력하라
# for ress in d:
#     if ress['email'] == '':
#         print("이메일 없는 사람은 ",ress['name'])


#사용자 이름을 입력하면 전화번호, 이메일을 출력하라. 이름이 없으면 '이름이 없습니다'라는 메시지를 출력하라
sen = input("이름을 입력하시오")
flag = 1
for rres in d:
    if rres['name'] == sen:
        print(sen, rres['phone'], rres['email'],'입니다.')
        flag = 0
if flag == 1:
    print(sen,"이름을 가진 사람이 없습니다.")
#학생들의 성적을 딕셔너리로 저장하고, 성적 평균을 계산하는 프로그램을 작성해보세요.
d = {
    "Alice": [85, 90, 95],
    "Bob": [75, 80, 85],
    "Charlie": [95, 95, 95]
}

for name, gr in d.items():
    avg = sum(gr) / len(gr)
    print(name,':',avg)

#숫자들이 들어있는 리스트에서 중복된 숫자를 제거하고, 남은 숫자들의 합을 계산하는 프로그램을 작성해보세요.
da = [1, 2, 2, 3, 3, 3, 4, 4, 5]
res = sum(set(da))
print(res)

#주어진 문자열에서 각 알파벳의 빈도수를 구하는 프로그램을 작성하시오.
text = "Hello, world!"
fre_dic = {}
for ch in text:
    if ch not in fre_dic:
        fre_dic[ch] = 1
    else:
        fre_dic[ch] += 1
print(fre_dic)

#두 개의 리스트가 주어졌을 때, 두 리스트에 공통으로 포함된 요소를 모두 담은 리스트를 반환하는 프로그램을 작성하시오.
list1 = set([1, 2, 3, 4, 5])
list2 = set([2, 4, 6, 8, 10])
print('교집합은',list(list1 & list2))              
print('교집합은',list(list1.intersection(list2)))

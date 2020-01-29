"""
grade = list(map(int, input().split()))
sum = 0
for i in range(len(grade)):
    if 0 <= grade[i] <= 100:
        sum += grade[i]
    else:
        print('잘못된 점수입니다')
        exit()
avg = sum/4
if avg >= 80:
    print("합격입니다.")
else:
    print("불합격입니다.")
"""

korean, english, mathmetics, science = map(int, input().split())
if 0 <= korean <= 100 and 0 <= english <= 100 and 0 <= mathmetics <= 100 and 0 <= science <= 100:
    if (korean + english + mathmetics + science) / 4 >= 80:
        print("합격")
    else:
        print("불합격")
else:
    print("잘못된 점수")
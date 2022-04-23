score_list = [90, 45, 70, 60, 55]
number = 1
for i in score_list:
    if i >= 60:
        result = "합격"
    else:
        result = "불합격"
    print("{}번 학생은 {}입니다.".format(number, result))
    number += 1
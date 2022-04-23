score = int(input("점수입력: "))

if 100 >= score > 90:
    print("{}점은 A학점 입니다.".format(score))

elif 90 >= score > 80:
    print("{}점은 B학점 입니다.".format(score))

elif 80 >= score > 70:
    print("{}점은 C학점 입니다.".format(score))

elif 70 >= score > 60:
    print("{}점은 D학점 입니다.".format(score))

else:
    print("{}점은 F학점 입니다.".format(score))
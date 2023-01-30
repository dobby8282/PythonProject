def get_average(marks):
    total = 0 # 0 + 90 + 80 + 85
    for subject in marks:
        total += marks[subject]

    l_average =total / len(marks)
    return l_average

marks = {'국어': 90, '영어':80, '수학':85}
average = get_average(marks)
print('평균은 {}점 입니다.'.format(average))
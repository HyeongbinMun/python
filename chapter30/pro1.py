korean, english, mathmatics, science = map(int, input().split())
def get_min_max_score(*grade):
    return min(grade), max(grade)
def get_average(**grade):
    return sum(grade.values()) / len(grade)
min_score, max_score = get_min_max_score(korean, english, mathmatics, science)
average_score = get_average(korean=korean, english=english, mathmatics=mathmatics, science=science)

print('낮은 점수 : {0:.2f}, 높은 점수 : {1:.2f}, 평균 점수 : {2:.2f}'.format(min_score, max_score, average_score))

min_score, max_score = get_min_max_score(english, science)
average_score = get_average(english=english, science=science)
print('낮은 점수: {0:.2f}, 높은 점수: {1:.2f}, 평균 점수: {2:.2f}'.format(min_score, max_score, average_score))
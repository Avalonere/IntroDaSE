def score2grade(score):
    grade = ""
    if score < 60:
        grade = "不合格"
    if 60 <= score <= 74:
        grade = "合格"
    if 75 <= score <= 89:
        grade = "良好"
    if score >= 90:
        grade = "优秀"
    return grade

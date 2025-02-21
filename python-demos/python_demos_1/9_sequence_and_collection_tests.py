mylist = [0, 1, 2, 3]
if mylist:
    print("mylist is True because it is not empty")


exam_scores = [0, 67, 25, 80, 72, 0]

if not all(exam_scores):
    print("At least one person scored zero on their test (or didn't take the test)")

if any(exam_scores):
    print("At least one person scored more than zero on their test")

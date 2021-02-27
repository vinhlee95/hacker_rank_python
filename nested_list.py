"""
Given the names and grades for each student in a class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.

https://www.hackerrank.com/challenges/nested-list/problem?h_r=next-challenge&h_v=zen&isFullScreen=false
"""

if __name__ == '__main__':
    name_and_score_list = []
    scores = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        name_and_score_list.append({"name": name, "score": score})
        scores.append(score)

    # Find the 2nd lowest point 🐌🐌🐌
    second_lowest_score = sorted(list(set(scores)))[1]

    # Following way is slower because we need to sort for the whole list initially
    # sorted_list = sorted(name_and_score_list, key=lambda item: item["name"])
    # for item in sorted_list:
    #     if item["score"] == second_lowest_score:
    #         print(item["name"])

    # This way is more efficient 🏎🏎🏎
    names_with_second_lowest_scores = [item["name"] for item in name_and_score_list if
                                       item["score"] == second_lowest_score]
    for name in sorted(names_with_second_lowest_scores):
        print(name)

def get_scores():
    scores = input("Enter scores separated by spaces: ").split()
    return [float(score) for score in scores]


def calculate_sum(scores):
    return sum(scores)


def calculate_average(scores):
    return calculate_sum(scores) / len(scores)


def calculate_maximum(scores):
    return max(scores)


def calculate_minimum(scores):
    return min(scores)


def main():
    scores = get_scores()

    print("Scores:", scores)
    print("Sum:", calculate_sum(scores))
    print("Average:", calculate_average(scores))
    print("Maximum:", calculate_maximum(scores))
    print("Minimum:", calculate_minimum(scores))


if __name__ == "__main__":
    main()

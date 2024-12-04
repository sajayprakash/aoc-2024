count = 0
with open("input.txt", "r") as input:
    reports = input.read().strip().split("\n")
    
    for report in reports:
        levels = list(map(int, report.split()))
        is_increasing = all(1 <= levels[i + 1] - levels[i] <= 3 for i in range(len(levels) - 1))
        is_decreasing = all(1 <= levels[i] - levels[i + 1] <= 3 for i in range(len(levels) - 1))
        
        if is_increasing or is_decreasing:
            count += 1

print("Safe reports:", count)

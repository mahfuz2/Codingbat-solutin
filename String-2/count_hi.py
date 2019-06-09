def count_hi(str):
    count = 0
    for i in range(len(str)):
        if str[i:i + 2] == "hi":
            count = count + 1
    return count


print(count_hi('abc hi ho'),
count_hi('ABChi hi'),
count_hi('hihi'))
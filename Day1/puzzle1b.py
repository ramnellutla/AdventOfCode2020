f = open("input.txt", "r")
lines = f.readlines()

arr = []

for line in lines:
    arr.append(int(line))

arr.sort()

i = 0
while i < len(arr)-2:
    j = i+1
    k = len(arr)-1

    sum = arr[i] + arr[j] + arr[k]

    if sum is 2020:
        print("Numbers: {}, {}, {}; Product: {}".format(
            arr[i], arr[j], arr[k], arr[i] * arr[j] * arr[k])
        return;

    if sum > 2020:
        j += 1;
    else
        i += 1;

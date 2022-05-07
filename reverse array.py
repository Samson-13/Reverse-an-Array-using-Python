# Reverse an Arry
# Made By M Samson Badding
def reverseArr(start, end, arr):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

if __name__ == '__main__':
    arr = ['cool', 'so', 'am', 'I']
    start = 0
    end = len(arr) - 1
    reverseArr(start, end, arr)
    print(' '.join(arr))

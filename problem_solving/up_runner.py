#finding runner-up score ---> second place

if __name__ == '__main__':
    n = int(input("Please enter number of runners: "))
    arr = map(int, input("Please enter runners' scores separated by space: ").split())
    arr = list(arr)
    first_runner = max(arr)
    s = first_runner
    while s == max(arr):
        arr.remove(s)
    print("The second runner's score was : {}".format(max(arr)))
    
    
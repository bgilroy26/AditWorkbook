import time

if __name__ == "__main__":

    n = 0

    while True:
        print("Hello")
        n += 1
        if n == 4:
            break
        time.sleep(n)
    
    print("End of Loop")

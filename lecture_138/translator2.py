d = dict(weather = "clima", earth = "terra", rain = "chuva")

if __name__ == "__main__":
    english = input("Enter word: ")
    if english in d.keys():
        print(d[english])
    else:
        print("We couldn't find that word!")

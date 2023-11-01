import matplotlib.pyplot as plt



def main():
    lang = ["HTML & CSS", "JavaScript", "Kotlin", "Python", "C++", "Java"]
    popularity = [25.0, 55.0, 65.0, 45.0, 85, 75]

    plt.barh(lang, popularity, color=["cyan", "yellow", "orange", "green", "red", "magenta"])
    plt.title("Language Dificulty Guide")
    plt.show()

if __name__ == "__main__":
    main()


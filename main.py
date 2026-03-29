import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("name")
    parser.add_argument("-g", "--greet", default="Hello")

    args = parser.parse_args()

    print(f"{args.greet}, {args.name}!")

if __name__ == "__main__":
    main()

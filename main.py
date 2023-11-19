import os
import requests  # noqa We are just importing this to prove the dependency installed correctly

def main():
    print(os.environ)
    print(os.listdir("."))

if __name__ == "__main__":
    main()

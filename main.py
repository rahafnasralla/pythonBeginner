import fileReader
from csvWriter import csvWriter
def main():
    csvWriter()
    data = fileReader.fileReader('data.csv')
    data.processFile()


if __name__ == "__main__":
    main()



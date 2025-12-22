class FileHandler:
    def write_file(self, filename, content):
        try:
            f = open(filename, "w")
            f.write(content)
            f.close()
            print("File written successfully")
        except Exception as e:
            print("Error while writing file:", e)

    def read_file(self, filename):
        try:
            f = open(filename, "r")
            data = f.read()
            f.close()
            return data
        except FileNotFoundError:
            print("File not found")
        except Exception as e:
            print("Error while reading file:", e)
fh = FileHandler()

fh.write_file("demo.txt", "Hello Aditya\nWelcome to Python")

content = fh.read_file("demo.txt")
print(content)

from model import tiki
import re

def main():
    key = "Quan nam"
    file_name = re.sub(r'\s+','_', key)
    file = f"file/{file_name}.csv"
 
    data = tiki.tiki(key, file)
    data.open_file()
    data.getProduct()
    data.close_file()

if __name__ == "__main__": 
    main()
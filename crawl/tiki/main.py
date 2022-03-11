from model import tiki
import re
import multithread
import multiprocessing
from multiprocessing import Pool, TimeoutError

# def f(i):
#     key = "Quan nam"
#     root_link = f'{key}&page={i}'
#     data = tiki.tiki(root_link, file)
#     data.getProduct()
def main():
    key = "Quan nam"
    file_name = re.sub(r'\s+','_', key)
    file = f"file/{file_name}.csv"
    # for i in range(1,20):
    
    data = tiki.tiki(file_name, file)
    data.open_file()
    # threads = []
    # for i in range(1,10):
    #     root_link = f'{key}&page={i}'
    # 'https://tiki.vn/search?q=Quan nam&page=22'
    p1 = multiprocessing.Process(target=data.getProduct,args={'https://tiki.vn/search?q=Quan nam&page=1'})
    p2 = multiprocessing.Process(target=data.getProduct,args={'https://tiki.vn/search?q=Quan nam&page=2'})
    p3 = multiprocessing.Process(target=data.getProduct,args={'https://tiki.vn/search?q=Quan nam&page=3'})
    p4 = multiprocessing.Process(target=data.getProduct,args={'https://tiki.vn/search?q=Quan nam&page=4'})
    p1.start()
    p2.start()
    p3.start()
    p4.start()
    p1.join()
    p2.join()
    p3.join()
    p4.join()
    data.close_file()
    # with Pool(processes=4) as pool:

    #     # print "[0, 1, 4,..., 81]"
    #     for i in pool.imap_unordered(f, range(1,5)):
    #         print(i)
if __name__ == "__main__": 
    main()
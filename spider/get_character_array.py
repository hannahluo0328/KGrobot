import codecs

# f = codecs.open(r"../data_new/test1.txt", 'r', 'utf-8')
# # f = codecs.open('./raw_data/relation.txt','r','utf-8')
# data = []
# for line in f.readlines():
#     array = line.strip("\n").split("\t")
#     print(array)

def get_character():
    f = codecs.open(r"../data_new/test1.txt",'r','utf-8')
    # f = codecs.open('./raw_data/relation.txt','r','utf-8')
    data = []
    for line in f.readlines():
        array = line.strip("\n").split("\t")
        print(array)
        arr = [array[0],array[1]]
        data.extend(arr)
    
    return data
# if __name__=='__main__':
# get_character()


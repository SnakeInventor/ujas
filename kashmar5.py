def format_data(data):
    """ Loads serialized .csv into dataset-like 2d array 
    
    Arguments:
    data: the string with .csv data
    """
    table = [] 
    data = data.split("\n") 

    for row in data:
        row = row.split(";") 
        if len(row) == 5: 
            category, product, date, price, prodano = row 
            category = category
            product = product 
            date = date.split(".")
            price = float(price)
            prodano = float(prodano) 

            table.append([category, product, date, price, prodano]) 

    return table

def to_csv_string(data):
    """ Serializes dataset-like 2d array into .csv format  
    
    Arguments:
    data: dataset-like 2d array
    """
    s = ""
    for row in data:
        s += ";".join(row) + "\n" 
    return s

with open("products.csv", "r" , encoding="utf8") as F:
    header = F.readline() 
    raw_data = F.read() 


dataset = format_data(raw_data)

dataset2 = dataset
def my_hash(s):
    """Creates hash sum for given string

    Arguments:
    s: string made from kirrilick letters and spaces
    """
    d = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ, "
    s = [d.index(c) + 1 for c in s]
    p = 67
    m = 10**9 + 9
    
    h = 0
    for i in range(len(s)):
        h += (s[i]*(p**i % m)) % m
    return h % m

dataset = sorted(dataset)

dataset_no_collision = []
buf = []
for i in range(len(dataset)):
    category, product, date, price, prodano = dataset[i]
    date = tuple(date)
    if i == 0 or dataset[i-1][0] == dataset[i][0]:
        buf.append((product, date, price, prodano))
    else:
        dataset_no_collision.append((my_hash(buf[0][0]), tuple(buf)))
        buf = [(product, date, price, prodano)]

# Вот хэш-таблица, но до этой задачи она не была нужна совершенно! Мало того, что категория продукта повторяется много раз,
# так ещё и категории пробутка повторяются, от чего происходят коллизии. Я собрал все строки с продуктов одной категории в 
# кортеж, а ключем - хэш названия категории       
hash_table = dict(dataset_no_collision)


dataset = dataset2

dataset = [(r[0], r[4]) for r in sorted(dataset, key=lambda r:r[4])[:10:]]

# Вывести нужно КАТЕГОРИЮ для ПРОДУКТОВ с наименьшими продажами, потому категории повторяются
for r in dataset:
    print(f"{r[0]}, {r[1]}")
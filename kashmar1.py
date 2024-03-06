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
            category, product, date, price, count = row 
            category = category
            product = product 
            date = date.split(".")
            price = float(price)
            count = float(count) 

            table.append([category, product, date, price, count]) 

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

summ = 0
for i in range(len(dataset)):
    category, product, date, price, count = dataset[i]

    total = price * count
    if category == "Закуски":
        summ += total
    dataset[i] = [category, product, date, price, count, total]

print(summ)

for i in range(len(dataset)):
    category, product, date, price, count, total = dataset[i]
    
    price = str(price)
    count = str(count)
    date = ".".join(date)
    total = str(total)
    dataset[i] = [category, product, date, price, count, total]


serialized_dataset = header.replace("\n", ";total\n") + to_csv_string(dataset)


with open("products_new.csv","w+", encoding="utf8") as F:
    F.write(serialized_dataset) 

dataset = dataset2


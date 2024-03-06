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

"""
Промокод должен состоять из первых 2-ух букв названия
 + день поступления
 + 2 предпоследних????? буквы названия в обратном порядке
 + месяц поступления в обратном порядке.
"""
def make_promo(name, date):
    """Makes promocode from name and date of arrival of product
    
    Arguments:
    name: string naming of product
    date: list consiting of day, month, year of arrival of product
    """
    promo = date[0] + name[-2] + name[-3] + date[1][::-1]
    return promo




for i in range(len(dataset)):
    category, product, date, price, count = dataset[i]
    
    promo = make_promo(product, date)
    price = str(price)
    count = str(count)
    date = ".".join(date)
    

    dataset[i] = [category, product, date, price, count, promo]


serialized_dataset = header.replace("\n", ";promo\n") + to_csv_string(dataset)


with open("products_promo.csv","w+", encoding="utf8") as F:
    F.write(serialized_dataset) 
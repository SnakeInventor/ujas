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

categories = list(set([r[0] for r in dataset]))

mi_t_in_category = []
for category in categories:
    products = [r for r in dataset if r[0] == category]
    mi_t_in_category.append([category, min(products, key=lambda r:r[4])])


mi_t_in_category = dict(mi_t_in_category)

usr_input = input()
while(usr_input != "молоко"):
    if (usr_input not in categories):
        print(f"“Такой категории не существует в нашей БД”")
    else:
        print(f"В категории: {usr_input} товар: {mi_t_in_category[usr_input][1]} был куплен {mi_t_in_category[usr_input][4]} раз")

    usr_input = input()
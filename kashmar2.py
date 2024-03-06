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

def insert_sort(table, column_ind):
	"""Sort dataset-like 2d array by selected column
	
	Arguments:
		table: dataset-like 2d array
		element_ind: index of column, by which sorting will be performed
	"""
	for i in range (1, len(table)):
		pos = i
		current = table[pos]
		while pos > 0 and current[column_ind] < table[pos - 1][column_ind]:
			table[pos] = table[pos - 1]
			pos -= 1
		table[pos] = current
	return table




with open("products.csv", "r" , encoding="utf8") as F:
    header = F.readline() 
    raw_data = F.read() 


dataset = format_data(raw_data)

dataset = insert_sort(dataset, 0)

vipechka = [r for r in dataset if r[0] == "Выпечка"]

vipechka = insert_sort(vipechka, 3)[::-1]


category, product, date, price, count = dataset[0]
print(f"В категории: {category} самый дорогой товар: {product} его цена за единицу товара составляет {price}")
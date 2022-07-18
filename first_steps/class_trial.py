class DataBase:
    lst_data = []
    FIELDS = ('id', 'name', 'old', 'salary')
    
    def insert(self, data):                
        for row in data:
            new_lst = row.split(' ')            
            new_dict = {}
            for i in range(len(self.FIELDS)):                
                new_dict[self.FIELDS[i]] = new_lst[i]
            self.lst_data.append(new_dict)
        print(self.lst_data)
    
    def select(self, a, b):        
        print(self.lst_data[a:b])

lst_in = ['1 Сергей 35 120000', '2 Федор 23 12000', '3 Иван 13 1200']
# db = DataBase()
# db.insert(lst_in)
# db.select(0,2)

DataBase().insert(lst_in)
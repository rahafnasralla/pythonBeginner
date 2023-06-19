class fileReader: 
    def __init__(self, file):
       self.file = file
    
    def processFile(self):
        complex = open(self.file,'r')
        lines = complex.readlines()
        dates = list(())
        for line in lines[1:]:
            date = line.split(',')[0]
            if date not in dates:
              dates.append(date)
            for d in dates:
              if date == d:
                  filename = '{}.csv'
                  formatted_date = d.replace('/', '_')
                  j = open(filename.format(formatted_date), "a")
                  j.write(line)
        







    
    

class Average():
    def __init__(self):
        self.series = []

    def __call__(self, new_value):
        self.series.append(new_value)
        total = sum(self.series)
        return total / len(self.series)


#High-order Function
def make_avg():
    series = []

    def average(new_value):
        series.append(new_value)
        total = sum(series)
        return total / len(series)

    return average

#nonlocal
def mk_avg():
    count = 0
    total = 0
    
    def avg(new_val):
        nonlocal count, total
        count+=1
        total+=new_val
        return total/count
    return avg



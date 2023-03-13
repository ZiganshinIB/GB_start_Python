

def print_operation_table(operation, x, y):
    for i in range(1, x+1):
        print(*[operation(i,j) for j in range(1,y+1)], sep="\t", end='\n')

if __name__ == "__main__":
    print_operation_table(lambda x,y: x*y, 6,6)
def still_orders(items_in_orders):
    for order in items_in_orders:
        for item in order:
            if item != 'x':
                return False
    return True

if __name__ == '__main__':
    picture = []
#     f = open('/Users/sirone/picture_input.txt')
    product_type_weights = []
    warehouse_pos = []
    order_pos = []
    warehouse_products = []
    order_items = []
    count1 = 0
    f = open('/Users/sirone/Downloads/mother_of_all_warehouses.in')
    size_rows, size_columns, no_drones, max_turns, max_drone_weight = f.readline().split(' ')
    no_product_type = int(f.readline().strip('\n'))
    weights = f.readline().strip('\n').split(' ')
    for _ in range(0, no_product_type):
        product_type_weights.append((count1, weights[count1]))
        count1 += 1
    no_warehouses = int(f.readline())
    for _ in range(0, no_warehouses):
        row, col = f.readline().strip('\n').split(' ')
        warehouse_pos.append((row, col))
        product_types_no = f.readline().strip('\n').split(' ')
        warehouse_products.append(product_types_no)
    no_orders = int(f.readline().strip('\n'))
    for _ in range(0, no_orders):
        row, col = f.readline().strip('\n').split(' ')
        order_pos.append((row, col))
        no_items_order = f.readline().strip('\n')
        items_in_orders = f.readline().strip('\n').split(' ')
        order_items.append(items_in_orders)
 
    while still_orders(items_in_orders):
        pass
    
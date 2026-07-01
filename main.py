from utils import calculate_total, print_receipt


def get_quantity(item_name):
    quantity = int(input(f"{item_name} quantity: "))
    return quantity


def main():
    customer_name = input("Customer name: ")

    coffee_quantity = get_quantity("Coffee")
    tea_quantity = get_quantity("Tea")
    sandwich_quantity = get_quantity("Sandwich")

    total = calculate_total(coffee_quantity, tea_quantity, sandwich_quantity)

    print_receipt(customer_name, coffee_quantity, tea_quantity, sandwich_quantity, total)


if __name__ == "__main__":
    main()

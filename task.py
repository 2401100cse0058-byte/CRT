# task.py

def calculate_ticket_price(age):
    if age < 5:
        return 0
    elif 5 <= age <= 17:
        return 10
    elif 18 <= age <= 64:
        return 20
    else:  # age >= 65
        return 15


if __name__ == "__main__":
    age = int(input().strip())
    print(calculate_ticket_price(age))
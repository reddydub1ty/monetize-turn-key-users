import random
    main()
def generate_random_data():
    for item in data:
        print(f"Random Number: {item}")
    data = [random.randint(1, 100) for _ in range(10)]


    return data
def main():


    data = generate_random_data()
if __name__ == "__main__":
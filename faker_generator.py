import csv
import random
from faker import Faker #this library can create fake URLS amongst other things 

fake = Faker()

def generate_wishlist_data(input_csv, output_csv, num_lines=2000):
    with open(input_csv, "r") as input_file:
        reader = csv.reader(input_file)
        header = next(reader)
        data = [row for row in reader]

    with open(output_csv, "w", newline='') as output_file:
        writer = csv.writer(output_file)
        writer.writerow(header)

        for _ in range(num_lines):
            random_data = random.choice(data)
            brand = random_data[0]
            power_type = random_data[1]
            project_description = random_data[2]
            url = fake.url()
            price = float(random_data[4]) * random.uniform(0.5, 1.5)

            writer.writerow([brand, power_type, project_description, url, round(price, 2)])

generate_wishlist_data("wishlist.csv", "generated_wishlist.csv")

import csv

from db import engine
from db import Model
from db import Session
from models import Product


def main() -> None:
    Model.metadata.drop_all(engine)
    Model.metadata.create_all(engine)

    with Session() as session:
        with session.begin():
            with open('data/products.csv') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    row['year'] = int(row['year'])
                    product = Product(**row)
                    session.add(product)


if __name__ == '__main__':
    main()

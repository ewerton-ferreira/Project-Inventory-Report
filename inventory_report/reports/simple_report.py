from datetime import datetime
from collections import Counter


class SimpleReport:
    @classmethod
    def generate(cls, file):
        oldest_date = min(item["data_de_fabricacao"] for item in file)
        close_to_expiration = min(
            (
                item["data_de_validade"]
                for item in file
                if item["data_de_validade"]
                > datetime.now().strftime("%Y-%m-%d")
            ),
            default=None,
        )
        more_products = Counter(
            item["nome_da_empresa"] for item in file
        ).most_common(1)[0][0]

        return (
            f"Data de fabricação mais antiga: {oldest_date}\n"
            f"Data de validade mais próxima: {close_to_expiration}\n"
            f"Empresa com mais produtos: {more_products}"
        )

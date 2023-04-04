from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @classmethod
    def generate(cls, file):
        report = super().generate(file)
        stock_products = cls.generate_filter_company(file)
        report += "\nProdutos estocados por empresa:\n"
        for company, quantity in stock_products.items():
            report += f"- {company}: {quantity}\n"
        return report

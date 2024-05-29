import os
import pdfkit
from flask import render_template
from pydantic import BaseModel


class PdfData(BaseModel):
    invoice_name: str
    invoice_id: str
    invoice_date: str
    invoice_expiry_date: str = ""
    supplier_id: str
    supplier_name: str
    supplier_address: str
    supplier_city: str
    supplier_country: str
    customer_id: str
    customer_name: str
    customer_address: str = ""
    invoice_line_count: int = 1
    invoice_description: str = ""
    invoice_taxable_amount: str
    invoice_tax_amount: str
    invoice_price_amount: str
    invoice_pending_amount: str = ""
    invoice_text_price_amount: str
    invoice_qr_path: str
    invoice_detraction: str = ""


class PdfClient:
    def __init__(self, template):
        self.template = template
        self.directory = os.path.abspath(".")

    def create_pdf(self, name="", pdf_data=None):
        print("pdfData", pdf_data)
        self.name = f"{name}.pdf"
        self.data = PdfData(**pdf_data).dict()

        body = render_template(self.template, data=self.data)
        options = {
            "page-size": "A4",
            "encoding": "UTF-8",
            "enable-local-file-access": None,
        }
        pdfkit.from_string(body, self.name, options)
        return {"base_directory": self.directory, "filename": self.name}

"""This module sends a mail with attachment with Yagmail."""

import datetime
import locale
import yagmail
from credentials import SENDER_MAIL
from credentials import SENDER_PSWD
from credentials import RECEIPIENTS_MAIL
from credentials import COMPANY_NAME
from credentials import COMPANY_CNPJ


if __name__ == "__main__":

    # Setting the locale to BR Portuguese.
    locale.setlocale(locale.LC_ALL, "pt_BR.UTF-8")

    # Defining mail params.
    FROM_ = SENDER_MAIL
    TO = RECEIPIENTS_MAIL
    REFERENCE_DATE = datetime.datetime.now().strftime("%B-%Y")
    SUBJECT = f"NF-es {COMPANY_NAME} - {COMPANY_CNPJ} - {REFERENCE_DATE}"
    BODY = "Anexo: NF-es"
    FILE_NAMES = ["test0.txt", "test1.txt"]

    # Accessing the mail server.
    yag = yagmail.SMTP(FROM_, password=SENDER_PSWD)

    # Sending the mail.
    yag.send(to=TO, subject=SUBJECT, contents=BODY, attachments=FILE_NAMES)

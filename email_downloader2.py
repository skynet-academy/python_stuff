import pandas as pd
import xlrd
import imaplib
import email
from getpass import getpass
import os
from converter import excel_to_csv, csv_to_sql

imap_url = 'imap.gmail.com'
attachment_dir = '/home/nico/projects/python_stuff'



def authentication(imap_url):
    """
    This function authenticate into the email which we want to use using IMAP and SSL conection
    """
    user = input("put your email: \n")
    #password = input("your password: \n")
    password = getpass()
    conx = imaplib.IMAP4_SSL(imap_url)
    conx.login(user, password)
    return conx


def get_body(msg):
    """
    This function returns the body of the email
    """
    if msg.is_multipart():
        return get_body(msg.get_payload(0))
    else:
        return msg.get_payload(None, True)


def get_attachments(msg):
    """
    with this function we can download the file it contains ans stores it in a directory
    we define in the variable 'attachment_dir'
    """
    for part in msg.walk():
        if part.get_content_maintype() == 'multipart':
            continue
        if part.get('Content-Disposition') is None:
            continue

        fileName = part.get_filename()

        if bool(fileName):
            filePath = os.path.join(attachment_dir, fileName)
            with open(filePath, 'wb') as f:
                f.write(part.get_payload(decode=True))

        print("The '{}' file was download successfully in path: '{}/' ".format(fileName, attachment_dir))
    return fileName 



def search_email(key, value, conx):
    """
    key: 'FROM'
    value: the email we want to download from
    """

    result, data = conx.search(None, key, '"{}"'.format(value))
    return data


def get_emails(result_bytes):
    """
    to get all emails 
    """
    msgs = []
    for num in result_bytes[0].split():
        typ, data = conx.fetch(num, '(RFC822)')
        msgs.append(data)
    return msgs

def show_email_from():
    """
    this function shows us all emails we got from an specific email
    """
    value = input("what email do you want to search?: \n")
    print(search_email('FROM', value, conx))


if __name__ == '__main__':
    conx = authentication(imap_url)
    conx.select('INBOX')

    #msgs = get_emails(search_email('FROM', value, conx ))
    show_email_from()
    last_email = input("input one number from the list above: ")
    result, data = conx.fetch(b'183', '(RFC822)')
    raw = email.message_from_bytes(data[0][1])
    fileName = get_attachments(raw)
    excel_to_csv(fileName, '10_floor')










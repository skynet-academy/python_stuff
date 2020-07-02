import pandas as pd
import xlrd
import imaplib
import email
from getpass import getpass
import os
from converter import Converter
import sys


imap_url = 'imap.gmail.com'
attachment_dir = '/home/nico/projects/python_stuff/'



def authentication(imap_url):
    """
    This function authenticate into the email which we want to use using IMAP and SSL conection
    """
    #user = input("put your email: \n")
    #password = input("your password: \n")
    #password = getpass()
    user = 'nhspbrusiasv118@gmail.com'
    password = '123321456britanicO!'
    conx = imaplib.IMAP4_SSL(imap_url)
    try:
        conx.login(user, password)
        print("the connection to {} was successfully!".format(user))
        return conx
    except Exception as e:
        print("Error: {}".format(str(e)))
        sys.exit(1)


#def get_body(msg):
#    """
#    This function returns the body of the email
#    """
#    if msg.is_multipart():
#        return get_body(msg.get_payload(0))
#    else:
#        return msg.get_payload(None, True)
#

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

        file_name = part.get_filename()

        if bool(file_name):
            filePath = os.path.join(attachment_dir, file_name)
            with open(filePath, 'wb') as f:
                f.write(part.get_payload(decode=True))

        print("The '{}' file was download successfully in path: '{}' ".format(file_name, attachment_dir))
    #return os.path.splitext(file_name)[0]
    return file_name



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
    email_selected = input("input one number from the list above: ")
    result, data = conx.fetch(b'190', '(RFC822)')
    raw = email.message_from_bytes(data[0][1])
    file_name = get_attachments(raw)
    new_file = Converter(file_name, sheet_name=0)
    new_file.excel_to_csv()
    new_file.csv_to_sql()

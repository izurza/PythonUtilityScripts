import glob
import email

if __name__ == '__main__':
    files = glob.glob("/****/email.eml")
    for each in files:
        msg = email.message_from_file(open(each))
        attachments = msg.get_payload()
        for attachment in attachments:
            try:
                fnam = attachment.get_filename()
                f = open(fnam, 'wb').write(attachment.get_payload(decode=True,))
                f.close()
            except Exception as detail:
                pass

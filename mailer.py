'''
Maintainer : Mohit Singh
Github: devmohit-live

'''

def mailer():
    sender_email = "sender"
    receiver_email = "receiver"
    # password = getpass.getpass()
    password = 'senders_pass'

    message = MIMEMultipart("alternative")
    message["Subject"] = "Model Built Successfully"
    message["From"] = sender_email
    message["To"] = receiver_email
    
    try:
        text = """\
       This is an autogenerated mail.
        """
        html = """\
        <html>
          <body>
            <p>Hi,<br>
            <b>
               The optimal machine learning model has been built and saved in the instance : <b></b>
               <br>
            </p>
          </body>
        </html>
        """

        # Turn these into plain/html MIMEText objects
        part1 = MIMEText(text, "plain")
        part2 = MIMEText(html, "html")
        message.attach(part1)
        message.attach(part2)

        # Create secure connection with server and send email
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(
                sender_email, receiver_email, message.as_string()
            )
    except e:
        print("Some error ocurred in mailer ! ",e)
print("Mail sent succesfully!")

mailer()
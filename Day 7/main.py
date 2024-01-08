def my_print(txt):
    print(txt)
    
    
msg_template = """Hello {name},
Thank you for joining {website}. We are very
happy to have you with us.
"""

def format_msg(my_name="Brian", my_website="stompsy.dev"):
    msg.template.format(name=my_name, website=my_website)
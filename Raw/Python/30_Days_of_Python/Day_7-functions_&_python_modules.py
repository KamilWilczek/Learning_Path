def my_print(txt):
    print(txt)


my_print("Hello world")


msg_template = """ Hello {name},
Thank you for joining {website}. We are very
happy to have you with us.
"""  # .format(name='Justin', website='cfe.sh')


def format_msg(my_name="Justin", my_website="cfe.sh"):
    my_msg = msg_template.format(name=my_name, website=my_website)
    # print(my_msg)
    return my_msg


names = ["Justin", "J", "A", "Y"]

for name in names:
    this_person_msg = format_msg(my_name=name)
    print(this_person_msg)


def base_funcrion(*args, **kwargs):
    print(args, kwargs)

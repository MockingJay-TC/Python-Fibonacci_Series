def add_tags(tag=None, text=None):

    print('<{0}> {1} </{0}>'.format(tag, text))

add_tags(tag=input("Enter tag: "), text=input("Enter text: "))
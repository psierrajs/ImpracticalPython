def unicode_test(value):
    import unicodedata
    name = unicodedata.name(value)
    value2 = unicodedata.lookup(name)
    print('value= "%s", name="%s", value="%s"' % (value, name, value2))

unicode_test('@')
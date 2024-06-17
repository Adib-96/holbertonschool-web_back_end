import re
fields = ["password", "date_of_birth"]
messages = ["name=egg;email=eggmin@eggsample.com;password=eggcellent;date_of_birth=12/12/1986;",
            "name=bob;email=bob@dylan.com;password=bobbycool;date_of_birth=03/04/1993;"]


def filter_datum(fields, redaction, message, separator):
    pattern = '|'.join(f'{field}=[^{separator}]*' for field in fields)
    return re.sub(pattern, lambda m: f"{m.group(0).split('=')[0]}={redaction}", message)



for message in messages:
    print(filter_datum(fields, 'xxx', message, ';'))
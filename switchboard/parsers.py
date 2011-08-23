"""
"""


def parse_consumer(message):
    delimiter = "."
    message['payload'] = message['body'].split(delimiter)
    return message
    
def parse_meter_compressed(message):
    return message

def parse_meter_pcu(message):
    return message

def parse_meter(message):
    return message

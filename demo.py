from CulturelandPython import client


if __name__ == "__main__":
    c = client.CulturelandClient('username', 'passwd')
    c.redeem('4180-0115-2657-8251')
    c.disconnect()

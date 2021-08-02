import sqlite3
from investor import Investor
import datetime

dt = datetime.datetime.now()
datenow = "{}/{}/{}".format(dt.day,dt.month,dt.year)
timenow = "{}:{}".format(dt.hour,dt.minute)

conn = sqlite3.connect("/home/rufus/Documents/Python for Regular Use/Bitcoin/bitcoin.db")
# conn.execute('''CREATE TABLE INVESTORS
#             ( ID INTEGER PRIMARY KEY NOT NULL,
#             NAME VARCHAR(10),
#             CASH FLOAT,
#             BITCOIN FLOAT);''')
# items = conn.execute('''INSERT INTO INVESTORS(NAME,CASH,BITCOIN)
#                      VALUES ('SIMPLE',10000,0);''')
conn.commit()

# Choose latest two items
items = list(conn.execute('''SELECT PRICE,TIMESTAMP FROM
                     BITCOIN ORDER BY TIMESTAMP DESC
                     LIMIT 2;'''))
priceDifference = (items[0][0] - items[1][0])/(items[1][0])
timeDifference = items[0][1] - items[1][1]

invpercChange = timeDifference/priceDifference

person = list(conn.execute('''SELECT CASH,BITCOIN FROM INVESTORS LIMIT 1;'''))
investor1 = Investor(person[0][0],person[0][1])
if invpercChange < 360000 and priceDifference > 0 :
    investor1.allin(items[0][0])
    print("Total Worth on {} at {} is {:.2f}".format(datenow,timenow,investor1.total_worth(items[0][0])))
    conn.execute('''UPDATE INVESTORS SET CASH = {},BITCOIN =
                 {};'''.format(investor1.cash,investor1.bitcoin))

elif abs(invpercChange) < 360000 and priceDifference < 0:
    investor1.allout(items[0][0])
    print("Total Worth on {} at {} is {:.2f}".format(datenow,timenow,investor1.total_worth(items[0][0])))
    conn.execute('''UPDATE INVESTORS SET CASH = {},BITCOIN =
                 {};'''.format(investor1.cash,investor1.bitcoin))

else:
    print(invpercChange)
    print("Total Worth on {} at {} is {:.2f}".format(datenow,timenow,investor1.total_worth(items[0][0])))
    print("No exchange")
conn.commit()
conn.close()

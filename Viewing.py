# Don't Run it's just for seeing the users

import time
mycoll = db.collection(u'earnMoneyUser').get()
count = 0
for e in mycoll:
  doc = collection.document(e.id)
  res = doc.get().to_dict()
  time.sleep(0.001)
  print(count, res)
  # print(res)
  count += 1

print(count)

import time
dell = collection.where('amount', '>', 1000).get()

count  = 0
for x in dell:
  doc = collection.document(x.id).update({
      'Message': firestore.DELETE_FIELD,    # to delete the field
      'message': '[UPDATE]: Please update the app from play store now to continue earn money !'    # to input the message
  })
  print(count, doc)
  time.sleep(0.001)
  count += 1

print('Over', count)

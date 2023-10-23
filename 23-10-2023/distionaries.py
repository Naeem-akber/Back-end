file_counts ={"jpg":1,"text":14,"csv":2,"py":23}
for extension in file_counts:
  print(extension)
for ext,amount in file_counts.items():
    print("thereare{}files with the.{}extension".format(amount,ext))

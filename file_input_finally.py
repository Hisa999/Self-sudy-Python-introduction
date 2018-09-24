f = open("file_not_found_exception","w")
try:
  f.write("aaa")
except FileNotFoundError as ioe:
  print("ファイルが見つかりませんでした")
finally:
  f.close()

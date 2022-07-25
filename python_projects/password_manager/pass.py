from django import views


pwd=input("what's the master password?")

mode=input("would you like to add a new password or view an existing one")
while True:
  if mode==views:
    pass
  elif mode=="add":
    pass
  else:
    print("invalid mode")
    continue
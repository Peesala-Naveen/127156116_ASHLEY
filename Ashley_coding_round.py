password = input()
score = 0
failed = []

if len(password) >= 8:
  score += 1
else:
  failed.append("length")

if any(ch.isupper() for ch in password):
  score += 1
else:
  failed.append("uppercase")

if any(ch.islower() for ch in password):
  score += 1
else:
  failed.append("lowercase")

if any(ch.isdigit() for ch in password):
  score += 1
else:
  failed.append("digit")

special = "!@#$%^&*()_+-=[]{};:'\",.<>|~"
if any(ch in special for ch in password):
  score += 1
else:
  failed.append("special")

if " " not in password:
  score += 1
else:
  failed.append("Space")

if score == 6:
  print("Valid score:6")
else:
  print("InValid :" + ",".join(failed) + " score:" + str(score))

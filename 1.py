def count_king_lines(text):
  lines = text.split("\n")
  king_lines = 0
  for line in lines:
    if "king" in line.lower():
      king_lines += 1
  return king_lines


text = ""
line = input()
while line != "":
  text += line + "\n"
  line = input()
king_lines = count_king_lines(text)
total_lines = len(text.split("\n"))
ratio = king_lines / total_lines
print(ratio)
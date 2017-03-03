out = open("program.ws", "w")

source = "uctf_whitespace_is_best_lang"
s = ""
for sym in source:
  s += "{:>08b} ".format(ord(sym))

for sym in s.split():
  out.write("   ")
  for digit in sym:
    out.write("\t" if digit == "1" else " ")
  out.write("\n")
  out.write("\t\n  ")
out.write("\n\n\n")
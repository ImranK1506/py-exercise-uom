# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count = 0
total_confidence = 0.0
for line in fh:
    line = line.rstrip()
    if not line.startswith("X-DSPAM-Confidence:"):
        continue

    fline = line.find(":")
    value_str = line[fline + 1:]
    value = float(value_str)

    count = count + 1
    total_confidence = total_confidence + value

if count > 0:
    avg = total_confidence / count
    print("Average spam confidence:", avg)

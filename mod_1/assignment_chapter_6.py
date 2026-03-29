text = "X-DSPAM-Confidence:    0.8475"
getColon = text.find(":")
sliceToEnd = text[getColon:]
stripSpace = sliceToEnd.lstrip(":")
setNum = float(stripSpace)
print(setNum)

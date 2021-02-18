text = "X-DSPAM-Confidence:    0.8475"
a = text.find("0")
b=text[a:]
print(float(b))
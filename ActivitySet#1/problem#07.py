# Strings
# Write code using find() and string slicing (see section 6.10) to extract the number at the end of the line below. Convert the extracted value to a floating point number and print it out.
text = "X-DSPAM-Confidence:    0.8475"
ffind = text.find(':')
piece = text[ffind+1:]
end = float(piece)
print(end)
fw = open("TextFile.txt", "w")
fw.write("Hello World\n")
fw.write("Shut Up\n")
fw.close()


fx = open("TextFile.txt", "r")
text = fx.read()
print(text)
fx.close()

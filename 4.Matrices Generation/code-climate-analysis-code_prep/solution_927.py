import io
# Write a string to a buffer
output = io.StringIO()
output.write('Python Exercises, Practice, Solution')
# Retrieve the value written
print(output.getvalue())
# Discard buffer memory
output.close()

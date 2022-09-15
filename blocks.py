#
blocks = int(input("Enter the number of blocks: "))

#
# Write your code here.
#

height = 0
width = 1
while blocks >= width:
    blocks = blocks - width
    width += 1
    height += 1
print("The height of the pyramid:", height)



import subprocess, binascii

print("\nInput1\tInput2\tInput3\tInput4\tInput5\tOutput")
print("============================================")
for x in range(0, 32):
        input = '{0:05b}'.format(x)
        tab = str('\t')
        input.split()

        ret = subprocess.call(["./p1", input[0], input[1], input[2], input[3], input[4]])
        print(f"| {int(input[0])}{tab}  {int(input[1])}{tab}  {int(input[2])}{tab}  {int(input[3])}{tab}  {int(input[4])}{tab} {str(ret)} |")
        print("============================================")

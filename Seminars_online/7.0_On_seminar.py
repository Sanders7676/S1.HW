# file_read = open("data.txt", mode = "r", encoding="utf-8")
# result = []
# for line in file_read:
# tmp = line.strip().split('#')
# result.append(tmp)
# print(*tmp)
# file_read.close()

# from pathlib import Path
# MAIN_DIR = Path(__file__).parent
#
# with open(MAIN_DIR / "data" / "data.txt", mode = "r", encoding="utf-8") as file_read:
# result = []
# for line in file_read:
# tmp = line.strip().split('#')
# result.append(tmp)
# print(*tmp)


from pathlib import Path
MAIN_DIR = Path(__file__).parent

with open(MAIN_DIR / "data" / "data.txt", mode = "r", encoding="utf-8") as file_read:
result = []
for line in file_read:
tmp = line.strip().split('#')
result.append(tmp)
print(*tmp)
print("*"*20)

with open(MAIN_DIR / "result" / "res1.txt", mode = "w", encoding="utf-8") as file_write1:
with open(MAIN_DIR / "result" / "res2.txt", mode = "w", encoding="utf-8") as file_write2:
for surname, name, parent in result:
template1 = f"{surname} {name[0]}.{parent[0]}.\n"
template2 = f"{surname}-{name[0]}-{parent[0]}\n"
file_write1.write(template1)
file_write2.write(template2



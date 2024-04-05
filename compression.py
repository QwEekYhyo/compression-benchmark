import timeit, os

ARCH_NAME = "test"

def zip(path):
    os.system(f"zip -qr archives/{ARCH_NAME}.zip {path}")

def seven_zip(path):
    os.system(f"7z a archives/{ARCH_NAME}.7z {path} > /dev/null")

def rar(path) :
    os.system(f"rar a -idq -r   archives/{ARCH_NAME} {path}")

def bzip(path):
    os.system(f"tar --bzip2 -cf archives/{ARCH_NAME}.tar.bz2 {path}")

def gzip(path):
    os.system(f"tar --gzip -cf  archives/{ARCH_NAME}.tar.gz {path}")

def xz(path)  :
    os.system(f"tar --xz -cf    archives/{ARCH_NAME}.tar.xz {path}")

CMDS = [zip, seven_zip, rar, gzip, xz]

def main(path):
    results = {}

    if not os.path.exists("archives"):
        os.mkdir("archives")

    for cmd in CMDS:
        results[str(cmd).split(" ")[1]] = timeit.timeit(lambda: cmd(path),
                                                        number=1)
    return results


if __name__ == "__main__":
    PATH = "/home/logan/Downloads"

    print(main(PATH))

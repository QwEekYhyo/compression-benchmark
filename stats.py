import compression, os

def launch_benchmark(path, number):
    # setup
    strs = [ str(x).split(" ")[1] for x in compression.CMDS ]
    all_results = {}
    for name in strs:
        all_results[name] = {}

    for i in range(number):
        if i != 0:
            os.system("./clean.sh")
        results = compression.main(path)
        for name, time in results.items():
            current = all_results[name]
            if "min" not in current or time < current["min"]:
                current["min"] = time
            if "max" not in current or time > current["max"]:
                current["max"] = time
            if "average" not in current:
                current["average"] = time / number
            else:
                current["average"] += time / number
        print(f"finished round {i + 1}")

    for k, v in all_results.items():
        print(f"{k}: {v}")


if __name__ == "__main__":
    launch_benchmark("/home/logan/Downloads", 5)

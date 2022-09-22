import pysrt


def process_subs(file, rate, start=0):
    subs = pysrt.open(file)
    end_ms = subs[-1].start.ordinal
    current_ms = int(start*1000)
    while current_ms < end_ms:
        yield subs.at(pysrt.SubRipTime.from_ordinal(current_ms)).text.replace("\n", " ")
        current_ms += int(rate*10)


if __name__ == "__main__":
    iterator = process_subs(
        file="/home/inigo/stable-diffusion/inputs/Arctic-Monkeys-Do-I-Wanna-Know.srt",
        rate=5,
        start=0)
    prev = None
    for i, el in enumerate(iterator):
        if el == "":
            continue
        if el != prev:
            print(f"{i}: {el}")
            prev = el
    print(i)

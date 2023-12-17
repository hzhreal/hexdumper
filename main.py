import argparse
import os

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("File", help="Specify A File")
    args = parser.parse_args()

    if args.File and os.path.exists(args.File):
        offset = 0
        with open(args.File, "rb") as infile:
            while True:
                chunk = infile.read(16)
                if len(chunk) == 0:
                    break

                text = "".join([chr(c) if 32 <= c < 128 else "." for c in chunk])

                output = f"{offset: #08x}: "
                output += " ".join(f"{c:02X}" for c in chunk[:8])
                output += " | "
                output += " ".join(f"{c:02X}" for c in chunk[8:])

                if len(chunk) % 16 != 0:
                    output += "   " * (16 - len(chunk)) + text 
                else:
                    output += f" {text}"
                print(output)

                offset += 16

    else:
        print("Specify a file that exists!")

if __name__ == "__main__":
    main()

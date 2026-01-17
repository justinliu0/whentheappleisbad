from PIL import Image
import sys
import os

ASCII = " .:-=+*#%@"

def img_to_ascii(path, width=120):
    img = Image.open(path).convert("L")
    w, h = img.size
    aspect = h / w
    img = img.resize((width, int(width * aspect * 0.55)))
    pixels = img.getdata()
    result = ""

    for i, p in enumerate(pixels):
       result += ASCII[p * len(ASCII) // 256]
       if (i + 1) % img.width == 0:
           result += "\n"
    return result

if __name__ == "__main__":
    os.makedirs("ascii", exist_ok=True)

    for file in sorted(os.listdir("frames")):
        if not file.endswith(".png"):
            continue
        ascii_frame = img_to_ascii(f"frames/{file}")
        out = f"ascii/{file.replace('.png','.txt')}"

        with open(out, "w", encoding="utf-8") as f:
            f.write(ascii_frame)
        print("converted", file)


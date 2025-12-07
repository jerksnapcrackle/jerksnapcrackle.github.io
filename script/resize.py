import cv2
import sys

def main():
    if len(sys.argv) < 4:
        print("python resize.py <scale_factor> <is inplace> <image_path>")
        return

    scale = float(sys.argv[1])
    inplace = sys.argv[2] == "inplace"
    img_paths = sys.argv[3:]

    if inplace:
        print("Note : inplace")

    for img_path in img_paths:
        img = cv2.imread(img_path)
        if img is None:
            print("cannot read file :", img_path)
            return

        new_width = int(img.shape[1] * scale)
        new_height = int(img.shape[0] * scale)

        resized = cv2.resize(img, (new_width, new_height), interpolation=cv2.INTER_LINEAR)

        if inplace:
            out_path = img_path
        else:
            out_path = img_path.rsplit(".", 1)
            out_path = out_path[0] + f"_scaled_{scale}." + out_path[1]

        cv2.imwrite(out_path, resized)
        print("saved :", out_path)

if __name__ == "__main__":
    main()

```
Hey, check this QR code ASAP! It's highly sensitive so I scrambled it, but you shouldn't have a hard time reconstructing - just make sure to update the a_order to our shared PIN. The b_order is the reverse of that 😉
```

Using this python script it shift around the qr and after it gets a matching qr code it scans it which leads into printing the flag : `INTIGRITI{7h475_h0w_y0u_r3c0n57ruc7_qr_c0d3}`

```py
from PIL import Image, ImageDraw
from itertools import permutations
from pyzbar.pyzbar import decode

def split_square_into_triangles(img, box):
    x0, y0, x1, y1 = box
    a_triangle_points = [(x0, y0), (x1, y0), (x0, y1)]
    b_triangle_points = [(x1, y1), (x1, y0), (x0, y1)]

    def crop_triangle(points):
        mask = Image.new("L", img.size, 0)
        draw = ImageDraw.Draw(mask)
        draw.polygon(points, fill=255)
        triangle_img = Image.new("RGBA", img.size)
        triangle_img.paste(img, (0, 0), mask)
        return triangle_img.crop((x0, y0, x1, y1))

    return crop_triangle(a_triangle_points), crop_triangle(b_triangle_points)

qr_code_image = Image.open("obscured.png")
width, height = qr_code_image.size
half_width, half_height = width // 2, height // 2

squares = {
    "1": (0, 0, half_width, half_height),
    "2": (half_width, 0, width, half_height),
    "3": (0, half_height, half_width, height),
    "4": (half_width, half_height, width, height)
}

triangle_images = {}
for key, box in squares.items():
    triangle_images[f"{key}a"], triangle_images[f"{key}b"] = split_square_into_triangles(
        qr_code_image, box)

def reconstruct_qr(a_order, b_order):
    final_positions = [
        (0, 0),
        (half_width, 0),
        (0, half_height),
        (half_width, half_height)
    ]

    reconstructed_image = Image.new("RGBA", qr_code_image.size)

    for i in range(4):
        a_triangle = triangle_images[f"{a_order[i]}a"]
        b_triangle = triangle_images[f"{b_order[i]}b"]
        combined_square = Image.new("RGBA", (half_width, half_height))
        combined_square.paste(a_triangle, (0, 0))
        combined_square.paste(b_triangle, (0, 0), b_triangle)
        reconstructed_image.paste(combined_square, final_positions[i])

    return reconstructed_image

a_orders = list(permutations(["1", "2", "3", "4"]))

for a_order in a_orders:
    b_order = a_order[::-1]
    reconstructed_image = reconstruct_qr(a_order, b_order)

    reconstructed_image.save("temp_reconstructed.png")

    decoded_objects = decode(reconstructed_image)
    if decoded_objects:
        for obj in decoded_objects:
            print(f"Found QR code: {obj.data.decode('utf-8')}")
            reconstructed_image.save("final_reconstructed.png")
            break
```
![image](https://github.com/x03ee/CTF-Writeup/blob/main/2024/1337CTF-2024/misc/Quick%20Recovery/final_reconstructed.png)

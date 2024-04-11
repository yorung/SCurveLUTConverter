with open('S-curve_for_CineStyle.txt', 'r') as file:
    curve = [float(line.strip()) for line in file]

def conv(r,g,b):
    r = curve[round(r*255)]/255
    g = curve[round(g*255)]/255
    b = curve[round(b*255)]/255
    return f"{r:.6f} {g:.6f} {b:.6f}"

with open('S-curve_for_CineStyle.cube', 'wb') as file:
    file.write(b"LUT_3D_SIZE 33\n")
    file.write(b"LUT_3D_INPUT_RANGE 0.0 1.0\n")
    file.write(b"\n")

    for b in range(33):
        for g in range(33):
            for r in range(33):
                file.write((conv(r/32,g/32,b/32) + '\n').encode())

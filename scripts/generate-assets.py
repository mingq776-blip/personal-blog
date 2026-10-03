from pathlib import Path
import math
import random
from PIL import Image, ImageDraw, ImageFilter

ROOT = Path(__file__).resolve().parents[1]
COVERS = ROOT / "src" / "assets" / "covers"
PUBLIC_IMAGES = ROOT / "public" / "images"
COVERS.mkdir(parents=True, exist_ok=True)
PUBLIC_IMAGES.mkdir(parents=True, exist_ok=True)

PALETTES = {
    "post-why-blog": ["#06111f", "#0c3151", "#28d7c0", "#f4c46b"],
    "post-knowledge-system": ["#140b24", "#3b185d", "#e05c8d", "#ffd166"],
    "post-astro-site": ["#071a17", "#154a42", "#77e68b", "#d8f56b"],
    "project-ai-knowledge": ["#0b1026", "#273469", "#7f5af0", "#2cb67d"],
    "project-data-dashboard": ["#071522", "#123c56", "#ff8c42", "#f6f7eb"],
    "project-creative-site": ["#180b1e", "#572057", "#ff4d6d", "#79e6ff"],
}


def blend(a: tuple[int, int, int], b: tuple[int, int, int], t: float):
    return tuple(round(a[i] * (1 - t) + b[i] * t) for i in range(3))


def hex_rgb(value: str):
    value = value.lstrip("#")
    return tuple(int(value[i : i + 2], 16) for i in (0, 2, 4))


def gradient(size, colors, angle=32):
    width, height = size
    base = Image.new("RGB", size, colors[0])
    pixels = base.load()
    angle_rad = math.radians(angle)
    dx, dy = math.cos(angle_rad), math.sin(angle_rad)
    denom = abs(dx) * width + abs(dy) * height
    for y in range(height):
        for x in range(width):
            t = ((x * dx) + (y * dy)) / denom
            t = max(0.0, min(1.0, t))
            if t < 0.48:
                color = blend(colors[0], colors[1], t / 0.48)
            elif t < 0.82:
                color = blend(colors[1], colors[2], (t - 0.48) / 0.34)
            else:
                color = blend(colors[2], colors[3], (t - 0.82) / 0.18)
            pixels[x, y] = color
    return base


def make_cover(name: str, seed: int, size=(1400, 900)):
    random.seed(seed)
    width, height = size
    colors = [hex_rgb(color) for color in PALETTES[name]]
    image = gradient(size, colors, angle=20 + seed * 7)
    overlay = Image.new("RGBA", size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)

    for _ in range(12):
        cx = random.randint(-100, width + 100)
        cy = random.randint(-80, height + 80)
        radius = random.randint(120, 430)
        alpha = random.randint(15, 55)
        color = random.choice(colors) + (alpha,)
        draw.ellipse((cx - radius, cy - radius, cx + radius, cy + radius), fill=color)

    for index in range(7):
        radius = 80 + index * 62
        box = (width * 0.68 - radius, height * 0.38 - radius, width * 0.68 + radius, height * 0.38 + radius)
        draw.ellipse(box, outline=colors[(index + 2) % 4] + (95 - index * 7,), width=2 + index % 3)

    for _ in range(22):
        x1 = random.randint(-80, width)
        y1 = random.randint(-40, height)
        x2 = x1 + random.randint(120, 620)
        y2 = y1 + random.randint(-160, 160)
        color = random.choice(colors[1:]) + (random.randint(25, 85),)
        draw.line((x1, y1, x2, y2), fill=color, width=random.randint(1, 4))

    glow = overlay.filter(ImageFilter.GaussianBlur(28))
    image = Image.alpha_composite(image.convert("RGBA"), glow)
    image = Image.alpha_composite(image, overlay)
    noise = Image.effect_noise(size, 22).convert("L")
    image = Image.composite(image, Image.new("RGBA", size, (0, 0, 0, 255)), noise.point(lambda p: 238 + p // 12))
    vignette = Image.new("L", size, 0)
    draw_v = ImageDraw.Draw(vignette)
    draw_v.ellipse((-width * 0.2, -height * 0.3, width * 1.2, height * 1.3), fill=255)
    vignette = vignette.filter(ImageFilter.GaussianBlur(120))
    dark = Image.new("RGBA", size, (0, 0, 0, 100))
    image = Image.composite(image, Image.alpha_composite(image, dark), vignette)

    target = COVERS / f"{name}.webp"
    image.convert("RGB").save(target, "WEBP", quality=86, method=6)
    print(f"generated {target.relative_to(ROOT)}")


def make_og():
    random.seed(99)
    size = (1200, 630)
    image = gradient(size, [hex_rgb("#07111f"), hex_rgb("#163a56"), hex_rgb("#28d7c0"), hex_rgb("#f4c46b")], angle=28)
    overlay = Image.new("RGBA", size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)
    for i in range(28):
        cx, cy = random.randint(0, 1200), random.randint(0, 630)
        r = random.randint(4, 18)
        color = random.choice([(255, 255, 255), (40, 215, 192), (244, 196, 107)]) + (random.randint(35, 125),)
        draw.ellipse((cx - r, cy - r, cx + r, cy + r), fill=color)
    for i in range(9):
        draw.arc((80 + i * 18, 30 + i * 14, 1120 - i * 18, 600 - i * 12), 205, 345, fill=(255, 255, 255, 42), width=2)
    overlay = overlay.filter(ImageFilter.GaussianBlur(1.2))
    image = Image.alpha_composite(image.convert("RGBA"), overlay)
    target = PUBLIC_IMAGES / "og-default.webp"
    image.convert("RGB").save(target, "WEBP", quality=88, method=6)
    print(f"generated {target.relative_to(ROOT)}")


if __name__ == "__main__":
    for index, name in enumerate(PALETTES, start=1):
        make_cover(name, index * 17)
    make_og()


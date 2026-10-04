from pathlib import Path
import math
import random
from PIL import Image, ImageDraw, ImageFilter

ROOT = Path(r"E:/codex/个人博客")
OUT = ROOT / "src" / "assets" / "covers"
OUT.mkdir(parents=True, exist_ok=True)
PALETTES = {
    "digital-paint": ["#0d2414", "#237a3a", "#74a83b", "#b9e86b"],
    "zhongwei-luohua": ["#101e15", "#2c6139", "#6c9b4b", "#d8c27a"],
    "qingsui-ai": ["#081b12", "#17583a", "#3f9f73", "#9adf78"],
    "ancient-architecture": ["#111b13", "#425d3c", "#8b9c55", "#dce0a1"],
    "personal-blog": ["#0b2014", "#256f43", "#62ae62", "#c7eb82"],
    "pixel2motion": ["#071b12", "#1b6049", "#55b98b", "#b8e29a"],
    "cmau-survey": ["#0b1e0f", "#346d36", "#86b85d", "#e3dc8b"],
}
def rgb(v):
    v=v.lstrip('#'); return tuple(int(v[i:i+2],16) for i in (0,2,4))
def make_gradient(size, colors):
    img=Image.new('RGB',(4,4),colors[0]); pix=img.load()
    for y in range(4):
        for x in range(4):
            t=(x+y)/6
            if t<.5: c=colors[0] if t<.2 else colors[1]
            elif t<.8: c=colors[1] if t<.62 else colors[2]
            else: c=colors[2] if t<.9 else colors[3]
            pix[x,y]=c
    return img.resize(size, Image.Resampling.BICUBIC)
def make(name, seed):
    random.seed(seed); w,h=1400,900; colors=[rgb(c) for c in PALETTES[name]]
    img=make_gradient((w,h),colors).convert('RGBA')
    layer=Image.new('RGBA',(w,h),(0,0,0,0)); d=ImageDraw.Draw(layer)
    for i in range(14):
        x,y=random.randint(-100,w+100),random.randint(-80,h+80); r=random.randint(100,420); c=random.choice(colors)+(random.randint(18,54),)
        d.ellipse((x-r,y-r,x+r,y+r),fill=c)
    for i in range(20):
        x1,y1=random.randint(-50,w),random.randint(-30,h); x2=x1+random.randint(100,600); y2=y1+random.randint(-140,140)
        d.line((x1,y1,x2,y2),fill=random.choice(colors[1:])+(random.randint(25,80),),width=random.randint(1,4))
    for i in range(8):
        r=80+i*48; d.ellipse((w*.72-r,h*.42-r,w*.72+r,h*.42+r),outline=colors[(i+1)%4]+(70,),width=2)
    layer=layer.filter(ImageFilter.GaussianBlur(3))
    img=Image.alpha_composite(img,layer)
    img.convert('RGB').save(OUT/f'{name}.webp','WEBP',quality=84,method=6)
    print(name)
for i,name in enumerate(PALETTES,1): make(name,i*31)

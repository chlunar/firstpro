import math
import time
from cs1graphics import*

sun = Circle(30)
canvas = Canvas(600, 200)
canvas.add(sun)g

def interpolate_colors(t, color1, color2):
    r1, g1, b1 = color1
    r2, g2, b2 = color2
    return (int((1-t) * r1 + t * r2),
            int((1-t) * g1 + t * g2),
            int((1-t) * b1 + t * b2))

def color_value(color):
    return Color(color).getColorValue()

def animate_sunrise2(sun, morning_sun, noon_sun,morning_sky,noon_sky):
    morning_color = color_value(morning_sun)
    noon_color = color_value(noon_sun)
    dark_sky = color_value(morning_sky)
    bright_sky = color_value(noon_sky)
    w = canvas.getWidth()
    h = canvas.getHeight()
    r = sun.getRadius()
    x0 = w/2.0
    y0 = h + r
    xradius = w/2 - r
    yradius = h
    for angle in range(181):
        rad = (angle/180.0) * math.pi
        t = math.sin(rad)
        sun_col = interpolate_colors(t, morning_color, noon_color)
        sun.setFillColor(sun_col)
        sky_col = interpolate_colors(t, dark_sky, bright_sky)
        canvas.setBackgroundColor(sky_col)
        x = x0 - xradius * math.cos(rad)
        y = y0 - yradius * math.sin(rad)
        sun.moveTo(x,y)
        time.sleep(0.1)

animate_sunrise2(sun, "dark orange", "yellow", "dark blue", "deepskyblue")

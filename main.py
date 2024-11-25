import qrcode

img = qrcode.make("https://oscar-i-m-g.github.io/portafolio/")
type(img)
img.save("portafolio.png")
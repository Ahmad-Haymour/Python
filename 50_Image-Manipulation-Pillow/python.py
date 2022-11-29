#--------------------------------------------#
# --  Image Manipulation => Pillow Package  --
#--------------------------------------------#
#   Terminal =>
#       python3 -m pip install --upgrade pip
#       python3 -m pip install --upgrade Pillow
#       pip freeze                                  => To see All your Packages

from PIL import Image
from PIL import ImageEnhance


print(dir(Image))
print(dir(ImageEnhance))


## Open the Image so we can Manipulate
myImage = Image.open("/home/user/Desktop/16personalitaties.png")

enh = ImageEnhance.Contrast(myImage)
enh.enhance(1.3).show("30% more contrast")

## Show the Image
myImage.show()

# ## Crop Image
# myBox = (300, 0, 800, 800)
# myNewImage = myImage.crop(myBox)

# ## Show New Image
# myNewImage.show()

# ## My Converted Mode Image
# myConvertedImage = myImage.convert('L')

# myConvertedImage.show()
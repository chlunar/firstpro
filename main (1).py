from skimage.exposure import rescale_intensity
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt


# To-Do
# 다음 함수가 정상적인 동작을 할 수 있도록 작성합니다.
# 아래 코드에서 #이 있는 부분을 모두 새롭게 작성하신다고 생각하시면 됩니다.
def convolve(image, kernel):
    (iH, iW) = (image.shape[0], image.shape[1])  # 원본 이미지의 height, width
    (kH, kW) = (kernel.shape[0], kernel.shape[1])  # 커널의 height, width

    # 원본 이미지에 커널을 매칭시켜 컨벌류션(element wise 곱한 후 모두 더함)을 수행해야 합니다.
    # 따라서 이미지의 외곽에 있는 픽셀들을 제대로 처리 하기 위해서는 원래 이미지에 패딩을 씌워 확장을 해야 합니다.

    pad = int((kH - 1) / 2)  #

    pad_image = np.zeros((iH + 2 * pad, iW + 2 * pad))  #
    pad_image[pad:-pad, pad:-pad] = image  #

    output_image = np.copy(image.astype("float"))  #

    for y in np.arange(pad, iH + pad):
        for x in np.arange(pad, iW + pad):
            roi = pad_image[x - pad:x + pad + 1, y - pad:y + pad + 1]  # 관심영역 설정- 좌표를 잘 조정해야 합니다.
            k = (roi * kernel).sum()
            output_image[x - pad, y - pad] = k  # 새로운 값 입력

    # 처리된 결과는 그레이 스케일 이미지의 0~255가 아닌 값들이 존재합니다.
    # 따라서, 이 값들ㅇ르 적절한 범위로 리스케일 시켜줍니다.
    # 그리고 그 값을 다시 255를 곱해서 정수형으로 변환시켜줍니다.

    output_image = rescale_intensity(output_image, in_range=(0, 255))
    new_image = (output_image * 255).astype("uint8")
    return new_image


# TO-DO
# 원본 이미지를 그대로 보여주는 3*3 필터를 작성합니다.
original = np.array((
    [0, 0, 0],
    [0, 1, 0],
    [0, 0, 0]), dtype="int")

sharpen = np.array((
    [0, -1, 0],
    [-1, 5, -1],
    [0, -1, 0]), dtype="int")

# To-Do
# 1/49로 채워진 7*7배열을 만들어 주세요.
smallBlur = np.full((7, 7), 1 / 49)

laplacian = np.array((
    [0, 1, 0],
    [1, -4, 1],
    [0, 1, 0]), dtype="int")

sobelX = np.array((
    [-1, 0, 1],
    [-2, 0, 2],
    [-1, 0, 1]), dtype="int")

sobelY = np.array((
    [-1, -2, -1],
    [0, 0, 0],
    [1, 2, 1]), dtype="int")

# 위의 6가지 커널을 이름:"original"과 배열명(orginal)로 구성된 튜플의 튜플로 만들어 주세요
# To-Do
kernelBank = (
    ("original", original),
    ("sharpen", sharpen),
    ("smallBlur", smallBlur),
    ("laplacian", laplacian),
    ("sobelX", sobelX),
    ("sobelY", sobelY),
)

# 원본 이미지 로딩 및 흑백 변환
image = Image.open("test2.jpg").convert("L")
image = np.array(image)

fig = plt.figure()

for i, filter in enumerate(kernelBank):
    ax = fig.add_subplot(2, 3, i + 1)
    convolveOutput = convolve(image, filter[1])
    ax.set_title(filter[0])
    ax.imshow(convolveOutput, cmap="gray")

plt.show()

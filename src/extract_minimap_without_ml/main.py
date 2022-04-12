import cv2
import numpy as np

def main():
    img = cv2.imread('../../images/base/image_0005.jpg')

    print('img shape: ', img.shape)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imwrite('gray.jpg', gray)

    edges = cv2.Canny(gray, 50, 150, apertureSize=3)
    cv2.imwrite('canny.jpg', edges)

    kernel = np.ones((4, 4), np.uint8)
    closing = cv2.morphologyEx(edges, cv2.MORPH_CLOSE, kernel)

    cv2.imwrite('closing.jpg', closing)

    # lines = cv2.HoughLines(edges, 1, np.pi/180, 200)
    lines = cv2.HoughLines(edges, 1, np.pi/180, 100)

    print('length lines: ', len(lines))

    # for rho,theta in lines[0]:

    for line in lines[:100]:
        # print(line)
        rho, theta = line[0]
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a*rho
        y0 = b*rho
        x1 = int(x0 + 1000*(-b))
        y1 = int(y0 + 1000*(a))
        x2 = int(x0 - 1000*(-b))
        y2 = int(y0 - 1000*(a))

        cv2.line(img, (x1,y1), (x2,y2), (0,0,255), 2)

    cv2.imwrite('test.jpg',img)


if __name__ == '__main__':
    main()
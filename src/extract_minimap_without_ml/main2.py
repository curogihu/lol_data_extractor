import cv2
import numpy as np

def main():
    img = cv2.imread('image_0005.jpg')
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 50, 150, apertureSize=3)

    print('edges: ', edges)

    # kernel = np.ones((4, 4), np.uint8)
    # closing = cv2.morphologyEx(edges, cv2.MORPH_CLOSE, kernel)

    # cv2.imwrite('closing_2.jpg', closing)
    
    minLineLength = 200
    # minLineLength = 10000
    # maxLineGap = 10
    maxLineGap = 160

    lines = cv2.HoughLinesP(edges, 1, np.pi/180, 100, minLineLength, maxLineGap)
    # lines = cv2.HoughLinesP(closing, 1, np.pi/180, 100, minLineLength, maxLineGap)

    # print(img.shape)
    print('edges shape: ', edges.shape)

    height, width, _ = img.shape
    
    tmp_img = np.zeros((height, width))

    cnt = 0
    # for x1,y1,x2,y2 in lines[0]:

    '''
    Plan
    1. set a temporary image
    2. draw line to a temporary image
    3. use OpenCV function to create a rectangle, closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
    4. extract rectangle contour from original image
    '''

    for line in lines:
        # if cnt >= 2:
        #     break

        x1, y1, x2, y2 = line[0]

        # if y1 < width // 2:
        #     pass

        if x1 < int(width * 0.86):
            continue

        cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 2)

        tmp_img[x1:x2, y1:y2] = 255

        if y1 == y2:
            # add horizontal auxiliary line
            cv2.line(img, (x1, height), (x2, height), (0, 255, 0), 2)
            tmp_img[x1:x2, height] = 255

        # 3 718 205 718
        # print(x1, y1, x2, y2)
        # break

        cnt += 1

    cv2.imwrite('houghlines5.jpg', img)
    cv2.imwrite('tmp.jpg', tmp_img)

    print(np.count_nonzero(tmp_img == 255))


if __name__ == '__main__':
    main()

    print('finished.')
import cv2 #OpenCVのインポート


# for i in range(991):
# for i in range(60):
for i in range(20):    
    # base_file_path = f"../../images/base/image_{i:04}.jpg"
    # base_file_path = f"../../images/base_summoners_lift/image_{i:04}.jpg"
    base_file_path = f"../../images/base_summoners_lift/11-14_JP1-316783041_01/image_{i:04}.jpg"

    # print(base_file_path)

    img = cv2.imread(base_file_path) #画像を読み込む
    img_gray = cv2.imread(base_file_path,0) #画像をグレースケールで読み込む
    # template = cv2.imread("minimap_sample.png", 0) #テンプレート画像をグレースケールで読み込む
    template = cv2.imread("minimap_sample_2.png", 0) #テンプレート画像をグレースケールで読み込む
    width, height = template.shape[::-1] #テンプレート画像の幅、高さを取得

    result = cv2.matchTemplate(img_gray, template, cv2.TM_CCORR_NORMED) #テンプレートマッチングの実行(比較方法cv2.TM_CCORR_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result) #類似度が最小,最大となる画素の類似度、位置を調べ代入する
    top_left = max_loc #最も似ている領域を赤で囲う
    bottom_right = (top_left[0] + width, top_left[1] + height) #矩形の右下の座標計算
    # cv2.rectangle(img, top_left, bottom_right, (0, 0, 255), 2) #最も似ている領域を赤の矩形で囲う

    print(top_left, bottom_right)
    # print(base_file_path, top_left, bottom_right, max_val) #最も似ている領域の類似度を表示
    # cv2.imshow("result",img) #別ウィンドウ"result"を開きmgを表示

    # cv2.waitKey(0) #キー入力待ち
    # cv2.destroyAllWindows() #ウインドウを閉じる
    x1, y1 = top_left
    x2, y2 = bottom_right

    print(x1, x2, y1, y2)


    extracted_img = img[y1:y2, x1:x2]

    # print(img.shape)
    # print(extracted_img.shape)

    cv2.imwrite(f'aaaa_{i:04}.jpg', extracted_img)
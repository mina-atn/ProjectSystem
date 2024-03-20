import cv2 as cv

# ---------- load images ----------

model1_cam1_images = []

# # List of image file paths
model1_cam1_image_paths = [
    'D:\\WS 23-24\\master\\projekt\\python\\Model 5\\1.JPG',
    'D:\\WS 23-24\\master\\projekt\\python\\Model 5\\2.JPG',
    'D:\\WS 23-24\\master\\projekt\\python\\Model 5\\3.JPG',
    'D:\\WS 23-24\\master\\projekt\\python\\Model 5\\4.JPG',
    'D:\\WS 23-24\\master\\projekt\\python\\Model 5\\5.JPG',
    'D:\\WS 23-24\\master\\projekt\\python\\Model 5\\6.JPG',
    'D:\\WS 23-24\\master\\projekt\\python\\Model 5\\7.JPG',
    'D:\\WS 23-24\\master\\projekt\\python\\Model 5\\8.JPG',
    'D:\\WS 23-24\\master\\projekt\\python\\Model 5\\9.JPG',
    'D:\\WS 23-24\\master\\projekt\\python\\Model 5\\10.JPG',
    'D:\\WS 23-24\\master\\projekt\\python\\Model 5\\11.JPG',
    'D:\\WS 23-24\\master\\projekt\\python\\Model 5\\12.JPG',
]

def save_resized_cam1_image():
    cv.imwrite('D:\\WS 23-24\\master\\projekt\\python\\Model 5\\resized\\1.jpg', model1_cam1_images[0])
    cv.imwrite('D:\\WS 23-24\\master\\projekt\\python\\Model 5\\resized\\2.jpg', model1_cam1_images[1])
    cv.imwrite('D:\\WS 23-24\\master\\projekt\\python\\Model 5\\resized\\3.jpg', model1_cam1_images[2])
    cv.imwrite('D:\\WS 23-24\\master\\projekt\\python\\Model 5\\resized\\4.jpg', model1_cam1_images[3])
    cv.imwrite('D:\\WS 23-24\\master\\projekt\\python\\Model 5\\resized\\5.jpg', model1_cam1_images[4])
    cv.imwrite('D:\\WS 23-24\\master\\projekt\\python\\Model 5\\resized\\6.jpg', model1_cam1_images[5])
    cv.imwrite('D:\\WS 23-24\\master\\projekt\\python\\Model 5\\resized\\7.jpg', model1_cam1_images[6])
    cv.imwrite('D:\\WS 23-24\\master\\projekt\\python\\Model 5\\resized\\8.jpg', model1_cam1_images[7])
    cv.imwrite('D:\\WS 23-24\\master\\projekt\\python\\Model 5\\resized\\9.jpg', model1_cam1_images[8])
    cv.imwrite('D:\\WS 23-24\\master\\projekt\\python\\Model 5\\resized\\10.jpg', model1_cam1_images[9])
    cv.imwrite('D:\\WS 23-24\\master\\projekt\\python\\Model 5\\resized\\11.jpg', model1_cam1_images[10])
    cv.imwrite('D:\\WS 23-24\\master\\projekt\\python\\Model 5\\resized\\12.jpg', model1_cam1_images[11])

    print('resized images saved successfully!')


def prepare_images(path_list, image_list):
    for path in path_list:
        image = cv.imread(path)
        resized_iamge = cv.resize(image, (900, 600))
        image_list.append(resized_iamge)

def main():
    prepare_images(model1_cam1_image_paths, model1_cam1_images)

    save_resized_cam1_image()

    cv.waitKey(0)
    cv.destroyAllWindows()    

if __name__ == "__main__":
    main()

















import cv2 as cv
import numpy as np

# ---------- define variables ----------

model_images = []
model_heights = []
model_box_images = []

goldbeck_images = []
goldbeck_heights = []
goldbeck_box_images = []

#-------- List of image file paths ----------

model_image_paths = [
    'D:\\WS 23-24\\master\\projekt\\python\\Model 5\\resized\\1.jpg',
    'D:\\WS 23-24\\master\\projekt\\python\\Model 5\\resized\\2.jpg',
    'D:\\WS 23-24\\master\\projekt\\python\\Model 5\\resized\\3.jpg',
    'D:\\WS 23-24\\master\\projekt\\python\\Model 5\\resized\\4.jpg',
    'D:\\WS 23-24\\master\\projekt\\python\\Model 5\\resized\\5.jpg',
    'D:\\WS 23-24\\master\\projekt\\python\\Model 5\\resized\\6.jpg',
    'D:\\WS 23-24\\master\\projekt\\python\\Model 5\\resized\\7.jpg',
    'D:\\WS 23-24\\master\\projekt\\python\\Model 5\\resized\\8.jpg',
    'D:\\WS 23-24\\master\\projekt\\python\\Model 5\\resized\\9.jpg',
    'D:\\WS 23-24\\master\\projekt\\python\\Model 5\\resized\\10.jpg',
    'D:\\WS 23-24\\master\\projekt\\python\\Model 5\\resized\\11.jpg',
    'D:\\WS 23-24\\master\\projekt\\python\\Model 5\\resized\\12.jpg',
]

goldbeck_image_paths = [
    'D:\\WS 23-24\\master\\projekt\\python\\GBImages\\resized\\0.jpg',
    'D:\\WS 23-24\\master\\projekt\\python\\GBImages\\resized\\1.jpg',
    'D:\\WS 23-24\\master\\projekt\\python\\GBImages\\resized\\2.jpg',
    'D:\\WS 23-24\\master\\projekt\\python\\GBImages\\resized\\3.jpg',
    'D:\\WS 23-24\\master\\projekt\\python\\GBImages\\resized\\4.jpg',
    'D:\\WS 23-24\\master\\projekt\\python\\GBImages\\resized\\5.jpg',
    'D:\\WS 23-24\\master\\projekt\\python\\GBImages\\resized\\6.jpg',
    'D:\\WS 23-24\\master\\projekt\\python\\GBImages\\resized\\7.jpg',
    'D:\\WS 23-24\\master\\projekt\\python\\GBImages\\resized\\8.jpg',
    'D:\\WS 23-24\\master\\projekt\\python\\GBImages\\resized\\9.jpg',
]

def save_result_images(result_image_list):
    cv.imwrite('D:\\WS 23-24\\master\\projekt\\python\\Model 5\\result\\1.jpg', result_image_list[0])
    cv.imwrite('D:\\WS 23-24\\master\\projekt\\python\\Model 5\\result\\2.jpg', result_image_list[1])
    cv.imwrite('D:\\WS 23-24\\master\\projekt\\python\\Model 5\\result\\3.jpg', result_image_list[2])
    cv.imwrite('D:\\WS 23-24\\master\\projekt\\python\\Model 5\\result\\4.jpg', result_image_list[3])
    cv.imwrite('D:\\WS 23-24\\master\\projekt\\python\\Model 5\\result\\5.jpg', result_image_list[4])
    cv.imwrite('D:\\WS 23-24\\master\\projekt\\python\\Model 5\\result\\6.jpg', result_image_list[5])
    cv.imwrite('D:\\WS 23-24\\master\\projekt\\python\\Model 5\\result\\7.jpg', result_image_list[6])
    cv.imwrite('D:\\WS 23-24\\master\\projekt\\python\\Model 5\\result\\8.jpg', result_image_list[7])
    cv.imwrite('D:\\WS 23-24\\master\\projekt\\python\\Model 5\\result\\9.jpg', result_image_list[8])
    cv.imwrite('D:\\WS 23-24\\master\\projekt\\python\\Model 5\\result\\10.jpg', result_image_list[9])
    cv.imwrite('D:\\WS 23-24\\master\\projekt\\python\\Model 5\\result\\11.jpg', result_image_list[10])
    cv.imwrite('D:\\WS 23-24\\master\\projekt\\python\\Model 5\\result\\12.jpg', result_image_list[11])

    print('result images saved successfully!')

def read_images(path_list, image_list):
    for path in path_list:
        image = cv.imread(path)
        image_list.append(image)

def show_multiple_image(window_name, image_list):    
    i = 0
    for img in image_list:
        cv.imshow(window_name+str(i), img)
        i += 1

def find_height(source_image_list, result_image_list, hight_list, final_height, px_per_meter):
    
    for img in source_image_list:

        # -------- processing image ----------
        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)        
        ret, thresh = cv.threshold(gray, 90, 255, cv.THRESH_BINARY)
        contours, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)        
        largest_contour = max(contours, key=cv.contourArea)
        x, y, w, h = cv.boundingRect(largest_contour)
        
        # -------- finding hight and progress -------
        height = int(h / px_per_meter)
        progress_percent = int(height / final_height * 100)

        # --------  drawing on image --------------
        cv.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
        cv.putText(img, f'Height: {height} / {final_height} meter', (x, y-10), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)
        cv.putText(img, f'Progress: {progress_percent}%', (x, y-30), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)
        cv.drawContours(img, [largest_contour], -1, (0,255,0), 1)

        # -------- save image and height in list ----------
        result_image_list.append(img)
        hight_list.append(height)
        print(f'Height is: ', height)



def goldbeck_height():

    img = goldbeck_images[7]
    blank = np.zeros(img.shape, dtype='uint8')   
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    # blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)
    # canny = cv.Canny(blur, 125, 175)

    ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
    
    contours, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
    
    cv.drawContours(blank, contours, -1, (0,255,0), 1)

    cv.imshow('image', img)
    cv.imshow('gray', gray)
    cv.imshow('thresh', thresh)
    cv.imshow('contours', blank)

#----------------- Main method --------------------------
    
def main():

    final_height = int(input("Please enter final height: "))
    px_per_meter = int(input("Please enter number of pixels per meter of height: "))

    read_images(model_image_paths, model_images)

    find_height(model_images, model_box_images, model_heights, final_height, px_per_meter)

    show_multiple_image('Box', model_box_images)

    save_result_images(model_box_images)

    # -------- Goldbeck Methods --------------
    # read_images(goldbeck_image_paths, goldbeck_images)
    # goldbeck_height()

    cv.waitKey(0)
    cv.destroyAllWindows()    

if __name__ == "__main__":
    main()





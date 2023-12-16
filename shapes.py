import cv2  # OpenCV Library
image = cv2.imread("inputImage.png")
cv2.imshow("Before", image)
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
_, thresh_image = cv2.threshold(gray_image, 220, 255, cv2.THRESH_BINARY)

contours, hierarchy = cv2.findContours(thresh_image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
print(hierarchy)
print("*******************************")
#print(hierarchy[0][1])
#print("**************NEEXXTTT*****************")
outfaceFlag =0
#print(hierarchy[0][1][0]) #Next
#print(hierarchy[0][1][1]) #previous
#print(hierarchy[0][1][2]) #child
#print(hierarchy[0][1][3]) #parent
#print(contours[0])
print(len(contours))
for i, contour in enumerate(contours):
    #print(hierarchy[0][i])
    if i == 0:
        continue
    epsilon = 0.01 * cv2.arcLength(contour, True)
    approx = cv2.approxPolyDP(contour, epsilon, True)
    #cv2.drawContours(image, contour, 0, (0, 0, 0), 4)

    x, y, w, h = cv2.boundingRect(approx)
    x_mid = int(x)
    y_mid = int(y)
    font = cv2.FONT_HERSHEY_DUPLEX
   # cv2.putText(image, str(i), (x,y), font, 0.5, (0,0,0), 1)
    x_mid = int(x + (w / 2))
    y_mid = int(y + h / 2) - 10
    coords = (x_mid, y_mid)
    colour = (0, 0, 0)
    font = cv2.FONT_HERSHEY_DUPLEX
    ff=int(i+1)
    if (ff!=len(contours) and hierarchy[0][ff][3]==i) and (hierarchy[0][ff][2]!=-1)        and (hierarchy[0][i][3]==0):
        
        outfaceFlag = 1
        coords = (x_mid, y_mid )
      #  cv2.putText(image, str(i), (x, y), font, 0.5, (0, 0, 0), 1)
        cv2.putText(image, "Face", (int(x+(w/2)),y), font, 0.5, (0,0,255), 1)
        print("Face ", hierarchy[0][i])
        #cv2.drawContours(image, contour, 1, (0, 255, 0), 4)
        print("FAAACEEE")
        xnew=int(x+w/2)
        ynew=int(y+h/2)
        newcoords=(xnew,ynew)
        cv2.putText(image, "Nose",newcoords, font, 0.5, (255,0,255), 1)
        xnew=int(x+w/4)
        ynew=int(y+h/4)
        newcoords=(xnew,ynew)
        cv2.putText(image, "Eye",newcoords, font, 0.5, (255,0,255), 1)
        xnew=int(x+(w*0.65))
        ynew=int(y+(h*0.25))
        newcoords=(xnew,ynew)
        cv2.putText(image, "Eye",newcoords, font, 0.5, (255,0,255), 1)
        xnew=int(x+w/2)
        ynew=int(y+(h*0.75))
        newcoords=(xnew,ynew)
        cv2.putText(image, "Mouth",newcoords, font, 0.5, (255,0,255), 1)


    elif len(approx) == 2:
        if ( hierarchy[0][i][3] != 0 and outfaceFlag == 1):
            continue
        else:
            outfaceFlag == 0
        cv2.putText(image, "Line", coords, font, 0.5, colour, 1)
        print("Line ", hierarchy[0][i])

    elif len(approx) == 3:
        if (ff != len(contours) and hierarchy[0][i][3] != 0 and outfaceFlag == 1):
            continue
        else:
            outfaceFlag == 0
            if(hierarchy[0][i][3]==int(i-1) and (i-1!=0)):
                continue
        cv2.putText(image, "Triangle", coords, font, 0.5, colour, 1)
        print("Triangle ", hierarchy[0][i])
    elif len(approx) == 4:
        if (ff != len(contours) and hierarchy[0][i][3] != 0 and outfaceFlag == 1):
            continue
        else:
            outfaceFlag == 0
            if (hierarchy[0][i][3] == int(i - 1)and (i-1!=0)):
                continue
            cv2.putText(image, "Rectangle", coords, font, 0.5, colour, 1)
            print("Rec ", hierarchy[0][i])
    else:
        if (  hierarchy[0][i][3] != 0 and outfaceFlag == 1):

            continue
        else:
            if (hierarchy[0][i][3] ==0)and(hierarchy[0][i][2] == -1):

                cv2.putText(image, "Curve", coords, font, 0.5, colour, 1)
                print("Curve ", hierarchy[0][i])
                outfaceFlag == 0
                continue
            if (hierarchy[0][i][3] == int(i - 1))and (i-1!=0):
                continue
            else:
                 cv2.putText(image, "Circle", coords, font, 0.5, colour, 1)
                 print("Circle ", hierarchy[0][i])

cv2.imshow("result_shape", image)
cv2.waitKey(0)
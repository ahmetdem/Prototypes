all: compile link

compile: 
	g++ -c main.cpp -I"C:/src/OpenCV-MinGW-Build-OpenCV-4.5.5-x64/include" -std=c++17

link:
	g++ main.o -o main -L"C:/src/OpenCV-MinGW-Build-OpenCV-4.5.5-x64/x64/mingw/bin" -lsqlite3 -llibopencv_calib3d455 -llibopencv_core455 -llibopencv_dnn455 -llibopencv_features2d455 -llibopencv_flann455 -llibopencv_highgui455 -llibopencv_imgcodecs455 -llibopencv_imgproc455 -llibopencv_ml455 -llibopencv_objdetect455 -llibopencv_photo455 -llibopencv_stitching455 -llibopencv_video455 -llibopencv_videoio455

clean:
	del *.o
	del main.exe
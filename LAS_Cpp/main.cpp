#include <opencv2/opencv.hpp>
#include <iostream>
#include "db.h"

int main(int argc, char const *argv[])
{
    cv::VideoCapture cap(0);

    if (!cap.isOpened()) {
        std::cout << "Cannot open the video camera" << std::endl;
        std::cin.get();
        return -1;
    }

    cv::QRCodeDetector qrDecoder = cv::QRCodeDetector();
    bool qrCodeProcessed = false;

    cv::String window_name = "WebCam";
    cv::namedWindow(window_name, cv::WINDOW_NORMAL);

    cv::resizeWindow(window_name, 800, 600);
    std::string previousData = "";

    while (true) {
        cv::Mat frame;
        bool success = cap.read(frame);

        if (!success) {
            std::cout << "Video camera is disconnected" << std::endl;
            std::cin.get();
            break;
        }

        std::string data = qrDecoder.detectAndDecode(frame);

        if (data.length() > 0 && data != previousData) {
            std::cout << "Decoded Data: " << data << std::endl;
            insert_to_db(data);
            previousData = data;
        }

        cv::imshow(window_name, frame);

        if (cv::waitKey(10) == 27) {
            std::cout << "Esc key is pressed by the user. Stopping the video" << std::endl;
            break;
        }
    }

    return 0;
}

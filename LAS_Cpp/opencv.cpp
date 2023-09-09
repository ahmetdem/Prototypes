// #include <opencv2/opencv.hpp>
// #include <iostream>

// int main(int argc, char const *argv[])
// {
//     cv::Mat img = cv::imread("zaregoto.jpeg");

//     if (img.empty()) {
//         std::cerr << "Error: image not found" << std::endl;
//         return -1;
//     }

//     std::string window_name = "Zaregoto";

//     cv::namedWindow(window_name, cv::WINDOW_AUTOSIZE);
//     cv::imshow(window_name, img);
//     cv::waitKey(0);
//     cv::destroyWindow(window_name);

//     return 0;
// }

/*#######################################################################*/

// #include <opencv2/opencv.hpp>
// #include <iostream>

// int main(int argc, char* argv[])
// {
//     //open the video file for reading
//     cv::VideoCapture cap("madoka.mp4"); 

//     // if not success, exit program
//     if (cap.isOpened() == false)  
//     {
//         std::cout << "Cannot open the video file" << std::endl;
//         std::cin.get(); //wait for any key press
//         return -1;
//     }

//     //Uncomment the following line if you want to start the video in the middle
//     //cap.set(CAP_PROP_POS_MSEC, 300); 

//     double fps = cap.get(cv::CAP_PROP_FPS); 
//     std::cout << "Frames per seconds : " << fps << std::endl;

//     cv::String window_name = "My First Video";

//     cv::namedWindow(window_name, cv::WINDOW_NORMAL); //create a window

//     while (true)
//     {
//         cv::Mat frame;
//         bool bSuccess = cap.read(frame); // read a new frame from video 

//         //Breaking the while loop at the end of the video
//         if (bSuccess == false) 
//         {
//         std::cout << "Found the end of the video" << std::endl;
//         break;
//         }

//         //show the frame in the created window
//         imshow(window_name, frame);

//         //wait for for 10 ms until any key is pressed.  
//         //If the 'Esc' key is pressed, break the while loop.
//         //If the any other key is pressed, continue the loop 
//         //If any key is not pressed withing 10 ms, continue the loop
//         if (cv::waitKey(10) == 27)
//         {
//             std::cout << "Esc key is pressed by user. Stoppig the video" << std::endl;
//             break;
//         }
//     }

//     return 0;
// }


/*####################################################################################*/

// #include <opencv2/opencv.hpp>
// #include <iostream>

// int main(int argc, char const *argv[])
// {
//     cv::VideoCapture cap(0);
    
//     if (cap.isOpened() == false) {
//         std::cout << "Cannot open the video camera" << std::endl;
//         std::cin.get();
//         return -1;
//     }


//     double dWidth = cap.get(cv::CAP_PROP_FRAME_WIDTH);
//     double dHeight = cap.get(cv::CAP_PROP_FRAME_HEIGHT);

//     std::cout << "Resolution of the video : " << dWidth << " x " << dHeight << std::endl;

//     cv::String window_name = "WebCam";
//     cv::namedWindow(window_name, cv::WINDOW_NORMAL);

//     cv::resizeWindow(window_name, 800, 600);

//     while(true)
//     {
//         cv::Mat frame;
//         bool success = cap.read(frame);

//         if (!success) {
//             std::cout << "Video camera is disconnected" << std::endl;
//             std::cin.get();
//             break;
//         }

//         cv::imshow(window_name, frame);

//         if (cv::waitKey(10) == 27) {
//             std::cout << "Esc key is pressed by user. Stopping the video" << std::endl;
//             break;
//         }
//     }

//     return 0;
// }


/*####################################################################################*/

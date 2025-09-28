#include<iostream>
#include "opencv.hpp"
#include <opencv2/opencv.hpp>
using namespace std;

int main(){
 cv::Mat img = cv::imread("../images/circle.jpg");
 cv::Mat resized;
 cv::resize(img ,resized , cv::Size(300,300));
 if(img.empty()){
   cout<<"No image found"<<endl;
 }

 ImageProcessor processor;
 cv::Mat gray=processor.toGray(resized);
 cv::Mat blur=processor.blur(gray);
 cv::Mat edges=processor.detectEdges(blur);

 cv::imshow("Image",edges);
 cv::waitKey(0);

 return 0;
 
}

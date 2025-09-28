#ifndef OPENCV_H
#define OPENCV_H
#include <opencv2/opencv.hpp>

class ImageProcessor{
  public:
    cv::Mat toGray(const cv::Mat& img);
    cv::Mat blur(const cv::Mat & img);
    cv::Mat detectEdges(const cv::Mat& img);
};

#endif

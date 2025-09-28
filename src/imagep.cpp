#include "opencv.hpp"

cv::Mat ImageProcessor::toGray(const cv::Mat &img){
  cv::Mat gray;
  cv::cvtColor(img , gray , cv::COLOR_BGR2GRAY);
  return gray;

}

cv::Mat ImageProcessor::blur(const cv::Mat &img){
  cv::Mat blurred;
  cv::medianBlur(img , blurred ,5);
  return blurred;
}

cv::Mat ImageProcessor::detectEdges(const cv::Mat &img){
  cv::Mat edges;
  cv::Canny(img , edges,100 , 200);
  return edges;
}

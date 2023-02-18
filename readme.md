2. Contrast Adjustment
2.1. Histogram Equalization
2.1.1. Write a program that can compute the histogram of a grayscale image (assuming 256 levels of gray). In a separate
main program, apply the program to Camera Man image, and illustrate the histogram as a stem plot besides the
test image (using “subplot” function).
2.1.1.1. Decrease the brightness of Camera Man by dividing the intensity values by 3 and named output as D.
2.1.1.2. Plot the histograms of Input and D. What can you observe from these two histograms?
2.1.1.3. Perform histogram equalization on D and output the result as H.
2.1.1.4. Perform local histogram equalization on image D and output the result as L.
2.1.1.5. Plot the histograms of H and L. What’s the main difference between local and global histogram
equalization?
2.1.1.6. Perform the log transform, inverse log transform and power-law transform to enhance image D. Please
adjust the parameters to obtain the results as best as you can. Show the parameters, resultant images
and corresponding histograms. Provide some discussions on the results as well.
2.1.2. Write a program that performs histogram equalization on Camera Man image. Display the original and equalized
images, as well as their corresponding histograms, all in one figure as mentioned in 2.1.1.
2.1.3. What is the difference between histeq and imadjust functions in Matlab? Play with these functions with various
input parameters for Camera Man image. Write down your observations in your report and display results.
2.2. Local Histogram Equalization
2.2.1. Implement a local histogram equalization with different windows size for the HE1,2,3, and 4 images. Explain and
display the results. Discuss the effects of increasing window size and compare it with global histogram
equalization in detail

# docker_project_isp

It's a project that create a better qr code from a noisy one. 

## To pull docker image:

docker pull danyache/my-first-repo:initialimg

## How to run image & extract the results:

Create a folder where the results are going to be saved (for instance, let it be result_folder)
Run the following command which outputs the results to absolute_path/result_folder (where absolute_path is an absolute path to result_folder):
docker run --volume "absolute_path:/project/results" danyache/my-first-repo:initialimg

#### One file will appear -- outfile_img_test.jpeg 

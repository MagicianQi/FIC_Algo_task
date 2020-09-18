# Build FIC Algorithm Task docker image

sudo docker build -t fic_algo_task_image .

# RUN

sudo docker run \
--name fic_algo_task \
--add-host=broker1:10.8.28.130 \
--add-host=broker2:10.8.28.130 \
--add-host=broker3:10.8.28.130 \
-itd fic_algo_task_image
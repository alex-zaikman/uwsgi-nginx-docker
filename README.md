Based on https://github.com/tiangolo/uwsgi-nginx-docker
This Docker image allows you to create Python web applications that run with uWSGI and Nginx in a single container and to be used with AWS Sagemaker
It usses SAGEMAKER_BIND_TO_PORT for the listen port, addes the com.amazonaws.sagemaker.capabilities.accept-bind-to-port lable and allows sreve to be passed as a parameter.
It also installs boto3 numpy pandas sklearn scipy tensorflow flask and ta-lib

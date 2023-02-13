FROM amazon/aws-lambda-python:3.8
#RUN은 이미지에 반영
RUN /var/lang/bin/python3.8 -m pip install --upgrade pip
RUN yum install mesa-libGL -y
#필요한 패키지 
RUN pip install opencv-python && pip install --upgrade google-api-python-client && pip install --upgrade google-cloud-vision && pip install numpy && pip install python-pptx && pip install matplotlib

COPY root-amulet-358418-f65fae9b5f90.json project.py /

# Set the CMD to your handler (could also be done as a parameter override outside of the Dockerfile)
#CMD는 컨테이너에 반영
COPY . .
CMD ["project.py"]
ENTRYPOINT ["python3"]

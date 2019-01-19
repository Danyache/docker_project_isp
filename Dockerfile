FROM python:3.7

MAINTAINER Daniil.Chesakov@skoltech.ru

WORKDIR project

RUN pip install matplotlib numpy scikit-image scipy imageio

ADD qr_code.jpg ./
ADD barbara.png ./
ADD lena.bmp ./
ADD HW1_image.py ./

VOLUME /project/results

CMD ["python", "HW1_image.py"]
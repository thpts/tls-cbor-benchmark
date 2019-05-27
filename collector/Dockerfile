FROM python:3.5

WORKDIR /usr/src/app

# The original version of this library has an outstanding bug that prevents it
# writing out to a directory that is not /tmp, in which we have fixed this
# within our own fork.
#
# See also: https://github.com/CaliDog/Axeman/pull/8
RUN pip install git+https://github.com/thpts/Axeman

COPY . .

CMD ["bash", "run.sh"]

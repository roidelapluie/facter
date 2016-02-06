FROM centos:7
MAINTAINER Julien Pivotto <roidelapluie@inuits.eu>
RUN mkdir /workspace
COPY . /workspace
RUN yum install -y /usr/bin/spectool /usr/bin/rpmbuild /usr/bin/yum-builddep

RUN mkdir -p /root/rpmbuild/SOURCES

RUN spectool -C /root/rpmbuild/SOURCES -g /workspace/facter.spec
RUN yum-builddep -y /workspace/facter.spec
RUN rpmbuild -ba /workspace/facter.spec
VOLUME /artifacts

FROM centos:7

MAINTAINER Julien Pivotto <roidelapluie@inuits.eu>

RUN mkdir /workspace
COPY . /workspace

RUN yum install -y /usr/bin/spectool /usr/bin/rpmbuild /usr/bin/yum-builddep


RUN useradd bob
RUN mkdir -p /home/bob/rpmbuild/SOURCES



RUN spectool -C /home/bob/rpmbuild/SOURCES -g /workspace/facter.spec
RUN yum-builddep -y /workspace/facter.spec

RUN chown -R bob: /home/bob /workspace

RUN rpmbuild -ba /workspace/facter.spec

VOLUME /artifacts
